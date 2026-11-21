#!/usr/bin/env python3
"""KVKK süre hesaplayıcı.

Yalnız standart kütüphane kullanır, ağa çıkmaz, dosya yazmaz.

Örnekler:
  python3 sure_hesapla.py basvuru-cevap --ulasma 2026-03-02
  python3 sure_hesapla.py sikayet --basvuru 2026-03-02 --cevap-ogrenme 2026-03-20
  python3 sure_hesapla.py ihlal --ogrenme "2026-03-06 16:00"
  python3 sure_hesapla.py ss-bildirim --son-imza 2026-05-18 --tatil 2026-05-27,2026-05-28,2026-05-29,2026-05-30
  python3 sure_hesapla.py kurul-istem --teblig 2026-04-01
  python3 sure_hesapla.py kurul-karar --teblig 2026-04-01
  python3 sure_hesapla.py zimni-ret --sikayet 2026-04-01
  python3 sure_hesapla.py iptal-davasi --teblig 2026-06-10

Sabit tarihli resmî tatiller (1 Ocak, 23 Nisan, 1 Mayıs, 19 Mayıs, 15 Temmuz,
30 Ağustos, 29 Ekim) kendiliğinden sayılır. Dini bayramların tam günlerini
(2429 sayılı Kanun m.2/B) --tatil ile ver; betik bunları bilmez. Bayramın bütün
tam günlerini yaz. İdari izin günlerini --tatil ile verme: 2429 sayılı Kanunda
sayılan tatillerden değildir. Yarım günleri (arife, 28 Ekim öğleden sonrası) de
verme: betik bunları iş günü sayar, ihtiyatlı sonuç budur.

Sonuç bir hesap yardımıdır. Tetikleyici tarihi, tebliğ sayılma anını ve güncel
mevzuatı ayrıca doğrula.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass, field
from datetime import date, datetime, timedelta

SABIT_TATILLER = {(1, 1), (4, 23), (5, 1), (5, 19), (7, 15), (8, 30), (10, 29)}
GUN_ADLARI = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]


@dataclass
class Sonuc:
    ad: str
    tetikleyici: str
    kural: str
    dayanak: str
    gun_turu: str
    son_tarih: str
    aciklama: list[str] = field(default_factory=list)
    uyarilar: list[str] = field(default_factory=list)


def tarih_oku(metin: str) -> date:
    try:
        return datetime.strptime(metin.strip(), "%Y-%m-%d").date()
    except ValueError as hata:
        raise argparse.ArgumentTypeError(f"Tarih YYYY-AA-GG biçiminde olmalı: {metin!r}") from hata


def an_oku(metin: str) -> datetime:
    temiz = metin.strip().replace("T", " ")
    for bicim in ("%Y-%m-%d %H:%M", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(temiz, bicim)
        except ValueError:
            continue
    raise argparse.ArgumentTypeError(f"Tarih ve saat 'YYYY-AA-GG SS:DD' biçiminde olmalı: {metin!r}")


def tatil_listesi(metin: str | None, dosya: str | None) -> set[date]:
    gunler: set[date] = set()
    parcalar: list[str] = []
    if metin:
        parcalar.extend(metin.split(","))
    if dosya:
        with open(dosya, encoding="utf-8-sig") as akis:
            for satir in akis:
                parcalar.extend(satir.split("#", 1)[0].split(","))
    for parca in parcalar:
        if parca.strip():
            gunler.add(tarih_oku(parca))
    return gunler


def gun_adi(gun: date) -> str:
    return GUN_ADLARI[gun.weekday()]


def yaz(gun: date) -> str:
    return f"{gun.isoformat()} {gun_adi(gun)}"


def tatil_mi(gun: date, tatiller: set[date]) -> bool:
    return gun.weekday() >= 5 or (gun.month, gun.day) in SABIT_TATILLER or gun in tatiller


def sonraki_is_gunu(gun: date, tatiller: set[date]) -> date:
    while tatil_mi(gun, tatiller):
        gun += timedelta(days=1)
    return gun


def takvim_gunu_ekle(baslangic: date, gun_sayisi: int) -> date:
    """Tetikleyici gün sayılmaz; süre izleyen gün işlemeye başlar."""
    return baslangic + timedelta(days=gun_sayisi)


def is_gunu_ekle(baslangic: date, gun_sayisi: int, tatiller: set[date]) -> date:
    gun = baslangic
    kalan = gun_sayisi
    while kalan > 0:
        gun += timedelta(days=1)
        if not tatil_mi(gun, tatiller):
            kalan -= 1
    return gun


def tatil_notu(son: date, tatiller: set[date]) -> list[str]:
    """Açık uzama kuralı bulunmayan sürelerde ihtiyatlı tarihi korur."""
    if not tatil_mi(son, tatiller):
        return []
    return [
        f"Son gün tatile rastlıyor. İhtiyatlı tarih {yaz(son)}. "
        f"Tatil nedeniyle uzama kabul edilirse {yaz(sonraki_is_gunu(son, tatiller))}. "
        "Uzamanın bu süreye uygulanıp uygulanmadığını dayanağıyla doğrula."
    ]


def dini_bayram_uyarisi(tatiller: set[date]) -> list[str]:
    if tatiller:
        return []
    return [
        "Dini bayram günleri verilmedi. Süre bu günlere rastlıyorsa --tatil ile yeniden hesapla. "
        "İdari izin günlerini tatil olarak verme; 2429 sayılı Kanunda sayılan tatillerden değildir."
    ]


def is_gunu_tatil_uyarilari(baslangic: date, son: date, tatiller: set[date]) -> list[str]:
    uyarilar: list[str] = []
    kullanilan = sorted(g for g in tatiller if baslangic < g < son)
    if not kullanilan:
        uyarilar.append(
            "--tatil ile verilen günlerden hiçbiri süreye rastlamadı ya da hiç tatil verilmedi. "
            "Süre dini bayrama rastlıyorsa bayramın tam günlerini --tatil ile verip yeniden hesapla."
        )
    else:
        uyarilar.append(
            "İş günü sayılmayan ek günler: " + ", ".join(yaz(g) for g in kullanilan) + ". "
            "Aralarında yarım gün (arife, 28 Ekim) veya idari izin varsa çıkarıp yeniden hesapla."
        )
    if (son - timedelta(days=1)) in tatiller or (son + timedelta(days=1)) in tatiller:
        uyarilar.append(
            f"Son tarih {yaz(son)} verilen tatil günlerine bitişik. Bayramın bütün günlerini "
            "verdiğini doğrula; eksik gün varsa son tarih tatile rastlıyor olabilir."
        )
    uyarilar.append(
        "Yarım günler (arife, 28 Ekim öğleden sonrası) iş günü sayıldı. "
        "Son gün yarım güne rastlıyorsa bildirimi öğleden önce ya da bir önceki iş günü yap."
    )
    return uyarilar


def basvuru_cevap(ulasma: date, tatiller: set[date]) -> Sonuc:
    son = takvim_gunu_ekle(ulasma, 30)
    return Sonuc(
        ad="Veri sorumlusunun başvuruya cevabı",
        tetikleyici=f"Başvurunun veri sorumlusuna ulaşması: {yaz(ulasma)}",
        kural="En kısa sürede ve en geç 30 gün",
        dayanak="6698 m.13/2",
        gun_turu="Takvim günü, ulaşma günü sayılmaz",
        son_tarih=yaz(son),
        aciklama=["Silme talebi haklıysa İmha Yönetmeliği m.12'deki 30 günlük süre de aynı tarihte dolar."],
        uyarilar=tatil_notu(son, tatiller),
    )


def sikayet(basvuru: date, cevap_ogrenme: date | None, tatiller: set[date]) -> Sonuc:
    cevap_suresi_sonu = takvim_gunu_ekle(basvuru, 30)
    ust_sinir = takvim_gunu_ekle(basvuru, 60)
    aciklama = [
        f"Veri sorumlusunun cevap süresi sonu: {yaz(cevap_suresi_sonu)}",
        f"Başvurudan itibaren 60 günlük üst sınır: {yaz(ust_sinir)}",
    ]
    uyarilar: list[str] = []
    if cevap_ogrenme is None:
        son = ust_sinir
        kural = "Cevap yok: başvurudan itibaren 60 gün"
        tetikleyici = f"Başvuru: {yaz(basvuru)}, cevap yok"
        uyarilar.append(f"Şikâyet {yaz(cevap_suresi_sonu)} tarihinden önce yapılırsa cevap süresi dolmamış olur.")
    elif cevap_ogrenme < basvuru:
        raise SystemExit("Hata: cevabı öğrenme tarihi başvuru tarihinden önce olamaz.")
    elif cevap_ogrenme <= cevap_suresi_sonu:
        ogrenmeden = takvim_gunu_ekle(cevap_ogrenme, 30)
        son = min(ogrenmeden, ust_sinir)
        kural = "Süresinde cevap: öğrenmeden itibaren 30 gün ve her hâlde başvurudan itibaren 60 gün"
        tetikleyici = f"Başvuru: {yaz(basvuru)}, cevabı öğrenme: {yaz(cevap_ogrenme)}"
        aciklama.append(f"Öğrenmeden itibaren 30 gün: {yaz(ogrenmeden)}")
    else:
        son = ust_sinir
        kural = "Geç cevap yeni süre başlatmaz: başvurudan itibaren 60 gün"
        tetikleyici = f"Başvuru: {yaz(basvuru)}, cevabı öğrenme: {yaz(cevap_ogrenme)} (30 günden sonra)"
        if cevap_ogrenme > ust_sinir:
            uyarilar.append("Cevap 60 günlük üst sınırdan sonra öğrenilmiş. Şikâyet süresi dolmuş olabilir.")
    uyarilar.extend(tatil_notu(son, tatiller))
    return Sonuc(
        ad="Kurula şikâyet",
        tetikleyici=tetikleyici,
        kural=kural,
        dayanak="6698 m.14/1 ve 2019/9 sayılı Kurul kararı",
        gun_turu="Takvim günü, tetikleyici gün sayılmaz",
        son_tarih=yaz(son),
        aciklama=aciklama,
        uyarilar=uyarilar,
    )


def ihlal(ogrenme: datetime) -> Sonuc:
    son = ogrenme + timedelta(hours=72)
    return Sonuc(
        ad="Veri ihlalinin Kurula bildirimi",
        tetikleyici=f"Veri sorumlusunun öğrenmesi: {ogrenme:%Y-%m-%d %H:%M} {gun_adi(ogrenme.date())} (Türkiye saati)",
        kural="Gecikmeksizin ve en geç 72 saat",
        dayanak="6698 m.12/5 ve 2019/10 sayılı Kurul kararı",
        gun_turu="Kesintisiz saat, hafta sonu ve tatil dâhil",
        son_tarih=f"{son:%Y-%m-%d %H:%M} {gun_adi(son.date())}",
        aciklama=[
            "Süre ihlalin gerçekleştiği andan değil veri sorumlusunun öğrendiği andan başlar.",
            "İlgili kişilere bildirim için ayrı ölçüt uygulanır: belirlendikten sonra makul olan en kısa süre.",
        ],
        uyarilar=["Bilgiler eksikse mevcut bilgiyle ilk bildirimi yap, tamamlayıcı bildirimi planla."],
    )


def ss_bildirim(son_imza: date, tatiller: set[date]) -> Sonuc:
    son = is_gunu_ekle(son_imza, 5, tatiller)
    # İhtiyatlı seçenek: Cumartesi iş günü sayılırsa.
    ihtiyatli = son_imza
    kalan = 5
    while kalan > 0:
        ihtiyatli += timedelta(days=1)
        cumartesi_is_gunu = (
            ihtiyatli.weekday() == 5
            and (ihtiyatli.month, ihtiyatli.day) not in SABIT_TATILLER
            and ihtiyatli not in tatiller
        )
        if cumartesi_is_gunu or not tatil_mi(ihtiyatli, tatiller):
            kalan -= 1
    cumartesi_uyarisi = (
        "Cumartesi ve Pazar iş günü sayılmadı. 6698 m.9/5 \"iş günü\"nü tanımlamaz. "
        f"Cumartesi iş günü sayılırsa son tarih {yaz(ihtiyatli)}. Tereddütte bu erken tarihe göre bildir."
    )
    return Sonuc(
        ad="Standart sözleşmenin Kuruma bildirimi",
        tetikleyici=f"Son imza: {yaz(son_imza)}",
        kural="İmzadan itibaren 5 iş günü",
        dayanak="6698 m.9/5 ve Aktarım Yönetmeliği m.14",
        gun_turu="İş günü (Cumartesi ve Pazar sayılmadı), imza günü sayılmaz",
        son_tarih=yaz(son),
        aciklama=["Kaydetme ile Kuruma iletim ayrı adımlardır. Süre iletimle karşılanır."],
        uyarilar=is_gunu_tatil_uyarilari(son_imza, son, tatiller) + [cumartesi_uyarisi],
    )


def duz_sure(ad: str, tetikleyici_adi: str, tetikleyici: date, gun: int, kural: str, dayanak: str,
             tatiller: set[date], aciklama: list[str] | None = None) -> Sonuc:
    son = takvim_gunu_ekle(tetikleyici, gun)
    return Sonuc(
        ad=ad,
        tetikleyici=f"{tetikleyici_adi}: {yaz(tetikleyici)}",
        kural=kural,
        dayanak=dayanak,
        gun_turu="Takvim günü, tetikleyici gün sayılmaz",
        son_tarih=yaz(son),
        aciklama=aciklama or [],
        uyarilar=tatil_notu(son, tatiller),
    )


def iptal_davasi(teblig: date, tatiller: set[date]) -> Sonuc:
    ham = takvim_gunu_ekle(teblig, 60)
    son = ham
    aciklama = [f"Tebliği izleyen günden itibaren 60. gün: {yaz(ham)}"]
    uyarilar: list[str] = []
    ara_bas = date(ham.year, 7, 20)
    ara_son = date(ham.year, 8, 31)
    if ara_bas <= ham <= ara_son:
        son = date(ham.year, 9, 7)
        aciklama.append(
            "Süre sonu çalışmaya ara verme dönemine (20 Temmuz–31 Ağustos) rastlıyor. "
            f"İYUK m.8/3 uyarınca ara vermenin bittiği günü izleyen tarihten itibaren yedi gün: {yaz(son)}"
        )
        uyarilar.append("Çalışmaya ara verme uzamasını ve nöbetçi mahkeme uygulamasını güncel İYUK m.8 ve m.61 ile doğrula.")
    if tatil_mi(son, tatiller):
        # Uzama yalnız hafta sonu ve sabit resmî tatile dayanıyorsa kendiliğinden uygulanır.
        # --tatil ile verilen güne dayanıyorsa ihtiyatlı tarih korunur.
        ihtiyatli = sonraki_is_gunu(son, set())
        uzamis = sonraki_is_gunu(son, tatiller)
        if uzamis == ihtiyatli:
            aciklama.append(f"Son gün tatil. İYUK m.8/2 uyarınca izleyen çalışma günü: {yaz(uzamis)}")
        else:
            aciklama.append(
                f"--tatil ile verilen günler 2429 sayılı Kanundaki tatil günleriyse İYUK m.8/2 uyarınca süre {yaz(uzamis)} gününe uzar."
            )
            uyarilar.append(
                f"Son tarih ihtiyatlı olarak {yaz(ihtiyatli)} gösterildi; uzama --tatil ile verilen günlere dayanıyor. "
                "İdari izin günleri 2429 sayılı Kanunda sayılan tatillerden değildir; süreyi uzattığını varsayma. "
                "Arife ve 28 Ekim yalnız öğleden sonra tatildir; son gün yarım güne rastlıyorsa uzamayı içtihatla doğrula."
            )
        if date(ihtiyatli.year, 7, 20) <= ihtiyatli <= date(ihtiyatli.year, 8, 31):
            olasi = sonraki_is_gunu(date(ihtiyatli.year, 9, 7), tatiller)
            aciklama.append(
                "m.8/2 ile uzayan son gün çalışmaya ara verme dönemine (20 Temmuz–31 Ağustos) rastlıyor. "
                f"m.8/3'ün bu durumda da uygulanacağı kabul edilirse süre {yaz(olasi)} gününe uzar. "
                "Bu hesap doğrulanmadı; son tarih olarak erken olan, ihtiyatlı tarih gösterildi."
            )
            uyarilar.append(
                "İYUK m.8/2 ve m.8/3'ün birlikte uygulanmasına ilişkin güncel Danıştay içtihadını doğrula. "
                "Doğrulanana kadar davayı erken tarihe göre aç."
            )
        son = ihtiyatli
    uyarilar.extend(dini_bayram_uyarisi(tatiller))
    uyarilar.append("Tebliğ sayılma tarihini kanalına göre belirle (e-tebligat, KEP, posta). Özel süre veya usul hükmü varsa o uygulanır.")
    return Sonuc(
        ad="İdare mahkemesinde iptal davası",
        tetikleyici=f"Yazılı bildirim (tebliğ): {yaz(teblig)}",
        kural="Özel süre yoksa 60 gün",
        dayanak="6698 m.18/3, İYUK m.7 ve m.8",
        gun_turu="Takvim günü, tebliği izleyen günden başlar, tatil günleri dâhil",
        son_tarih=yaz(son),
        aciklama=aciklama,
        uyarilar=uyarilar,
    )


def zimni_ret(sikayet_tarihi: date, tatiller: set[date]) -> Sonuc:
    ret = takvim_gunu_ekle(sikayet_tarihi, 60)
    dava = iptal_davasi(ret, tatiller)
    aciklama = [
        "Bu tarih ilgili kişinin işlem yapması gereken bir son gün değildir. Kurulun cevap süresinin son günüdür; "
        "o gün sonuna kadar cevap verilmezse talep reddedilmiş sayılır.",
        "Zımni redde karşı dava süresi ihtiyatlı hesapla bu tarihi izleyen günden başlar. "
        f"60 günlük dava süresinin ihtiyatlı son günü: {dava.son_tarih}",
    ]
    aciklama.extend(f"Dava süresi hesabı: {satir}" for satir in dava.aciklama[1:])
    uyarilar: list[str] = []
    if tatil_mi(ret, tatiller):
        uyarilar.append(
            "Cevap süresinin son günü tatile rastlıyor. Dava süresinin başlangıcı için uzamaya güvenme, "
            f"hesabı {yaz(ret)} tarihine göre yap."
        )
    uyarilar.append(
        "Görevli yargı yolunu, dava süresini ve zımni retten sonra gelen açık cevabın süreye etkisini "
        "güncel İYUK hükümleri ve içtihatla doğrula."
    )
    uyarilar.extend(u for u in dava.uyarilar if not u.startswith("Tebliğ sayılma"))
    return Sonuc(
        ad="Şikâyetin zımnen reddi",
        tetikleyici=f"Kurula şikâyet: {yaz(sikayet_tarihi)}",
        kural="60 gün içinde cevap verilmezse talep reddedilmiş sayılır",
        dayanak="6698 m.15/4",
        gun_turu="Takvim günü, tetikleyici gün sayılmaz",
        son_tarih=f"{yaz(ret)} (zımni ret tarihi, Kurulun cevap süresinin son günü)",
        aciklama=aciklama,
        uyarilar=uyarilar,
    )


def metin_cikti(sonuc: Sonuc) -> str:
    satirlar = [
        sonuc.ad,
        f"  Tetikleyici : {sonuc.tetikleyici}",
        f"  Kural       : {sonuc.kural}",
        f"  Dayanak     : {sonuc.dayanak}",
        f"  Gün türü    : {sonuc.gun_turu}",
        f"  Son tarih   : {sonuc.son_tarih}",
    ]
    for satir in sonuc.aciklama:
        satirlar.append(f"  Not         : {satir}")
    for satir in sonuc.uyarilar:
        satirlar.append(f"  Uyarı       : {satir}")
    satirlar.append("  Tetikleyici tarihi ve tatil günlerini kanıtıyla doğrula.")
    return "\n".join(satirlar)


def ayristirici() -> argparse.ArgumentParser:
    ortak = argparse.ArgumentParser(add_help=False)
    ortak.add_argument("--tatil", help="Virgülle ayrılmış dini bayram tam günleri (YYYY-AA-GG); idari izin ve yarım gün verme")
    ortak.add_argument("--tatil-dosyasi", help="Tatil günleri dosyası (UTF-8): satır başına bir veya virgülle ayrılmış birden çok YYYY-AA-GG; # sonrası yorum sayılır")
    ortak.add_argument("--json", action="store_true", help="Sonucu JSON olarak yaz")

    ana = argparse.ArgumentParser(description="KVKK süre hesaplayıcı")
    alt = ana.add_subparsers(dest="komut", required=True)

    p = alt.add_parser("basvuru-cevap", parents=[ortak], help="m.13/2: başvuruya cevap, 30 gün")
    p.add_argument("--ulasma", required=True, type=tarih_oku)

    p = alt.add_parser("sikayet", parents=[ortak], help="m.14/1: Kurula şikâyet, 30/60 gün")
    p.add_argument("--basvuru", required=True, type=tarih_oku)
    p.add_argument("--cevap-ogrenme", type=tarih_oku)

    p = alt.add_parser("ihlal", parents=[ortak], help="2019/10: ihlal bildirimi, 72 saat")
    p.add_argument("--ogrenme", required=True, type=an_oku)

    p = alt.add_parser("ss-bildirim", parents=[ortak], help="m.9/5: standart sözleşme bildirimi, 5 iş günü")
    p.add_argument("--son-imza", required=True, type=tarih_oku)

    p = alt.add_parser("kurul-istem", parents=[ortak], help="m.15/3: Kurulun bilgi ve belge istemi, 15 gün")
    p.add_argument("--teblig", required=True, type=tarih_oku)

    p = alt.add_parser("kurul-karar", parents=[ortak], help="m.15/5: giderim kararının yerine getirilmesi, 30 gün")
    p.add_argument("--teblig", required=True, type=tarih_oku)

    p = alt.add_parser("zimni-ret", parents=[ortak], help="m.15/4: şikâyetin zımnen reddi, 60 gün")
    p.add_argument("--sikayet", required=True, type=tarih_oku)

    p = alt.add_parser("iptal-davasi", parents=[ortak], help="İYUK m.7: iptal davası, 60 gün")
    p.add_argument("--teblig", required=True, type=tarih_oku)
    return ana


def calistir(argv: list[str] | None = None) -> Sonuc:
    ana = ayristirici()
    args = ana.parse_args(argv)
    try:
        tatiller = tatil_listesi(args.tatil, args.tatil_dosyasi)
    except argparse.ArgumentTypeError as hata:
        ana.error(f"--tatil / --tatil-dosyasi: {hata}")
    except (OSError, UnicodeDecodeError) as hata:
        ana.error(f"--tatil-dosyasi okunamadı: {hata}")
    if args.komut == "basvuru-cevap":
        sonuc = basvuru_cevap(args.ulasma, tatiller)
    elif args.komut == "sikayet":
        sonuc = sikayet(args.basvuru, args.cevap_ogrenme, tatiller)
    elif args.komut == "ihlal":
        sonuc = ihlal(args.ogrenme)
    elif args.komut == "ss-bildirim":
        sonuc = ss_bildirim(args.son_imza, tatiller)
    elif args.komut == "kurul-istem":
        sonuc = duz_sure(
            "Kurulun bilgi ve belge istemine cevap", "Yazının tebliği", args.teblig, 15,
            "15 gün", "6698 m.15/3", tatiller,
            ["Yazıda ayrı bir süre veya talimat varsa onu da karşıla. Ek süre talebi süreyi kendiliğinden durdurmaz."],
        )
    elif args.komut == "kurul-karar":
        sonuc = duz_sure(
            "Kurulun giderim kararının yerine getirilmesi", "Kararın tebliği", args.teblig, 30,
            "Gecikmeksizin ve en geç 30 gün", "6698 m.15/5", tatiller,
            ["Dava açmak kararın yürütmesini kendiliğinden durdurmaz."],
        )
    elif args.komut == "zimni-ret":
        sonuc = zimni_ret(args.sikayet, tatiller)
    else:
        sonuc = iptal_davasi(args.teblig, tatiller)
    if args.json:
        print(json.dumps(asdict(sonuc), ensure_ascii=False, indent=2))
    else:
        print(metin_cikti(sonuc))
    return sonuc


if __name__ == "__main__":
    try:
        calistir()
    except BrokenPipeError:
        sys.exit(0)

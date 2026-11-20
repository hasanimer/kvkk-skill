"""sure_hesapla.py için birim testleri.

Çalıştırma: python3 -m unittest discover -s tests -v
"""

import contextlib
import io
import sys
import unittest
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills" / "kvkk" / "scripts"))

import sure_hesapla as s  # noqa: E402

BOS: set[date] = set()


class BasvuruVeSikayet(unittest.TestCase):
    def test_cevap_suresi_otuz_takvim_gunu(self):
        sonuc = s.basvuru_cevap(date(2026, 3, 2), BOS)
        self.assertTrue(sonuc.son_tarih.startswith("2026-04-01"))

    def test_suresinde_cevapta_ogrenmeden_otuz_gun(self):
        sonuc = s.sikayet(date(2026, 3, 2), date(2026, 3, 20), BOS)
        self.assertTrue(sonuc.son_tarih.startswith("2026-04-19"))

    def test_altmis_gun_ust_siniri_ogrenmeden_otuz_gunu_keser(self):
        # 30. günde öğrenilen cevap: öğrenme + 30 = başvuru + 60
        sonuc = s.sikayet(date(2026, 3, 2), date(2026, 4, 1), BOS)
        self.assertTrue(sonuc.son_tarih.startswith("2026-05-01"))

    def test_kirkinci_gun_cevabi_yeni_sure_baslatmaz(self):
        # EVALUATION senaryosu: cevap 40. günde geliyor
        basvuru = date(2026, 3, 2)
        sonuc = s.sikayet(basvuru, date(2026, 4, 11), BOS)
        self.assertTrue(sonuc.son_tarih.startswith("2026-05-01"))
        self.assertIn("yeni süre başlatmaz", sonuc.kural)

    def test_cevap_yoksa_altmis_gun(self):
        sonuc = s.sikayet(date(2026, 3, 2), None, BOS)
        self.assertTrue(sonuc.son_tarih.startswith("2026-05-01"))

    def test_ust_sinirdan_sonra_ogrenilen_cevap_uyari_verir(self):
        sonuc = s.sikayet(date(2026, 3, 2), date(2026, 5, 10), BOS)
        self.assertTrue(any("dolmuş olabilir" in u for u in sonuc.uyarilar))

    def test_ogrenme_basvurudan_once_olamaz(self):
        with self.assertRaises(SystemExit):
            s.sikayet(date(2026, 3, 2), date(2026, 3, 1), BOS)

    def test_tatile_rastlayan_son_gun_ihtiyatli_tarihi_korur(self):
        # 2026-03-06 Cuma + 30 gün = 2026-04-05 Pazar
        sonuc = s.basvuru_cevap(date(2026, 3, 6), BOS)
        self.assertTrue(sonuc.son_tarih.startswith("2026-04-05"))
        self.assertTrue(any("2026-04-06" in u for u in sonuc.uyarilar))


class Ihlal(unittest.TestCase):
    def test_cuma_onalti_pazartesi_onalti(self):
        # EVALUATION senaryosu: cuma 16.00'da öğrenilen ihlal
        sonuc = s.ihlal(datetime(2026, 3, 6, 16, 0))
        self.assertEqual(sonuc.son_tarih, "2026-03-09 16:00 Pazartesi")

    def test_hafta_sonu_cikarilmaz(self):
        sonuc = s.ihlal(datetime(2026, 3, 7, 9, 30))
        self.assertEqual(sonuc.son_tarih, "2026-03-10 09:30 Salı")


class StandartSozlesme(unittest.TestCase):
    def test_bes_is_gunu_hafta_sonunu_atlar(self):
        # 2026-03-04 Çarşamba -> Per, Cum, Pzt, Sal, Çar
        sonuc = s.ss_bildirim(date(2026, 3, 4), {date(2099, 1, 1)})
        self.assertTrue(sonuc.son_tarih.startswith("2026-03-11"))

    def test_sabit_resmi_tatil_atlanir(self):
        # 2026-04-20 Pazartesi; 23 Nisan Perşembe tatil
        sonuc = s.ss_bildirim(date(2026, 4, 20), {date(2099, 1, 1)})
        self.assertTrue(sonuc.son_tarih.startswith("2026-04-28"))

    def test_verilen_ek_tatil_atlanir(self):
        ek = {date(2026, 3, 5), date(2026, 3, 6)}
        sonuc = s.ss_bildirim(date(2026, 3, 4), ek)
        self.assertTrue(sonuc.son_tarih.startswith("2026-03-13"))

    def test_tatil_verilmezse_uyari(self):
        sonuc = s.ss_bildirim(date(2026, 3, 4), BOS)
        self.assertTrue(any("Dini bayram" in u for u in sonuc.uyarilar))


class IptalDavasi(unittest.TestCase):
    def test_resmi_tatile_rastlayan_son_gun_uzar(self):
        # 2026-03-02 + 60 = 2026-05-01 Cuma, resmî tatil -> 4 Mayıs Pazartesi
        sonuc = s.iptal_davasi(date(2026, 3, 2), {date(2099, 1, 1)})
        self.assertTrue(sonuc.son_tarih.startswith("2026-05-04"))

    def test_hafta_sonu_uzar_hafta_ici_degismez(self):
        # 2026-03-10 + 60 = 2026-05-09 Cumartesi -> 11 Mayıs Pazartesi
        sonuc = s.iptal_davasi(date(2026, 3, 10), {date(2099, 1, 1)})
        self.assertTrue(sonuc.son_tarih.startswith("2026-05-11"))
        # 2026-03-11 + 60 = 2026-05-10 Pazar -> 11 Mayıs; 2026-03-13 + 60 = 12 Mayıs Salı
        sonuc = s.iptal_davasi(date(2026, 3, 13), {date(2099, 1, 1)})
        self.assertTrue(sonuc.son_tarih.startswith("2026-05-12"))

    def test_calismaya_ara_verme_uzamasi(self):
        # 2026-06-10 + 60 = 2026-08-09, ara verme içinde -> 7 Eylül 2026 Pazartesi
        sonuc = s.iptal_davasi(date(2026, 6, 10), {date(2099, 1, 1)})
        self.assertTrue(sonuc.son_tarih.startswith("2026-09-07"))


class DuzSureler(unittest.TestCase):
    def test_komut_satiri_json(self):
        tampon = io.StringIO()
        with contextlib.redirect_stdout(tampon):
            sonuc = s.calistir(["kurul-istem", "--teblig", "2026-04-01", "--json"])
        self.assertTrue(sonuc.son_tarih.startswith("2026-04-16"))
        self.assertIn('"dayanak": "6698 m.15/3"', tampon.getvalue())

    def test_giderim_karari_otuz_gun(self):
        with contextlib.redirect_stdout(io.StringIO()):
            sonuc = s.calistir(["kurul-karar", "--teblig", "2026-04-01"])
        self.assertTrue(sonuc.son_tarih.startswith("2026-05-01"))

    def test_zimni_ret_altmis_gun(self):
        with contextlib.redirect_stdout(io.StringIO()):
            sonuc = s.calistir(["zimni-ret", "--sikayet", "2026-04-01"])
        self.assertTrue(sonuc.son_tarih.startswith("2026-05-31"))

    def test_tatil_parametresi_okunur(self):
        self.assertEqual(s.tatil_listesi("2026-03-20, 2026-03-21", None), {date(2026, 3, 20), date(2026, 3, 21)})


if __name__ == "__main__":
    unittest.main()

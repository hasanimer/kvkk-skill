# Değişiklikler

Sürüm numarası `skills/kvkk/SKILL.md` içindeki `metadata.version` ile aynıdır. Hukuki içerik değişikliklerinde dayanak kaynağı ve doğrulama tarihi yazılır.

## 1.2.0

Yayımlanmadı. Etiket itildiğinde `kvkk.zip` kendiliğinden üretilir.

### Eklenenler
- `references/kanun-ozeti.md`: 6698 sayılı Kanunun yürürlükteki m.4, m.5/2, m.6/3, m.8, m.9, m.10–18 ve m.28 hükümlerinin bent bazında iskeleti. 20.11.2026 tarihinde Mevzuat Bilgi Sistemindeki konsolide metinle karşılaştırıldı.
- `references/acik-riza.md`: rızanın gerekliliği, geçerlilik unsurları, sunum, geri alma, özel durumlar ve rıza metni iskeleti. 2026/347 sayılı İlke Kararı ve ekleri Resmî Gazete nüshasından okundu.
- `references/sablonlar.md`: açık rıza metni yönlendirmesi, İmha Yönetmeliği m.6'ya göre saklama ve imha politikası iskeleti, çerez tercih paneli metni.
- `scripts/sure_hesapla.py`: başvuru cevabı, Kurula şikâyet, ihlal bildirimi, standart sözleşme bildirimi, Kurul istemi ve kararı, zımni ret ve iptal davası süreleri için hesaplayıcı. Testleri `tests/` altında.
- `EVALUATION.md`: dokuz yeni senaryo, tetiklenme denemeleri ve sonuç kayıt tablosu.
- `tools/dogrula.py` ve GitHub Actions: paket yapısı, iç bağlantı ve test denetimi, haftalık dış bağlantı denetimi, etiketle `kvkk.zip` üretimi.

### Değişenler
- `SKILL.md`: `description` açık rıza, çerez, çalışan izleme, idari para cezası, GDPR ve İngilizce sorgular için genişletildi. `license` ve `metadata` eklendi. Okura göre derinlik, yanıt dili, resmî kaynağa erişilemeyen oturum ve süre betiği kuralları eklendi.
- `references/aydinlatma-taslaklari.md`: haklar paragrafı 2026/347 sayılı İlke Kararının Ek-1'indeki kısa biçime çevrildi. Önceki sürüm m.11'in tamamını metne aktarıyordu; Karar bunu gereksiz uzunluk örneği sayıyor.
- Her referans dosyasının başına içerik tarihi eklendi.

## 1.1.1

20.11.2026. Avukatlık bürolarına yönelik örnekler kurgu senaryolarla güncellendi. İlk temas, aday ve referans, bülten, alıcılar ve çerezler için iş akışı korundu.

## 1.0.0

20.11.2026. İlk açık sürüm: `skills/kvkk/` paketi ve `kvkk.zip`; KVKK uyumu, VERBİS, yurt dışı aktarım, Kurul başvuruları, ihlal bildirimi, avukatlık bürosu ve GDPR karşılaştırması iş akışları.

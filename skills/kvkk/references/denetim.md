# KVKK uyum denetimi ve düzeltme planı

## Kapsam ve kanıt toplama

1. İncelenen tüzel kişileri, iş birimlerini, sistemleri, siteleri, dönemi ve tedarikçileri belirle. Grup şirketlerinin veri akışında her tüzel kişinin rolünü ve paylaşımın dayanağını ayrı göster. Kapsam dışı kalan süreçleri belirt.
2. İş biriminden faaliyet örnekleri al. Toplama, kullanım, erişim, paylaşım, aktarım, saklama ve imhayı uçtan uca izle. Sözleşme ve politika ile uygulamadaki ekranı, ayarı ve kayıtları karşılaştır. Gerçek kişi örnekleri yerine maskelenmiş kayıt, yapılandırma özeti veya boş form tercih et. Bir örneğin bütün sistem hakkında neyi gösterdiğini sınırla.
3. Her süreç için şu ayrımları kaydet. **Beyan** süreç sahibinin açıklamasıdır. **Kanıt** görülen doküman veya uygulama kaydıdır. **Bulgu** kanıtla birlikte incelenen uyuşmazlıktır. **Açık konu** sonucu etkileyen eksik bilgidir. Bilinmeyen bir kontrolü uygulanmış veya ihlal edilmiş sayma.

### İstenebilecek kanıtlar

| Süreç | Kanıt örnekleri | Karşılaştırma |
|---|---|---|
| Toplama ve şeffaflık | Veri giriş alanları, aydınlatma sürümleri, sunum tarihi, rıza/geri alma kayıtları | Formun her alanı belirli amaç ve somut dayanakla eşleşiyor mu? Sunum toplama sırasında mı? |
| Güvenlik ve özel nitelikli veri | Rol matrisi, çalışan ayrılış işlemi, erişim incelemesi, çok faktörlü kimlik doğrulama, log ve yedek geri dönüş testleri, 2018/10 tedbir kayıtları | Yetki ve saklama politika ile fiilî ayarlarda uyumlu mu? Yüksek riskli erişim izlenebiliyor mu? |
| Tedarikçi ve aktarım | Sözleşme, işleme eki, alt işleyen listesi, erişim ülkeleri, ağ ve sistem şeması, sözleşme bildirim delili | Aktarım haritası, tedarikçi beyanı, uygulama ve kullanılan güvenceyi doğruluyor mu? |
| Saklama ve imha | Kayıt bazlı süre matrisi, mevzuat dayanağı, imha çizelgesi, olay/uyuşmazlık için geçici saklama kararı | Üretim, yedek, çıktı ve tedarikçi kopyaları aynı plana dâhil mi? |
| Başvuru ve ihlal | Maskelenmiş örnek dosya, olay çizelgesi, teslim kaydı, test/tatbikat | Tetikleyici, sorumlu, süre ve yapılan işlemin delili görülebiliyor mu? |
| VERBİS | Sicil veya istisna değerlendirmesi, dayanak mali yıl, çalışan sayımı, kayıt/bildirim ve güncelleme delili | Envanter ve sicildeki amaç, alıcı, veri grubu, tedbir ve süreler tutarlı mı? |

## Envanter, saklama ve doğrulama örnekleri

- **Envanter modeli.** Süreç kimliği, süreç sahibi, ilgili kişi grubu, veri kategorisi, amaç, hukuki şart ve kanıt, toplama yöntemi, ilgili sistem, erişim rolü, alıcı, ülke ve aktarım güvencesi, saklama dayanağı/başlangıcı/azami süre, imha yöntemi, tedbir, aydınlatma sürümü, son gözden geçirme. Bir alan birden fazla amaçla kullanılıyorsa dayanak ve süre bakımından ayrıştır. Envantere kişilerin bireysel kayıtlarını aktarma. [Kurumun envanter rehberi](https://www.kvkk.gov.tr/Icerik/5445/Kisisel-Veri-Isleme-Envanteri-Hazirlama-Rehberi-Kurum-Internet-Sayfasinda-Yayinlanmistir).
- **İmha.** Silmede ilgili kullanıcıların erişim ve yeniden kullanımının engellenmesini, yok etmede kimsenin erişim, geri getirme ve yeniden kullanım imkânının kalmamasını, anonimleştirmede başka verilerle eşleştirme hâlinde dahi belirlenebilirliğin ortadan kalkmasını değerlendir. Takma ad kullanılmış kayıtların tekrar ilişkilendirilip ilişkilendirilemediğini kontrol et. [İmha Yönetmeliği m.8–10](https://www.kvkk.gov.tr/Icerik/5441/KISISEL-VERILERIN-SILINMESI-YOK-EDILMESI-VEYA-ANONIM-HALE-GETIRILMESI-HAKKINDA-YONETMELIK).
- **İmha takvimi.** Politikası gereken veri sorumlusunda yükümlülüğün doğduğu tarihi izleyen ilk periyodik imhayı ve azami altı aylık periyodu kontrol et. Politika yükümlülüğü bulunmayanda m.11'deki üç aylık kuralı ve Kurulun kısaltma yetkisini teyit et. İmha işlemlerinin kayıtlarını, diğer hukuki yükümlülükler saklı kalmak üzere en az üç yıl saklama kuralını kontrol et. İlgili kişi talebi için ayrıca m.12'yi uygula. [İmha Yönetmeliği m.7, 11–12](https://www.kvkk.gov.tr/Icerik/5441/KISISEL-VERILERIN-SILINMESI-YOK-EDILMESI-VEYA-ANONIM-HALE-GETIRILMESI-HAKKINDA-YONETMELIK).
- **Uygulama teyidi.** Silinen bir kaydın yedekten döndürüldüğünde yeniden görünmesini önleyen işlemi, tedarikçiden gelen imha teyidini ve aktif geçici saklama kararının sona ermesini kontrol et. Yeniden ilişkilendirme mümkünse anonimleştirme sonucunu düzelt.
- **Meşru menfaat kaydı.** Menfaatin meşru, somut ve güncel olduğunu; veri işlemenin bu menfaat için gerekli olduğunu; kişinin makul beklentileri, veri hassasiyeti, olası zarar ve alternatifler karşısında dengenin neden sağlandığını yaz. Kontroller ve tekrar değerlendirme nedenleriyle bitir. Bunu yalnız gerçekten m.5/2(f)'ye dayanan işlem için hazırla.

## Bulgudan kapanışa

Bulgu dili somut olsun. Örnek biçim: `Kapsam | Gözlem | Kanıt ve tarih | Uygulanabilir dayanak | Etki ve olasılık | Öneri | Sorumlu rol | Hedef tarih | Kapanış kanıtı`. Kullanıcı bir risk sınıflandırması istemişse önceliği etkilenebilecek kişilerin zararı, aciliyet, devam eden işleme, özel nitelikli veri ve ölçüm belirsizliğiyle açıkla. Öneriyi mevzuat yükümlülüğü, Kurumun iyi uygulama önerisi veya kurum içi tercihe göre tanımla. Uyum incelemesini yalnız politika metni değişikliğine bağlama. Hatalı ayarın kapandığını veya yeni sürecin çalıştığını gösteren doğrulama ölçütü ekle. [Kurumun veri güvenliği kaynakları](https://www.kvkk.gov.tr/Icerik/2040/Veri-Guvenligine-Iliskin-Yukumlulukler).

## Uyum projesi ve rol bazında eğitim

Proje adımlarını kuruluşun büyüklüğüne ve işlemlerine göre seç. Sicil ekranı, bildirim kanalı, süre ve karar künyesi için güncel Kurum kaynağını aç. Çalışma grubu, komite ve eğitim paketi gibi operasyonel tercihleri ilgili yasal yükümlülükten ayrı değerlendir. [Kurumun uyum süreci duyurusu](https://www.kvkk.gov.tr/Icerik/6554/Kisisel-Verilerin-Korunmasi-Kanunu-Uyum-Surecine-Iliskin-Duyuru).

| Aşama | Uygulama ve teslim ölçütü |
|---|---|
| Başlangıç | Yönetim desteği, süreç sahibi, hukuk ve BT irtibatı, dış sağlayıcılar, kapsam ve tamamlanma ölçütleri. Küçük kuruluşlarda rolleri kişilere ata; hizmet dışarıda yürütülüyorsa sağlayıcıyı kanıt toplamaya dâhil et. |
| Envanter görüşmesi | Boş tabloyla birlikte örnek satır ver. İş biriminden günlük sürecini baştan sona anlatmasını iste. Görüşme sonunda bir gerçek akışı politika, sistem ayarı ve maskeli örnekle karşılaştır. Açık soruyu süreç sahibine bağla. |
| Fark analizi | Aydınlatma ve rıza noktaları, saklama/imha, tedarikçi ve aktarım, erişim ve özel nitelikli veri, başvuru/ihlal ve sicil üzerinden somut farkları kaydet. Hangi metnin düzeleceğini ve hangi ekran, ayar veya iş adımının değişeceğini belirt. |
| VERBİS kontrolü | Sicile başvuru, irtibat kişisi, bildirim ve güncelleme kayıtlarını ayrı kontrol et. Veri kategorisi–kişi grubu–amaç–alıcı eşleşmesini örnek faaliyetlerle sınayarak yurt dışı aktarımı, saklama ve tedbirleri envanterle karşılaştır. Onaylanmış bildirim delilini sakla. [Sicil Yönetmeliği](https://www.kvkk.gov.tr/Icerik/5442/VERI-SORUMLULARI-SICILI-HAKKINDA-YONETMELIK). |
| Eğitim ve uygulama | Yönetim için risk ve karar sahipliği, İK için aday ve sağlık belgesi, müşteri ekibi için müracaat ve aydınlatma, BT için erişim, imha ve ihlal bildirimi senaryosu hazırla. Katılım kanıtı ile senaryoda doğru karar alındığını gösteren cevabı ayrı kaydet. |
| İzleme | İşleme amacı, alıcı, sağlayıcı, ülke veya ürün değişirse envanter ve aydınlatmanın etkilenip etkilenmediğini gözden geçir. Riskli bulguda tarihli kanıtla kapanışı, gerekiyorsa yeni sorumluyu ve yeniden kontrol zamanını kaydet. |

Eğitim talebinde üç kısa alıştırma seç. Örnekler: işten ayrılan personelin erişimi açık kalmış, yalnız mesai için parmak izi kullanılıyor veya sağlayıcı gece bir ifşa bildirmiş. Katılımcıdan önce doğru kişiye haber verme, ölçülü ilk adım ve gerekli kanıtı yazmasını iste. Olayın hukuki sonucunu eğitim içindeki varsayımlara bağla. [Kurumun veri güvenliği rehberi](https://www.kvkk.gov.tr/Icerik/2040/Veri-Guvenligine-Iliskin-Yukumlulukler).

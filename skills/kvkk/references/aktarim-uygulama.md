# Yurt dışına aktarım dosyası ve standart sözleşme bildirimi

Bu modülü standart sözleşme hazırlığı, mevcut aktarımın denetimi, bulut veya yapay zekâ tedariki ve bildirim dosyasının hazırlanmasında aç. Hukuki yolu önce [aktarım karar ağacından](aktarim.md) belirle. Bir sonuca ulaşmak için eksik her olguya bir belge, doğrulayacak kişi ve tarih bağla.

## 1. Veri akışını ve taraf rollerini kanıtla

| Denetim sorusu | Öncelikli kayıt |
|---|---|
| Hangi tüzel kişi aktarıyor, hangi tüzel kişi alıyor? | Sipariş formu, veri işleme sözleşmesi, grup şeması, alt işleyen listesi ve destek ekibinin bağlı olduğu kuruluş |
| Veri nerede saklanıyor, işleniyor veya erişilebilir oluyor? | Üretim ve yedek bölgesi ayarı, destek erişim matrisi ve erişim kayıtları, alt işleyen ülke ve hizmet tablosu |
| Hangi veri, hangi sıklıkla ve hangi amaçla aktarılıyor? | Mimarinin güncel veri akışı, envanter satırı, kaynak ve hedef sistem, örnek alanlar ve saklama ayarları |
| Karşı taraf talimatla mı hareket ediyor, kendi amacını mı belirliyor? | Veri kullanımı, ürün geliştirme, eğitim, telemetri, güvenlik, alt işleme ve silme hükümleriyle fiilî uygulama |

- Aktarım yönünü marka, fatura ülkesi veya sunucu konumundan çıkarmak yerine ayrı alıcı tüzel kişiyi ve fiilî erişimi birlikte belirle. Türkiye'deki sağlayıcının yurt dışındaki alt işleyene veri açması ile Türkiye'deki müşterinin doğrudan yurt dışındaki sağlayıcıya yüklemesi ayrı aktarım senaryolarıdır. Kuruluş içindeki aynı tüzel kişiye ait erişim iddiasında, fiiliyatta ayrı alıcı veya alt işleyen bulunmadığını ve sektörel veri yerelleştirme kurallarını araştır.
- İlgili kişi verisini doğrudan yabancı veri sorumlusuna veriyorsa arada bir veri aktaran bulunup bulunmadığını kontrol et. Yabancı veri sorumlusunun bu veriyi ayrı bir hizmet sağlayıcıya açması sonraki, bağımsız bir akıştır. Kanunun işleme faaliyetine yer bakımından uygulanmasını ayrıca değerlendir.
- Her amaç için rolü yeniden değerlendir. Sağlayıcının müşteri talimatıyla barındırması ile aynı içeriği kendi modeli için kullanması farklı işleme faaliyetleri olabilir. Aynı tedarikçiye tek rol atamadan önce hizmet koşullarını ve ürün ayarlarını karşılaştır.
- Örnek kayıt: `[Akış ID] | [aktaran tüzel kişi/rol] → [alıcı tüzel kişi/rol] | [ülke/erişim] | [amaç ve veri] | [sıklık] | [m.5/m.6 bendi] | [m.9 yolu] | [kanıt ve doğrulama tarihi] | [açık husus / sorumlu]`.

[Aktarım yönetmeliği m.4, 6 ve 7](https://www.resmigazete.gov.tr/eskiler/2024/07/20240710-2.htm) · [Kurumun aktarım rehberi](https://www.kvkk.gov.tr/SharedFolderServer/CMSFiles/13711235-abb6-4b17-9a6b-0a68c1ad86c5.pdf).

## 2. Güvenceyi ve sözleşme eklerini sınamadan imzaya geçme

| Modül | Aktaran → alıcı | Fiilî rol örneği |
|---|---|---|
| SS-1 | Sorumlu → sorumlu | Türkiye'deki rezervasyon aracısı → yabancı otel |
| SS-2 | Sorumlu → işleyen | Türkiye'deki işveren → talimatla barındıran yabancı sağlayıcı |
| SS-3 | İşleyen → işleyen | Türkiye'deki hizmet sağlayıcı → yabancı alt işleyen |
| SS-4 | İşleyen → sorumlu | Türkiye'deki işleyenin hizmet sonucunu yabancı veri sorumlusuna iletmesi |

- Alıcı ülkede ilgili kişinin haklarını kullanabilmesini ve etkili kanun yollarına başvurabilmesini somutlaştır. Uygulanabilir hukuk ve uygulama, ilgili kişi taleplerine cevap, kamu makamı taleplerinin yönetimi, yüksek riskli veri ve sonraki aktarımları incele. Sözleşmeye uyumu engelleyebilecek durumu, kanıtı ve ek tedbirleri yaz. Önemli belirsizlikte kapsamı sınırlama, ek güvence isteme veya ilgili akışı durdurma seçeneğini değerlendir.
- Doğru SS modülünü ve indirme tarihini kaydet. İmzadan önce metni güncel resmî örnekle karşılaştır. Yalnız örneğin izin verdiği seçimlik hükümleri ve ekleri doldur. Ticari ana sözleşmeyi ve AB standart sözleşme maddelerini ayrı incele. Türk standart sözleşmesiyle çelişen talimat, saklama veya erişim hükmünü gider.
- Eklerde veri ve kişi kategorileriyle amaçları ilişkilendir. Sıklığı, saklama ölçütünü veya süresini ve imha yöntemini somutlaştır. Listelenen tedbirleri sistem ayarı, politika veya sözleşme taahhüdüne bağla. Özel nitelikli veri varsa ek tedbirleri göster. İlgili modülde alt işleyen listesini ve izin veya değişiklik düzenini doğrula.
- İmza dosyasını şirketin tam unvanı, temsil belgesindeki imzacı, iki imza tarihi ve imzalı Türkçe metin üzerinden kontrol et. Yabancı dildeki belgelerde noter onaylı Türkçe çeviriyi, yabancı resmî belgelerde geçerli muafiyet, apostil veya konsolosluk tasdiki gereken hâlleri kontrol et. Geçmişe yürürlük tarihi vermeden önceki aktarım dönemini ayrı değerlendir.

[Resmî SS metinleri](https://www.kvkk.gov.tr/Icerik/7929/Standart-Sozlesmeler) · [İmza, belge ve bildirim kontrolü](https://www.kvkk.gov.tr/Icerik/8170/Yurt-Disina-Kisisel-Veri-Aktariminda-Kullanilacak-Standart-Sozlesmelerde-Dikkat-Edilmesi-Gereken-Hususlara-Iliskin-Kamuoyu-Duyurusu).

## 3. Bildirim dosyasını ve ekran sırasını hazırla

1. Dosyaya imzalı sözleşme ve eklerinin tek PDF’ini, imza yetkisi kanıtlarını ve varsa noter onaylı çevirileri al. Son imza tarihini, beş iş günlük son günü ve bildirim yükümlüsünü kaydet. Tereddütte tatil ve çalışılmayan günleri somut takvimde doğrula. Fizikî teslim, KEP ve resmî modül kanallarından seçilen yolun teslim kanıtını belirle.
2. [Standart Sözleşme Bildirim Modülünde](https://standartsozlesme.kvkk.gov.tr/) kuruluş hesabı yetkili kişiyi tanımlar. Yetkili kişi kendi oturumunda temsil ettiği veri sorumlusu veya veri işleyeni seçer, karşı tarafı ekler ve sözleşme kaydını hazırlar. Kimlik numarası, parola ve doğrulama kodu gibi bilgileri kullanıcı kendi resmî oturumunda girer. Sohbette bunları isteme.
3. Karşı taraf kaydında yerleşiklik türüne göre ekranda istenen ülke veya yerel kimlik alanı ile tam unvan, açık adres ve iletişim bilgilerini kontrol et. Sözleşme kaydında aktaran ve alıcı yönünü, her tarafın rolünü, karşı taraf kaydını, imzaların tamamlandığı tarihi ve imzalı tek PDF’yi doğrula. İmza yetkisi kanıtlarını ve uygulanabilir çevirileri ekle. Portalın ek dosya alanında zorunluluk işareti bulunmasa da Yönetmelik m.14/6 belgelerini dosyaya koy.
4. Kılavuzun 14. bölümündeki kaydetme işlemi düzenlenebilir kayıt oluşturur. 17. bölümdeki ayrı gönderme ve onay işlemiyle sözleşme Kuruma iletilir. Hazırlık çıktısına kullanıcı tarafından kontrol edilecek alanları ve ekleri yaz. Yetkili kişi iletimden sonra başarı mesajını, kayıt durumunu veya seçilen kanala ait teslim delilini gönderilen dosya sürümü ve bildirim tarihiyle arşivler. Kurumun incelemesi teslimden sonra başlar.

[Resmî modül kılavuzu](https://standartsozlesme.kvkk.gov.tr/sharedFolder/kullanim-kilavuzu.pdf) · [Bildirim kanalları duyurusu](https://www.kvkk.gov.tr/Icerik/8043/Standart-Sozlesme-Bildirim-Modulu-Hakkinda-Kamuoyu-Duyurusu).

[Portalın aydınlatma metni](https://standartsozlesme.kvkk.gov.tr/sharedFolder/aydinlatma-metni.pdf), Kurumun veri sorumlusu olarak modül giriş ve bildirim süreçlerinde işlediği kişisel verilere ilişkindir. Metin, işleme amacını bildirim yükümlülüğünün yerine getirilebilmesi ve mevzuat uygulamasının izlenmesiyle, hukuki sebebi m.5/2(a) ve m.9/5 ile ilişkilendirir. Bu modül işlemesine ilişkin m.11 talepleri Kuruma yöneltilir. Aktarım tarafları kendi faaliyetleri için m.10 uyarınca olaya uygun aydınlatma hazırlar.

## 4. Değişiklik, sona erme ve kanıt kaydı

- Yeni ülke, uzaktan destek kuruluşu, alt işleyen, grup şirketi, amaç veya veri kategorisini eski eklerle karşılaştır. Taraflar, modül ve aktarım güvencesi değişiyorsa yeni akışın mevcut sözleşmeyle karşılanıp karşılanmadığını belirle. Yeni taraf veya rol için gerekiyorsa yeni modül ve imzaları, yeni akış devreye alınmadan hazırla.
- Sonraki alıcı değiştiğinde imzalanan resmî modülün sonraki aktarımlar maddesini ve ilgili eki aç. SS-2'de 7.8(c) ile 8(a) kapsamında Ek I ve Ek III'ü, seçilmiş izin veya ön bildirim koşullarını ve değişiklik bildirimini kontrol et. SS-2 m.8(b) uyarınca alt işleyene eşdeğer yükümlülükler getiren yazılı sözleşmenin 7.8 koşullarına etkisini incele. Ek standart sözleşme ihtiyacını akışın kendi koşullarına göre belirle. [Resmî SS-2 metni](https://www.kvkk.gov.tr/SharedFolderServer/CMSFiles/b531d656-9cea-4cdb-84ce-1ab92198c9b1.pdf).
- Taraflar veya eklerdeki bilgi ve açıklamalar değiştiğinde ya da sözleşme sona erdiğinde Yönetmelik m.14/8 uyarınca m.14/5'teki bildirim usulünü uygula. Değişiklik veya sona erme tarihini ve beş iş günü takvimini kayda al. Yeni sözleşme varsa son imzasından başlayan bildirim süresini ayrıca izle. İmzalı asıl metin üzerinde geriye dönük değişiklik yapmak yerine ilgili bildirim yolunu ve gerekiyorsa yeni sözleşmeyi kullan.
- Modülde gönderilmiş sözleşmenin ayrıntısından değişiklik veya sonlandırma alanını ve olay tarihini kontrol et. Kılavuza göre değişiklik veya sonlandırmanın gönderilmesi sözleşmeyi yeniden incelemeye iletir. Sonlandırma bir kez bildirilebilir. Ardından o kayıt için değişiklik bildiriminin yolu kapanır. Etkilenen eklerin önceki ve yeni sürümlerini, olayın kanıtını, bildirim tarihini ve teslim delilini sakla. Sona erme sonrasında yeni aktarımın kesilmesini, veri iadesi veya silmeyi ve gerekiyorsa yedeklerin kalan saklama süresini doğrula.

[Aktarım yönetmeliği m.14](https://www.resmigazete.gov.tr/eskiler/2024/07/20240710-2.htm) · [Kurumun aktarım rehberi, s. 59–60](https://www.kvkk.gov.tr/SharedFolderServer/CMSFiles/13711235-abb6-4b17-9a6b-0a68c1ad86c5.pdf) · [Modül kılavuzu, bölüm 18 ve 19](https://standartsozlesme.kvkk.gov.tr/sharedFolder/kullanim-kilavuzu.pdf).

## 5. Bulut ve yapay zekâ tedarikinde ek kontrol

- Girdi, dosya eki, çıktı, arama dizini veya vektör kaydı, telemetri, güvenlik kaydı, destek erişimi ve sonraki aktarımı ayrı sorgula. Model eğitimi kapalıysa bunun hesap ve ürün kapsamını, saklama süresini, insan incelemesini ve istisnaları sözleşme ile ayarlardan doğrula. Veri merkezi bölgesini, destek ile yedek ve alt işleyen ülkelerinden ayrı kaydet.
- Hassas veya müvekkile ait belgede önce işleme ihtiyacını, özel nitelikli veri şartını ve meslek sırrını değerlendir. Maskeli örnekte dosya eki, metadata, nadir olay anlatımı ve başka bilgilerle birleştirildiğinde kimliğin açığa çıkma ihtimalini kontrol et. Yerel veya anonim veriyle yürütülen çalışma seçeneğini değerlendir. Tedarikçinin veri işleme koşulları ile fiilî hesap ayarı uyuşmuyorsa kanıt iste ve öneriyi koşullu yaz.
- Tedarikçi incelemesini sözleşme ve ayar sürümü, somut tespit, gerekli düzeltme ve teyit tarihiyle kapat. Denetim kaydında **doğrulanmış**, **tedarikçi beyanı**, **eksik kanıt** ayrımını koru. Kullanım öncesi kararı, açık kalan riskleri ve değişiklik halinde yeniden değerlendirmeyi üstlenecek kişiyi kaydet.

[Kurumun üretken yapay zekâ rehberi](https://www.kvkk.gov.tr/Icerik/8547/uretken-yapay-zeka-ve-kisisel-verilerin-korunmasi-rehberi-15-soruda) · [Avukatların mesleki faaliyetleri rehberi](https://www.kvkk.gov.tr/Icerik/8990/avukatlarin-mesleki-faaliyetlerinde-kisisel-verilerin-korunmasina-iliskin-uygulama-rehberi-yayimlandi).

# Yerel kişisel veri tespiti ve maskeleme

İçerik tarihi: 2026-11-21.

Bu bölümü çok sayıda Türkçe belgeyi ön elemeden geçirmek, sistemden çıkacak bir metni kontrol etmek veya maskeleme aracını değerlendirmek gerektiğinde aç. Araçların çıktısı inceleme sırası ve aday veri alanları belirlemek için kullanılır. m.5, m.6, m.8 ve m.9 değerlendirmesini işlem, amaç, taraf ve fiilî aktarım üzerinden yap.

| Aday | Kullanım alanı | Kontrol |
|---|---|---|
| `gurgah/kvkk-pii` | Yapılandırılmış tanımlayıcıları metin içinde bulma ve maskeleme. İsteğe bağlı ad/kurum/konum ve hassas veri katmanları var. | Regex ve doğrulama biçimsel işaret verir. README'deki hazır hukuk raporuna dayanak olarak başvurma. Örneğin sağlık verisi için her zaman açık rıza gerektiği iddiası güncel m.6/3 koşullarını yansıtmaz. Yeniden eşleştirilebilen tokenlar takma adlandırmadır. [Proje](https://github.com/gurgah/kvkk-pii). |
| `halilneed/turkish-kvkk-classifier` | Metin veya paragraf içinde hangi veri kategorilerinin olabileceğini işaretleme. Model kartında 14 genel ve 10 özel nitelikli etiket var. | Çok etiketli sınıflandırıcı veri değerini veya konumunu vermez. Model kartı eğitim verisinin sentetik olduğunu açıklıyor. v1.1'in yayımlanan zor setinde özel nitelikli veri duyarlılığı 0,822. Negatif etiketi temizleme kararı için kullanma. [Model kartı](https://huggingface.co/halilneed/turkish-kvkk-classifier). |
| `cesareth/kvkk-denetim` | Metin incelemesine başlarken kullanılabilecek genel kontrol soruları. | Eski yaptırım tablosunu ve sabit öncelik süresini dosyaya uygulama. Kullanıcı puan istiyorsa yöntemi ve ağırlıkları baştan açıkla. Hukukî değerlendirmeyi bu becerinin kaynak akışıyla yürüt. [Yayımlanan beceri](https://github.com/aiskillstore/marketplace/blob/main/skills/cesareth/kvkk-denetim/SKILL.md). |

## Uygulama ve seçim

1. Dosyaları inceleme kapsamına göre seç ve önce yerelde metin çıkar. OCR gereken sayfaları, taranamayan ekleri ve tabloları işaretle. Yol, dosya adı, belge özellikleri, açıklama, yorum, dipnot, görsel ve ek dosyaları aktarım öncesi ayrı kontrol et.
2. Belirli alanları temizlemek için doğrulanabilir desenlerle ve gerekirse varlık tanımayla başla. Kategorileri veya önceliği bulmak için ayrı bir sınıflandırıcı kullan. Uzun belgelerde metni sayfa veya bölüm bazında incele ve model bağlam sınırına takılan yerleri kaydet. İki aracın olumsuz sonucu erişim veya aktarım kararı için tek başına yeterli değildir.
3. Bir araç tercih edilecekse önce kişisel veri içermeyen sentetik veya uygun şekilde anonimleştirilmiş yerel örneklerde dene. Noktalama ve Türkçe karakter, taranmış metin ve OCR hatası, ekler, örtük özel nitelikli veri, benzer ama kişiye ait olmayan ifadeler, uzun belge ve tekrar eden adlar için örnek bulundur. Sonucu yanlış negatif, yanlış pozitif ve biçim bozulması açısından ayrı kaydet.
4. Kapsamı, sürümü, modelleri ve koşulları belgeye bağla. Canlı hizmet veya API çağrısı içeriyorsa girdinin, tanı kayıtlarının ve ağ trafiğinin nereye gittiğini ayrıca doğrula. Paket, model veya örnek kod bağımlılıkları ancak kullanıcı talep ettiğinde ve uygun inceleme sonrasında kurulabilir. Müvekkil verisiyle deneme için ilk tercih yerel ve elle doğrulanmış akıştır.
5. Dışarıya verilecek bir belge için kişi ve kurum adları dışındaki dolaylı tanımlayıcıları, eşleştirme olasılığını, orijinal ve gizli PDF metin katmanlarını ve ekleri insan incelemesinden geçir. Gereken kullanım için ayrı, yeni bir çıktı oluştur. Tersine çevrilebilir eşleştirme tablosunu aynı çıktı veya erişim alanında saklama. [İmha Yönetmeliği m.10](https://www.kvkk.gov.tr/Icerik/5441/KISISEL-VERILERIN-SILINMESI-YOK-EDILMESI-VEYA-ANONIM-HALE-GETIRILMESI-HAKKINDA-YONETMELIK).

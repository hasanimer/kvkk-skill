# KVKK Skill

6698 sayılı Kişisel Verilerin Korunması Kanunu için Türkçe bir [Agent Skill](https://agentskills.io/specification). KVKK uyum denetimi ve belge taslağı, VERBİS, standart sözleşme bildirimi ve bağlayıcı şirket kuralları, ilgili kişi başvurusu, Kurula şikâyet, veri ihlali ve idari dava için kaynaklı çalışma akışları sağlar.

Avukatlık büroları, çalışan denetimi, sağlık, e-ticaret ve yapay zekâ için ayrı uygulama notları içerir. KVKK ve GDPR birlikte gündeme geldiğinde iki rejimin kapsamını, aktarım yollarını ve sürelerini ayrı inceler. Paket Markdown dosyalarından ve yalnız standart kütüphane kullanan isteğe bağlı bir Python süre hesaplayıcısından oluşur. API anahtarı, model kurulumu veya ücretli bağlantı gerektirmez.

Aydınlatma metni hazırlarken [iş akışı](skills/kvkk/references/aydinlatma.md), her faaliyet için veri, amaç, hukuki sebep ve alıcıyı eşleştirir. [Doldurulabilir iskeletler](skills/kvkk/references/aydinlatma-taslaklari.md) ve [yayımlanmış örnekler](skills/kvkk/references/aydinlatma-ornekleri.md) taslak hazırlama ve mevcut metni inceleme için ayrı yollar sağlar.

## Kurulum

| Ortam | Kurulum | Başlatma |
|---|---|---|
| Codex | `skills/kvkk/` klasörünün tamamını `.agents/skills/` veya `~/.agents/skills/` altına kopyala. | `$kvkk` |
| Claude Code | `skills/kvkk/` klasörünün tamamını `.claude/skills/` veya `~/.claude/skills/` altına kopyala. | `/kvkk` |
| OpenCode | `kvkk/` klasörünü `.opencode/skills/` veya `~/.config/opencode/skills/` altına yerleştir. | “`kvkk` becerisini kullan” de. |
| Claude web ve Cowork | [kvkk.zip](https://github.com/hasanimer/kvkk-skill/releases/latest/download/kvkk.zip) dosyasını **Customize → Skills → Create skill → Upload a skill** yoluyla yükle. | Sohbette “KVKK becerisini kullan” de. |

Güncel GitHub CLI ile kullanıcı düzeyinde de kurabilirsin:

```sh
gh skill install hasanimer/kvkk-skill kvkk --agent codex --scope user
gh skill install hasanimer/kvkk-skill kvkk --agent claude-code --scope user
gh skill install hasanimer/kvkk-skill kvkk --agent opencode --scope user
```

OpenCode’da yalnızca bir proje için kurmak istersen aynı komutu proje kökünde `--scope project` ile çalıştır. GitHub CLI bu kurulumda OpenCode’un da taradığı `.agents/skills/` yolunu kullanır. Elle kurulumda ZIP içindeki `kvkk/` klasörünü bütünüyle çıkar. `SKILL.md`, `references/`, `scripts/` ve `LICENSE` aynı `kvkk/` klasöründe olmalı. [OpenCode beceri belgeleri](https://opencode.ai/docs/skills/) · [GitHub CLI kurulum belgeleri](https://cli.github.com/manual/gh_skill_install).

Windows'ta `~` kullanıcı profilini ifade eder. Claude web yüklemesi için yayımlanan `kvkk.zip` dosyasında üst düzey klasör `kvkk/` adını taşır. Özel beceri yükleme, hesabın kod çalıştırma ve dosya oluşturma ayarlarına ve varsa kuruluş politikasına bağlıdır. [Codex belgeleri](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills) · [Claude Code belgeleri](https://code.claude.com/docs/en/skills#choose-where-skills-load) · [Claude web belgeleri](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Örnek istekler

- “Bir kliniğin yurt dışındaki yazılım sağlayıcısı sağlık kayıtlarına uzaktan erişiyor. Veri akışını, aktarım yolunu, standart sözleşme türünü ve eksik kanıtları belirle.”
- “Veri sorumlusu silme talebine 40. günde cevap verdi. Kurula şikâyet süresini değerlendir ve başvuru eklerini listele.”
- “Avukatlık bürosu için aday müvekkil görüşmelerini, tevkil ve dava dosyalarının saklanmasını ele alan bir envanter taslağı oluştur.”
- “İletişim formundaki aydınlatmayı denetle. Formun gönderim koşulunu ve pazarlama seçimini ayır. Eksik alıcıları ve doğrulanmamış aktarım iddialarını tespit et.”

[Beceri giriş dosyası](skills/kvkk/SKILL.md) iş akışlarını yönlendirir. [Değerlendirme senaryoları](EVALUATION.md) süre, dayanak, yetki ve kaynak doğrulamasını sınamak için kullanılabilir. GitHub sorun bildirimlerinde örnekleri sentetik tut ve gerçek kişi bilgileri ile müvekkil belgelerini çıkar.

## Süre hesaplayıcı

Kod çalıştırabilen ortamlarda beceri tarih hesabını [`scripts/sure_hesapla.py`](skills/kvkk/scripts/sure_hesapla.py) ile yapar. Elle de kullanabilirsin:

```sh
python3 skills/kvkk/scripts/sure_hesapla.py sikayet --basvuru 2026-03-02 --cevap-ogrenme 2026-04-11
python3 skills/kvkk/scripts/sure_hesapla.py ihlal --ogrenme "2026-03-06 16:00"
python3 skills/kvkk/scripts/sure_hesapla.py ss-bildirim --son-imza 2026-05-18 --tatil 2026-05-27,2026-05-28,2026-05-29,2026-05-30
```

Sabit tarihli resmî tatiller kendiliğinden sayılır. Dini bayramların tam günlerini `--tatil` ile vermen gerekir. İdari izin günlerini tatil olarak verme; 2429 sayılı Kanunda sayılan tatillerden değildir. Arife yarım gündür; son gün arifeye rastlıyorsa ihtiyatlı tarihi esas al. Çıktı bir hesap yardımıdır; tetikleyici tarihi ve tebliğ anını ayrıca doğrula.

## Bakım

- Her referans dosyasının başındaki içerik tarihi notların ne zaman yazıldığını gösterir. Hukuki içeriği değiştirdiğinde tarihi ve [CHANGELOG](CHANGELOG.md) kaydını güncelle, dayanak kaynağını yaz.
- `python3 tools/dogrula.py` paket yapısını ve iç bağlantıları, `python3 -m unittest discover -s tests` süre hesaplayıcıyı denetler. İkisi de her pull request'te çalışır. Dış bağlantılar haftada bir ayrı bir iş akışıyla denetlenir. GitHub, herkese açık depolarda 60 gün boyunca depo etkinliği olmazsa zamanlanmış iş akışlarını kendiliğinden devre dışı bırakır; depo uzun süre değişmediyse Actions sekmesinden "Dış bağlantı denetimi" iş akışını yeniden etkinleştir veya elle çalıştır.
- Yeni sürüm için `SKILL.md` içindeki `metadata.version` değerini artır, [CHANGELOG](CHANGELOG.md) dosyasına aynı numarayla `## x.y.z` başlığı ekle ve bölüme yayın tarihini yaz. Değişikliği `main` dalına birleştir, Doğrulama iş akışının geçtiğini gör, sonra `main` üzerindeki o commit'e aynı numarayla `v` etiketi koyup it (`git tag v1.2.0 && git push origin v1.2.0`). `kvkk.zip` kendiliğinden üretilir ve yayın, dosyasıyla birlikte iş akışı tarafından oluşturulur. Yayını GitHub arayüzünden yeni bir etiketle elle oluşturma: dosyasız yayın hemen “latest” olur ve iş akışı bitene kadar kurulum bağlantısı 404 döner. Etiketinde `-` bulunan sürümler ön sürüm olarak yayımlanır.
- Hatalı veya eskimiş bir hukuki ifade görürsen resmî kaynağın bağlantısıyla sorun bildirimi aç.

## Kaynaklar ve lisans

Hukuki değerlendirme olay tarihine ve somut olgulara göre yapılır. Süreler, istisnalar ve formlar güncel resmî kaynaklardan doğrulanır. [KVK Kurumu](https://www.kvkk.gov.tr/) · [Mevzuat Bilgi Sistemi](https://www.mevzuat.gov.tr/) · [Resmî Gazete](https://www.resmigazete.gov.tr/)

Depodaki özgün içerik [MIT lisansı](LICENSE) ile paylaşılır. Bağlantısı verilen üçüncü taraf kaynakları kendi koşullarına tabidir.

**English.** Turkish-language Agent Skill for Türkiye’s data protection law. Install the `skills/kvkk/` folder in Codex, Claude Code, or OpenCode. The release ZIP can also be uploaded to Claude. Use official sources to verify each case.

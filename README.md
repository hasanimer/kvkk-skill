# KVKK Skill

6698 sayılı Kişisel Verilerin Korunması Kanunu için Türkçe bir [Agent Skill](https://agentskills.io/specification). KVKK uyum denetimi ve belge taslağı, VERBİS, standart sözleşme bildirimi ve bağlayıcı şirket kuralları, ilgili kişi başvurusu, Kurula şikâyet, veri ihlali ve idari dava için kaynaklı çalışma akışları sağlar.

Avukatlık büroları, çalışan denetimi, sağlık, e-ticaret ve yapay zekâ için ayrı uygulama notları içerir. KVKK ve GDPR birlikte gündeme geldiğinde iki rejimin kapsamını, aktarım yollarını ve sürelerini ayrı inceler. Paket Markdown dosyalarından oluşur. API anahtarı, model kurulumu veya ücretli bağlantı gerektirmez.

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

OpenCode’da yalnızca bir proje için kurmak istersen aynı komutu proje kökünde `--scope project` ile çalıştır. GitHub CLI bu kurulumda OpenCode’un da taradığı `.agents/skills/` yolunu kullanır. Elle kurulumda ZIP içindeki `kvkk/` klasörünü bütünüyle çıkar. `SKILL.md`, `references/` ve `LICENSE` aynı `kvkk/` klasöründe olmalı. [OpenCode beceri belgeleri](https://opencode.ai/docs/skills/) · [GitHub CLI kurulum belgeleri](https://cli.github.com/manual/gh_skill_install).

Windows'ta `~` kullanıcı profilini ifade eder. Claude web yüklemesi için yayımlanan `kvkk.zip` dosyasında üst düzey klasör `kvkk/` adını taşır. Özel beceri yükleme, hesabın kod çalıştırma ve dosya oluşturma ayarlarına ve varsa kuruluş politikasına bağlıdır. [Codex belgeleri](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills) · [Claude Code belgeleri](https://code.claude.com/docs/en/skills#choose-where-skills-load) · [Claude web belgeleri](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Örnek istekler

- “Bir kliniğin yurt dışındaki yazılım sağlayıcısı sağlık kayıtlarına uzaktan erişiyor. Veri akışını, aktarım yolunu, standart sözleşme türünü ve eksik kanıtları belirle.”
- “Veri sorumlusu silme talebine 40. günde cevap verdi. Kurula şikâyet süresini değerlendir ve başvuru eklerini listele.”
- “Avukatlık bürosu için aday müvekkil görüşmelerini, tevkil ve dava dosyalarının saklanmasını ele alan bir envanter taslağı oluştur.”
- “İletişim formundaki aydınlatmayı denetle. Formun gönderim koşulunu ve pazarlama seçimini ayır. Eksik alıcıları ve doğrulanmamış aktarım iddialarını tespit et.”

[Beceri giriş dosyası](skills/kvkk/SKILL.md) iş akışlarını yönlendirir. [Değerlendirme senaryoları](EVALUATION.md) süre, dayanak, yetki ve kaynak doğrulamasını sınamak için kullanılabilir. GitHub sorun bildirimlerinde örnekleri sentetik tut ve gerçek kişi bilgileri ile müvekkil belgelerini çıkar.

## Kaynaklar ve lisans

Hukuki değerlendirme olay tarihine ve somut olgulara göre yapılır. Süreler, istisnalar ve formlar güncel resmî kaynaklardan doğrulanır. [KVK Kurumu](https://www.kvkk.gov.tr/) · [Mevzuat Bilgi Sistemi](https://www.mevzuat.gov.tr/) · [Resmî Gazete](https://www.resmigazete.gov.tr/)

Depodaki özgün içerik [MIT lisansı](LICENSE) ile paylaşılır. Bağlantısı verilen üçüncü taraf kaynakları kendi koşullarına tabidir.

**English.** Turkish-language Agent Skill for Türkiye’s data protection law. Install the `skills/kvkk/` folder in Codex, Claude Code, or OpenCode. The release ZIP can also be uploaded to Claude. Use official sources to verify each case.

Bu beceriyi kullandığınız çalışmalarda [KVKK Skill](https://github.com/hasanimer/kvkk-skill) bağlantısını paylaşarak atıf yapmanızı rica ederiz.

#!/usr/bin/env python3
"""Beceri paketinin yapısal doğrulaması. Yalnız standart kütüphane kullanır.

Kontroller:
  - SKILL.md frontmatter: name klasör adıyla aynı, description 1-1024 karakter,
    metadata.version (1.2.3 biçiminde) ve metadata.icerik-tarihi var. Tırnaksız
    değerlerde ': ', ' #' ve YAML işaretiyle başlayan değer reddedilir; blok
    skaler (> |) desteklenmez.
  - Depodaki Markdown dosyalarında göreli bağlantılar (başlıklı ve <...> biçimli
    olanlar dâhil) var olan dosyaya gidiyor; skills/kvkk altındaki dosyalar beceri
    klasörünün dışına bağlantı vermiyor.
  - references/ altındaki her dosya SKILL.md'den bağlanmış.
  - Her referans dosyasının ilk satırlarında "İçerik tarihi" veya "Son doğrulama" var.
  - CHANGELOG.md, metadata.version için bir başlık içeriyor.

Çalıştırma: python3 tools/dogrula.py
            python3 tools/dogrula.py --surum   (yalnız metadata.version değerini yazar)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parents[1]
BECERI = KOK / "skills" / "kvkk"
BAGLANTI = re.compile(r"\]\(\s*(?:<([^<>\n]*)>|([^)\s<>]+))(?:\s+(?:\"[^\"\n]*\"|'[^'\n]*'))?\s*\)")
BAGLANTI_ACILISI = re.compile(r"\]\(")
AD = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SURUM = re.compile(r"^\d+\.\d+\.\d+$")
# Tırnaksız bir YAML değerini bozan ya da anlamını değiştiren kalıplar.
YAML_RISKI = re.compile(r"""^[>|"'\[\]{}&*!%@`#,]|^[-?:](\s|$)|:\s|:$|\s#""")
TARIH = re.compile(r"^(İçerik tarihi|Son doğrulama): \d{4}-\d{2}-\d{2}\.", re.M)


def yaml_hatasi(ham: str) -> str:
    """Bu ayrıştırıcının gerçek bir YAML yükleyicisinden farklı okuyacağı değeri bildirir."""
    if not ham:
        return ""
    if len(ham) >= 2 and ham.startswith('"') and ham.endswith('"'):
        ic = ham[1:-1]
        return "çift tırnak içinde \" veya \\ kullanılamaz" if '"' in ic or "\\" in ic else ""
    if YAML_RISKI.search(ham):
        return "değer çift tırnak içine alınmalı (': ', ' #' ya da YAML işaretiyle başlayan tırnaksız değer)"
    return ""


def frontmatter(metin: str, hatalar: list[str] | None = None) -> dict[str, str]:
    if not metin.startswith("---\n"):
        return {}
    govde = metin[4:].split("\n---\n", 1)[0]
    alanlar: dict[str, str] = {}
    ust = ""
    for satir in govde.splitlines():
        if not satir.strip():
            continue
        girintili = satir.startswith((" ", "\t"))
        anahtar, _, deger = satir.strip().partition(":")
        deger = deger.strip()
        sorun = yaml_hatasi(deger)
        if sorun and hatalar is not None:
            hatalar.append(f"SKILL.md: frontmatter {anahtar.strip()}: {sorun}")
        deger = deger.strip('"')
        if girintili and ust:
            alanlar[f"{ust}.{anahtar}"] = deger
        else:
            alanlar[anahtar] = deger
            ust = anahtar if not deger else ""
    return alanlar


def main() -> int:
    hatalar: list[str] = []

    skill = BECERI / "SKILL.md"
    skill_metni = skill.read_text(encoding="utf-8")
    alanlar = frontmatter(skill_metni, hatalar)
    if "--surum" in sys.argv[1:]:
        print(alanlar.get("metadata.version", ""))
        return 0
    if not AD.fullmatch(alanlar.get("name", "")) or len(alanlar.get("name", "")) > 64:
        hatalar.append("SKILL.md: name yalnız küçük harf, rakam ve tek tire içermeli, en çok 64 karakter olmalı")
    if alanlar.get("name") != BECERI.name:
        hatalar.append(f"SKILL.md: name {alanlar.get('name')!r}, klasör adı {BECERI.name!r} olmalı")
    aciklama = alanlar.get("description", "")
    if not 1 <= len(aciklama) <= 1024:
        hatalar.append(f"SKILL.md: description {len(aciklama)} karakter, 1-1024 aralığında olmalı")
    if "<" in aciklama or ">" in aciklama:
        hatalar.append("SKILL.md: description içinde < veya > kullanılamaz")
    for anahtar in ("metadata.version", "metadata.icerik-tarihi"):
        if not alanlar.get(anahtar):
            hatalar.append(f"SKILL.md: {anahtar} eksik")
    if alanlar.get("metadata.version") and not SURUM.match(alanlar["metadata.version"]):
        hatalar.append(f"SKILL.md: metadata.version {alanlar['metadata.version']!r}, 1.2.3 biçiminde olmalı")

    for dosya in sorted(KOK.rglob("*.md")):
        if ".git" in dosya.parts:
            continue
        metin = dosya.read_text(encoding="utf-8")
        eslesmeler = list(BAGLANTI.finditer(metin))
        if len(eslesmeler) != len(BAGLANTI_ACILISI.findall(metin)):
            hatalar.append(f"{dosya.relative_to(KOK)}: çözümlenemeyen bağlantı sözdizimi var")
        for eslesme in eslesmeler:
            hedef = eslesme.group(1) if eslesme.group(1) is not None else eslesme.group(2)
            if re.match(r"^[a-z][a-z0-9+.-]*:", hedef) or hedef.startswith("#"):
                continue
            yol = (dosya.parent / hedef.split("#", 1)[0]).resolve()
            if not yol.exists():
                hatalar.append(f"{dosya.relative_to(KOK)}: kırık bağlantı {hedef}")
            elif dosya.is_relative_to(BECERI) and not yol.is_relative_to(BECERI):
                hatalar.append(f"{dosya.relative_to(KOK)}: beceri klasörünün dışına çıkan bağlantı {hedef}")

    for dosya in sorted((BECERI / "references").glob("*.md")):
        if f"references/{dosya.name}" not in skill_metni:
            hatalar.append(f"SKILL.md: references/{dosya.name} bağlanmamış")
        bas = "\n".join(dosya.read_text(encoding="utf-8").splitlines()[:6])
        if not TARIH.search(bas):
            hatalar.append(f"{dosya.relative_to(KOK)}: ilk satırlarda içerik tarihi yok")

    surum = alanlar.get("metadata.version", "")
    degisiklikler = KOK / "CHANGELOG.md"
    if not degisiklikler.exists():
        hatalar.append("CHANGELOG.md yok")
    elif surum and not re.search(rf"^## {re.escape(surum)}[ \t]*$", degisiklikler.read_text(encoding="utf-8"), re.M):
        hatalar.append(f"CHANGELOG.md: '## {surum}' başlığı yok (başlık sürümle birebir aynı olmalı)")

    for hata in hatalar:
        print(f"HATA  {hata}")
    if hatalar:
        return 1
    print(f"Tamam: sürüm {surum}, description {len(aciklama)} karakter, bağlantılar ve tarih satırları geçerli.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

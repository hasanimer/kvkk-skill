#!/usr/bin/env python3
"""Beceri paketinin yapısal doğrulaması. Yalnız standart kütüphane kullanır.

Kontroller:
  - SKILL.md frontmatter: name klasör adıyla aynı, description 1-1024 karakter,
    metadata.version ve metadata.icerik-tarihi var.
  - Depodaki Markdown dosyalarında göreli bağlantılar var olan dosyaya gidiyor.
  - references/ altındaki her dosya SKILL.md'den bağlanmış.
  - Her referans dosyasının ilk satırlarında "İçerik tarihi" veya "Son doğrulama" var.
  - CHANGELOG.md, metadata.version için bir başlık içeriyor.

Çalıştırma: python3 tools/dogrula.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parents[1]
BECERI = KOK / "skills" / "kvkk"
BAGLANTI = re.compile(r"\]\(([^)\s]+)\)")
TARIH = re.compile(r"^(İçerik tarihi|Son doğrulama): \d{4}-\d{2}-\d{2}\.", re.M)


def frontmatter(metin: str) -> dict[str, str]:
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
        deger = deger.strip().strip('"')
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
    alanlar = frontmatter(skill_metni)
    if alanlar.get("name") != BECERI.name:
        hatalar.append(f"SKILL.md: name {alanlar.get('name')!r}, klasör adı {BECERI.name!r} olmalı")
    aciklama = alanlar.get("description", "")
    if not 1 <= len(aciklama) <= 1024:
        hatalar.append(f"SKILL.md: description {len(aciklama)} karakter, 1-1024 aralığında olmalı")
    for anahtar in ("metadata.version", "metadata.icerik-tarihi"):
        if not alanlar.get(anahtar):
            hatalar.append(f"SKILL.md: {anahtar} eksik")

    for dosya in sorted(KOK.rglob("*.md")):
        if ".git" in dosya.parts:
            continue
        for hedef in BAGLANTI.findall(dosya.read_text(encoding="utf-8")):
            if re.match(r"^[a-z][a-z0-9+.-]*:", hedef) or hedef.startswith("#"):
                continue
            yol = (dosya.parent / hedef.split("#", 1)[0]).resolve()
            if not yol.exists():
                hatalar.append(f"{dosya.relative_to(KOK)}: kırık bağlantı {hedef}")

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
    elif surum and f"## {surum}" not in degisiklikler.read_text(encoding="utf-8"):
        hatalar.append(f"CHANGELOG.md: {surum} başlığı yok")

    for hata in hatalar:
        print(f"HATA  {hata}")
    if hatalar:
        return 1
    print(f"Tamam: sürüm {surum}, description {len(aciklama)} karakter, bağlantılar ve tarih satırları geçerli.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

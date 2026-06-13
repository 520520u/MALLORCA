#!/usr/bin/env python3
"""Descarga imágenes reales de Wikimedia → mallorca-guia/images/."""
import time
import urllib.request
from pathlib import Path

from images_data import REMOTE

OUT = Path(__file__).parent / "images"
UA = "MallorcaGuia/1.0 (https://github.com/520520u/MALLORCA; educational)"


def main():
    OUT.mkdir(exist_ok=True)
    ok, fail = 0, []
    for name, url in REMOTE.items():
        dest = OUT / name
        if dest.exists() and dest.stat().st_size > 2000:
            ok += 1
            continue
        print(f"↓ {name}")
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
            if len(data) < 2000:
                raise ValueError(f"muy pequeño ({len(data)} bytes)")
            dest.write_bytes(data)
            ok += 1
        except Exception as e:
            print(f"  ERROR: {e}")
            fail.append(name)
        time.sleep(1.8)
    # miniaturas
    try:
        from PIL import Image
        for f in sorted(OUT.glob("*.jpg")) + sorted(OUT.glob("*.jpeg")):
            thumb = f.with_name(f.stem + "_thumb" + f.suffix)
            if thumb.exists() and thumb.stat().st_size > 500:
                continue
            im = Image.open(f)
            if im.mode in ("RGBA", "P"):
                im = im.convert("RGB")
            im.thumbnail((960, 960), Image.Resampling.LANCZOS)
            im.save(thumb, optimize=True, quality=82)
    except ImportError:
        import subprocess
        for f in OUT.glob("*"):
            if "_thumb" in f.name or f.suffix.lower() not in (".jpg", ".jpeg"):
                continue
            thumb = f.with_name(f.stem + "_thumb" + f.suffix)
            if not thumb.exists() or thumb.stat().st_size < 500:
                subprocess.run(["sips", "-Z", "960", str(f), "--out", str(thumb)], check=False)
    print(f"OK {ok}/{len(REMOTE)} → {OUT}")
    if fail:
        print("FALLARON:", ", ".join(fail))


if __name__ == "__main__":
    main()

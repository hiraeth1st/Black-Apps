from pathlib import Path
import hashlib
root = Path(__file__).parent / "dist"
assert (root / "index.html").is_file()
for apk in (root / "downloads").glob("*.apk"):
    expected = apk.with_suffix(".sha256.txt").read_text().split()[0]
    assert hashlib.sha256(apk.read_bytes()).hexdigest() == expected, apk.name
print("APK integrity verified; static site ready.")

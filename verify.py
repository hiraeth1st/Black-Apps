from pathlib import Path
import hashlib
import json
import urllib.request

project = Path(__file__).resolve().parent
root = project / "dist"
assert (root / "index.html").is_file()

def digest(path):
    checksum = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            checksum.update(chunk)
    return checksum.hexdigest()

for item in json.loads((project / "downloads.json").read_text()):
    name = item["file"]
    assert Path(name).name == name and name.endswith(".apk")
    apk = root / "downloads" / name
    expected = item["sha256"]
    assert apk.with_suffix(".sha256.txt").read_text().split()[0] == expected
    if not apk.exists():
        if "url" not in item:
            raise RuntimeError("Missing bundled APK: " + name)
        assert item["url"].startswith("https://github.com/hiraeth1st/Black-Video/releases/download/")
        temporary = apk.with_suffix(".part")
        try:
            request = urllib.request.Request(item["url"], headers={"User-Agent": "BLACK-Apps-Build"})
            with urllib.request.urlopen(request, timeout=120) as response, temporary.open("wb") as output:
                size = 0
                while chunk := response.read(1024 * 1024):
                    size += len(chunk)
                    if size > item["size"]:
                        raise RuntimeError("Download exceeds expected size: " + name)
                    output.write(chunk)
            if temporary.stat().st_size != item["size"] or digest(temporary) != expected:
                raise RuntimeError("Downloaded APK verification failed: " + name)
            temporary.replace(apk)
        finally:
            temporary.unlink(missing_ok=True)
    if apk.stat().st_size != item["size"] or digest(apk) != expected:
        raise RuntimeError("APK verification failed: " + name)
    print("Verified:", name)
print("All three APKs verified; static site ready.")

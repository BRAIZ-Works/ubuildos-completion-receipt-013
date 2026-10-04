from pathlib import Path
import hashlib,json,re,sys
root=Path(__file__).resolve().parents[1]
req=["index.html","styles.css","app.js","src/data.js","src/onboarding.js","README.md","docs/METHODOLOGY.md","docs/LIMITATIONS.md","docs/PRIVACY.md","docs/SECURITY.md","docs/ACCESSIBILITY.md","PUBLICATION_GATE.md","LINKEDIN_POST.md","PUBLIC_MANIFEST.json","SHA256SUMS.txt"]
missing=[x for x in req if not (root/x).exists()]
assert not missing, missing
text=' '.join((root/x).read_text(errors='ignore') for x in ["index.html","README.md","LINKEDIN_POST.md","docs/LIMITATIONS.md"])
assert "synthetic" in text.lower()
assert "does not claim faster onboarding" in text.lower()
assert "does not claim" in text.lower()
assert "crm integration" in text.lower()
manifest=json.loads((root/'PUBLIC_MANIFEST.json').read_text())
for rel,h in manifest['files'].items(): assert hashlib.sha256((root/rel).read_bytes()).hexdigest()==h,(rel,'hash mismatch')
print(f"PASS: {len(manifest['files'])} manifest-bound files; required public boundaries present")

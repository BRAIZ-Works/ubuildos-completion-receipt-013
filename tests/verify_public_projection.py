from pathlib import Path
import hashlib, json, re
root=Path(__file__).resolve().parents[1]
required=[
 'index.html','styles.css','app.js','src/data.js','src/onboarding.js','README.md','START_HERE.md','HOW_IT_WORKS.md',
 'CLAIMS_AND_LIMITATIONS.md','PROOF.md','ACCESSIBILITY.md','SECURITY_PRIVACY.md','RIGHTS_AND_PROVENANCE.md',
 'RECOVERY_VERSIONING.md','BRAND_BINDING.md','DOCUMENTATION_INDEX.md','LIFECYCLE_STATUS.md','PUBLICATION_GATE.md',
 'PUBLIC_MANIFEST.json','SHA256SUMS.txt'
]
missing=[x for x in required if not (root/x).exists()]
assert not missing, ('required files missing', missing)
text=' '.join((root/x).read_text(errors='ignore') for x in ['README.md','START_HERE.md','CLAIMS_AND_LIMITATIONS.md','SECURITY_PRIVACY.md'])
low=text.lower()
for token in ['synthetic','faster onboarding','crm integration','regulated-data','does not']:
    assert token in low, token
for p in root.glob('*.md'):
    t=p.read_text(errors='ignore')
    assert not re.search(r'\b(TODO|TBD|PLACEHOLDER)\b',t,re.I), p.name
# Documentation index referential-integrity anti-regression.
index=(root/'DOCUMENTATION_INDEX.md').read_text(errors='ignore')
indexed=set(re.findall(r'\|\s*`?([A-Z0-9_./-]+\.(?:md|json|txt))`?\s*\|', index, re.I))
missing_indexed=[x for x in sorted(indexed) if not (root/x).is_file()]
assert not missing_indexed, ('indexed documents missing', missing_indexed)
manifest=json.loads((root/'PUBLIC_MANIFEST.json').read_text())
assert manifest.get('schema')=='UBUILDOS_PUBLIC_MANIFEST_V1'
assert manifest.get('release')=='Day 12 Client Onboarding Tracker public projection v1.2.2'
entries=manifest.get('entries',[])
assert entries, 'empty manifest'
seen=set()
for e in entries:
    rel=e['path']; seen.add(rel)
    p=root/rel
    assert p.is_file(), rel
    assert p.stat().st_size==e['bytes'], (rel,'size mismatch')
    assert hashlib.sha256(p.read_bytes()).hexdigest()==e['sha256'], (rel,'hash mismatch')
actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name not in {'PUBLIC_MANIFEST.json','SHA256SUMS.txt'}}
assert seen==actual, ('population mismatch',sorted(actual-seen),sorted(seen-actual))
# Check checksum population exactly matches manifest-bound files plus manifest.
lines=[ln.strip() for ln in (root/'SHA256SUMS.txt').read_text().splitlines() if ln.strip()]
checksum_paths=set()
for ln in lines:
    sha, rel=ln.split('  ',1)
    p=root/rel
    assert p.is_file(), ('checksum path missing', rel)
    assert hashlib.sha256(p.read_bytes()).hexdigest()==sha, ('checksum mismatch', rel)
    checksum_paths.add(rel)
expected_checksum_paths=actual|{'PUBLIC_MANIFEST.json'}
assert checksum_paths==expected_checksum_paths, ('checksum population mismatch', sorted(expected_checksum_paths-checksum_paths), sorted(checksum_paths-expected_checksum_paths))
print(f'PASS: {len(entries)} manifest-bound files; indexed-document referential integrity PASS; Day-12 v1.2.2 documentation/public boundaries present')

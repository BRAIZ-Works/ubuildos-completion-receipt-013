# Day 12 requirement trace - v1.2.1

- Required steps -> product timeline + tests.
- Blockers -> explicit BLOCKED state + test.
- Owner -> visible owner field; missing owner -> REVIEW + test.
- Completion evidence -> required for COMPLETE + negative test.
- Dependencies -> downstream WAITING until predecessors COMPLETE + negative test.
- Export -> CSV includes visible status/reason/dependencies/blocker/evidence + test.
- Public boundary -> README, claims/limitations, security/privacy, proof, accessibility, rights/provenance.
- Documentation lifecycle -> `LIFECYCLE_STATUS.md` present and manifest-bound.
- Publication authority -> `PUBLICATION_GATE.md` present and manifest-bound; changed successor remains blocked pending Fresh IQA + exact owner authority.
- Documentation index integrity -> verifier requires every indexed document to exist.

# START HERE - Day 12 Client Onboarding Tracker

**Audience:** public reviewer / operator / evaluator  
**Document type:** inspection guide  
**Live build:** https://braiz-works.github.io/ubuildos-completion-receipt-013/

## 60-second inspection

1. Open the live build.
2. Find **Collect access requirements** and confirm it is `BLOCKED` with the visible blocker.
3. Find **Prepare initial workspace** and confirm it remains `WAITING` while its predecessor is incomplete.
4. Compare each step's owner, dependency, blocker, completion evidence, status, and reason.
5. Use **Export visible CSV** and confirm those evaluated fields remain visible in the export.

## State meanings

- `COMPLETE` - required predecessor(s) and required completion evidence are satisfied.
- `BLOCKED` - an active blocker prevents clean progression.
- `WAITING` - a named predecessor is not complete.
- `REVIEW` - ownership/evidence is missing or contradictory, so the workflow refuses to guess.

## Next reading

- [HOW_IT_WORKS.md](HOW_IT_WORKS.md)
- [CLAIMS_AND_LIMITATIONS.md](CLAIMS_AND_LIMITATIONS.md)
- [PROOF.md](PROOF.md)
- [DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md)

All included client records are synthetic demonstration data.

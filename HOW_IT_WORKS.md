# How It Works

**Audience:** public reviewer / workflow designer  
**Document type:** methodology

## Decision model

Each onboarding step carries six public fields:

`owner -> dependency -> blocker -> completion evidence -> status -> reason`

Evaluation is conservative:

1. Missing or contradictory required facts route to `REVIEW`.
2. An active blocker routes to `BLOCKED`.
3. An incomplete required predecessor routes to `WAITING`.
4. A step may be `COMPLETE` only when its required predecessors and required completion evidence are satisfied.
5. Export projects the evaluated state; it does not change the decision logic.

## Why this matters

The workflow makes the reason for state visible. It does not hide handoff logic behind a score or silently convert incomplete work into completion.

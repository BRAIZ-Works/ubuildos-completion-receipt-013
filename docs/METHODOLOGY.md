# Methodology

The tracker evaluates steps in dependency order. Missing owners, contradictory evidence, active blockers, and completion claims without required evidence fail safely. A downstream step can be COMPLETE only when every named predecessor is COMPLETE. Export is a projection of evaluated state and does not mutate it.

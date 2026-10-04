# Recovery and Versioning

**Audience:** maintainer / reviewer  
**Document type:** recovery and change-control guide

The frozen Day-12 product v1.0.0 remains unchanged.

Documentation/distribution defects are repaired through versioned successors. Failed or superseded predecessors remain lineage evidence and are not silently rewritten.

A material documentation/distribution byte change invalidates only the affected proof and requires affected/dependent QA and fresh independent requalification before publication of the changed bytes.

If a public deployment must be rolled back, restore the last known-good public repository state and verify the restored live surface before declaring recovery complete.

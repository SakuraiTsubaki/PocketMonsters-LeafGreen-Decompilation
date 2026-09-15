# Project Status

**Current stage:** Phase 0 — target identity / reproducibility baseline

Initial setup is complete. Metadata-only target inventory tooling and CI are active; no retail target is authoritative until its identity is directly observed.

## Progress

- [x] Establish repository baseline and ROM/key exclusion rules
- [x] Add deterministic metadata-only target inventory tooling
- [x] Add target version inventory and CI
- [ ] Inventory the first verified LeafGreen target
- [ ] Record region/language/revision/hash metadata
- [ ] Document ROM address-space and executable/data layout
- [ ] Map symbols, functions, and major subsystems
- [ ] Document game-data formats and resource containers
- [ ] Begin bounded source reconstruction
- [ ] Add reconstruction matching verification

Machine-readable inventory: `manifests/version-inventory.json`

## Validation levels

- **Unverified** — not independently checked.
- **Observed** — confirmed in a target or extracted data.
- **Reproduced** — recreated with documented steps.
- **Matched** — reconstructed output verified against the intended target.

## Immediate next milestone

Run `tools/inventory_target.py` on the first local LeafGreen target, register exact identity, then begin the address-space map. Retail bytes remain local and read-only.

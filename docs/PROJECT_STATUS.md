# Project Status

**Current stage:** Phase 0 — Target definition (in progress)

This document tracks decompilation progress, target-version coverage, validation level, and the next major milestones.

## Research baseline

This project assumes **no locally owned retail ROM image**. Research and reconstruction therefore begin from public documentation, reverse-engineering repositories, version/hash databases, hardware evidence, and reproducible derived work.

The original Japanese release is the historical comparison baseline. All confirmed regional, language, and revision branches are tracked separately.

## Version inventory

| Target | Region | Language | Revision / update | Verification | Notes |
| --- | --- | --- | --- | --- | --- |
| Pokémon LeafGreen | Japan | Japanese | Rev 0 | Observed | Primary historical baseline; `AGB-BPGJ-0`; full public hash set recorded |
| Pokémon LeafGreen | Japan | Japanese | Rev 1 | Observed | Japanese revision branch; `AGB-BPGJ-1`; SHA-1 recorded |
| Pokémon LeafGreen | North America | English | Rev 0 / Rev 1 | Reproduced upstream / local verification pending | `pret/pokefirered` matching targets |
| Pokémon LeafGreen | Europe English branch | English | Rev 1 | Observed / mapping in progress | `AGB-BPGP-1`; do not invent Rev 0 |
| Pokémon LeafGreen | Other localized branches | German/French/Italian/Spanish | Rev 0 currently observed | Observed / inventory in progress | Product-code/hash matrix seeded in `VERSIONS.md` |

## Progress

- [x] Establish Japanese LeafGreen Rev 0 and Rev 1 baseline identities
- [x] Record Rev 0 physical-dump hash evidence
- [x] Seed first-pass international branch inventory
- [ ] Cross-verify Rev 1 full hash set and physical evidence
- [ ] Reconstruct Japanese Rev 0 ↔ Rev 1 differences
- [ ] Complete market/product-code/hash mapping for every official branch
- [ ] Inventory Japanese source/symbol/data research by subsystem
- [ ] Document executable and section layout
- [ ] Map symbols, functions, and major subsystems
- [ ] Document game-data formats and resource containers
- [ ] Reconstruct scripts, events, and behavior
- [ ] Reconstruct asset pipelines and metadata
- [ ] Add reproducible extraction/repacking tooling
- [ ] Add automated verification where practical

## Validation levels

- **Unverified** — proposed or recorded but not independently checked.
- **Observed** — confirmed directly in a target build, extracted data, authoritative documentation, or stable public identity evidence.
- **Reproduced** — behavior or data can be recreated with documented steps.
- **Matched** — reconstructed output is verified against the intended target.

## Current evidence documents

- [`VERSIONS.md`](VERSIONS.md)
- [`versions/JAPANESE_BASELINE.md`](versions/JAPANESE_BASELINE.md)
- [`RESEARCH_GUIDE.md`](RESEARCH_GUIDE.md)
- [`VERIFICATION.md`](VERIFICATION.md)

## Next milestones

1. Complete LeafGreen's official region/language/revision matrix.
2. Verify Japanese Rev 1 hashes and reconstruct its changes from Rev 0.
3. Separate North-American `BPGE` and European `BPGP` identities cleanly.
4. Inventory Japanese LeafGreen code/data plus Mystery Gift, Wireless Adapter, e-Reader, Sevii Islands, and GameCube-link evidence.
5. Begin executable/data mapping only after target identities are stable.

Update this file whenever the project reaches a meaningful milestone or adds a new supported target.

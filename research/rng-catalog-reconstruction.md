# Pokémon LeafGreen RNG release-catalog reconstruction

The existing Japanese reconstruction remains the origin reference. Six additional SHA-256-gated identities cover English rev0/rev1, German, French, Italian, and Spanish. Every ROM independently matches the adjacent `Random`/`SeedRng` compiler layout and a shared IWRAM state.

All seven identities implement the same ISO-style 32-bit LCG and reuse the verified `src/random.c`; build-specific addresses remain in the reports. Naming and semantics follow `pret/pokefirered@037335f4c725d7c9aecdac87066f2002b4bd7e14`, `src/random.c`. CFGs omit ROM halfwords.

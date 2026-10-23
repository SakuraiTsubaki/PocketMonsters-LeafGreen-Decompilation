# Pokemon LeafGreen WaitForVBlank global reconstruction

The existing Japanese reconstruction remains the origin reference. All 7 cataloged releases (Japanese, English, German, French, Italian, Spanish) clear bit zero of `gMain.intrCheck` at offset `0x1C` before waiting for VBlank. Observed wait modes: volatile-poll.

Per-release evidence records the function range and hash, RAM base, literal locations, call target where present, and a raw-free CFG. The catalog also recalculates the legacy origin map's PC-relative literal locations instead of carrying forward a hand-entered address. No ROM instructions or binaries are published.

Naming and behavior are corroborated by `pret/pokefirered` at `ce6406d8c2eaf46d543c8a2606de0c3cb1951982`, `src/main.c`.

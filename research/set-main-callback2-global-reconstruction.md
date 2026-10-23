# Pokemon LeafGreen SetMainCallback2 global reconstruction

The existing Japanese reconstruction remains the origin reference. All 7 cataloged releases (Japanese, English, German, French, Italian, Spanish) independently prove the same leaf behavior: the argument is stored at `gMain + 0x4`, a release-specific state byte at `gMain + 0x438` is cleared, and the function returns without a call. Observed compiler forms: inline-state-offset.

Per-release maps retain addresses, code-range hashes, RAM addresses, and raw-free control-flow evidence. No ROM instruction bytes are published. Names and behavior are corroborated by `pret/pokefirered` at `ce6406d8c2eaf46d543c8a2606de0c3cb1951982`, `src/main.c`.

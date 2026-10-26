# LeafGreen VBlankIntr reconstruction

The Japanese release `bpg-j-rev0-retail` is the origin reference. All 7 cataloged releases (Japanese, English, German, French, Italian, Spanish) have a VBlank handler immediately after the verified serial callback setter and match the `frlg` control-flow profile. Wireless sync and VCOUNT samples around m4aSoundMain are retained.

Per-release maps preserve code hashes, call targets, validated state addresses and the dependency hash for interrupt initialization. CFG evidence omits raw halfwords and no ROM instruction bytes are published. Naming and behavior are corroborated by `pret/pokefirered` at `037335f4c725d7c9aecdac87066f2002b4bd7e14`, `src/main.c`.

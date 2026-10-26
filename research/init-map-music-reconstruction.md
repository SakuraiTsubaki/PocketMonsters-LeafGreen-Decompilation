# LeafGreen InitMapMusic reconstruction

The Japanese release `bpg-j-rev0-retail` is the origin reference. All 7 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain exactly one verified InitMapMusic routine. It clears the release-specific IWRAM gDisableMusic byte and calls ResetMapMusic. Per-release maps preserve ranges, hashes, call targets and raw-free control flow. No ROM instruction bytes are published. Naming is corroborated by `pret/pokefirered` at `037335f4c725d7c9aecdac87066f2002b4bd7e14`, `src/sound.c`.

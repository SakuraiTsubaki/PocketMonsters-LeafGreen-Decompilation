# LeafGreen interrupt initialization reconstruction

The Japanese release `bpg-j-rev0-retail` is the origin reference. All 7 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain exactly one InitIntrHandlers structure and its callback setters matching the `frlg` profile. VBlank is enabled through EnableInterrupts.

The implementation copies 14 table entries, DMA-copies the 0x800-byte interrupt dispatcher with DMA3 control 0x84000200, installs the IWRAM vector, clears callbacks and enables VBlank. Per-release maps retain code ranges, hashes, validated literals and call targets without ROM instruction bytes. Naming and behavior are corroborated by `pret/pokefirered` at `037335f4c725d7c9aecdac87066f2002b4bd7e14`, `src/main.c`.

# LeafGreen display and serial interrupt reconstruction

The Japanese release `bpg-j-rev0-retail` is the origin reference. All 7 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain exactly one HBlank, VCount and Serial handler matching the `frlg` structural profile. VCount records REG_VCOUNT and invokes m4aSoundVSync without a vcount callback.

Each handler sets both the shared IWRAM interrupt check and gMain.intrCheck with HBlank 0x0002, VCount 0x0004 or Serial 0x0080. Per-release maps retain ranges, code hashes, validated literals and call targets without publishing ROM instruction bytes. Naming and behavior are corroborated by `pret/pokefirered` at `037335f4c725d7c9aecdac87066f2002b4bd7e14`, `src/main.c`.

# LeafGreen GBA entrypoint reconstruction

The Japanese release `bpg-j-rev0-retail` is the origin reference. All 7 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain a verified ARM branch at the GBA entry address. Per-release evidence stores the target and a four-byte range hash without publishing the encoded instruction word. `src/rom_entry.s` preserves the semantic branch using symbols.

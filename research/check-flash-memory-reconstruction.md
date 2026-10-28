# LeafGreen flash-memory detection reconstruction

The Japanese release `bpg-j-rev0-retail` is the origin reference. All 7 cataloged releases (Japanese, English, German, French, Italian, Spanish) preserve the same 38-byte control-flow shape: `IdentifyFlash` returns zero on success, the presence flag is set, and `InitFlashTimer` is called only on that success path. Per-release maps retain addresses, calls and code hashes without ROM bytes or instruction halfwords. `pret/pokefirered` commit `037335f4c725d7c9aecdac87066f2002b4bd7e14`, `src/load_save.c`, is the naming basis.

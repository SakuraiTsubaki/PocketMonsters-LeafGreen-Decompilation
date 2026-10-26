# LeafGreen play-time counter controls reconstruction

The Japanese release `bpg-j-rev0-retail` is the origin reference. All 7 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain one verified Reset/Start/Stop/SetToMax control family using the `pointer` save-storage profile. Start calls the observed SetToMax entry when hours exceed 999.

Per-release maps preserve ranges, hashes, state/save addresses and raw-free control-flow summaries. No ROM instruction bytes are published. Naming and behavior are corroborated by `pret/pokefirered` at `037335f4c725d7c9aecdac87066f2002b4bd7e14`, `src/play_time.c`.

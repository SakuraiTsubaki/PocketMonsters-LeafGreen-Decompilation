# BPGJ rev0 MapMusicMain reconstruction

The verified Japanese ROM implements `MapMusicMain` across `0x080710F0..0x080711D7`. The contiguous 232-byte function range has SHA-256 `406f9909313b41ed7a6aa839437b0f621732367baff958555ad0d3067e28bf65`; only its hash and publication-safe CFG are retained.

The function uses an agbcc-style absolute-word jump table with eight entries. `SakuraiTsubaki/Decompilation` commit `4f687a912ecc40823a17a67fa885768cdca12e98` extends the shared Thumb tracer to resolve this exact compiler pattern without treating the literal pool and table as instructions. The resulting CFG reaches every case and records eight direct calls.

Behavior and names are corroborated by `pret/pokefirered` commit `037335f4c725d7c9aecdac87066f2002b4bd7e14`, `src/sound.c`: state 1 starts the current BGM, state 5 waits for BGM completion, state 6 waits for both BGM and fanfare completion before starting the queued track, and state 7 performs the corresponding fade-in transition. LeafGreen and FireRed share the same Japanese revision-0 function bytes, while their whole-ROM identities remain distinct.

`src/map_music_main.c` is a behavioral reconstruction bound to the ROM CFG, jump-table targets, call order, and code-range hash. No ROM instruction bytes or table words are published.


# BPGJ revision 0 key-input reconstruction

The Japanese LeafGreen `InitKeys` is at `0x080005C0` and `ReadKeys` at
`0x080005E8`. The ROM range has SHA-256
`7d473529a37c87cd9a0236adaa8d6ba1fda7a635bc1165b493b7887ac7846d63`.

The functions preserve key-repeat timing, active-low keypad input, L-to-A
remapping, and the watched-key latch. Save options are reached indirectly
through `gSaveBlock2Ptr` at `0x0300504C`. FireRed and LeafGreen have identical
bytes for this range, but each repository records its own selected ROM identity
and evidence. No raw instruction bytes are published.

# BPGJ revision 0 VBlank interrupt

The Japanese LeafGreen handler at `0x08000724` selects wireless or wired-link
VSync, increments the optional counter through the pointer stored at
`gMain+0x20`, dispatches the VBlank callback, and advances the scalar counter
at `gMain+0x24`. It then flushes buffered GPU and DMA3 work and mirrors the
sound engine's PCM DMA counter.

This retail revision records `REG_VCOUNT` immediately before and after
`m4aSoundMain`; both byte stores are present in the ROM and are retained here.
Link-battle receive, RNG, wireless-indicator update, and both VBlank
acknowledgments follow. The analysis map records the exact Japanese call
targets, globals, structure offsets, and range hash without publishing ROM
instruction bytes.


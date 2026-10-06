# BPGJ revision 0 display and serial interrupts

The Japanese LeafGreen ROM places `HBlankIntr`, `VCountIntr`, and `SerialIntr`
after the VBlank handler. HBlank and serial conditionally dispatch their
respective `gMain` callbacks before acknowledging the interrupt in both the
BIOS check word and `gMain.intrCheck`.

VCount records the current scanline byte at `0x03003DC0`, calls this build's
`m4aSoundVSync`, and performs the same dual acknowledgment. The map preserves
the exact function boundaries, game-specific call targets, literals, flags,
and combined range hash without publishing ROM instruction bytes.


# BPGJ revision 0 interrupt initialization

The Japanese LeafGreen build copies 14 handlers and the 0x800-byte
`IntrMain` buffer, installs the IWRAM interrupt vector, clears three callback
slots, sets `REG_IME`, and enables VBlank through `EnableInterrupts`.

Its interrupt template is `0x081CDE24`. This differs between FireRed and
LeafGreen, so the ROM range hash and map remain game-specific even though the
reconstructed behavior is shared. No raw ROM instructions are published.

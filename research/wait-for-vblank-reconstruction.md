# WaitForVBlank reconstruction

Target: BPGJ-rev0 (2957b392dc09fc8df45a660af5493368d7bd378d299862f4cc115998e9da0bf2)

The already verified Japanese `AgbMain` map calls `WaitForVBlank` at 0x08000890. A fresh conservative Thumb trace terminates at 0x080008B8, observes a return, and is published without instruction halfwords. The code-only ROM range SHA-256 is `a76d461ef38542e453f177d865ed0be60c4cbca398e3ff02657adee9bcbb520a`; no ROM bytes are stored.

The function clears bit 0 of `gMain.intrCheck` at the proven offset `0x1C` before waiting. This build polls the volatile flag until the VBlank interrupt handler sets it. The corresponding `VBlankIntr` reconstruction independently shows that the handler sets the same flag, closing the producer/consumer relationship.

Names were aligned with [pret/pokefirered](https://github.com/pret/pokefirered) at commit `037335f4c725d7c9aecdac87066f2002b4bd7e14`, then checked against this ROM's addresses, control flow, literals, and state accesses. The upstream project is a naming reference, not a substitute for the local ROM evidence.


# DoSoftReset reconstruction

Target: BPGJ-rev0 (2957b392dc09fc8df45a660af5493368d7bd378d299862f4cc115998e9da0bf2)

The verified Japanese `AgbMain` map calls `DoSoftReset` at 0x080008D8. A fresh Thumb trace closes at 0x08000930, observes a return, and is published without instruction halfwords. The code-only range SHA-256 is `dbe54fad672a911a2b27b6a13903f252386a5c2a16811c1150820295cfa3447a`; no ROM bytes are stored.

The straight-line routine disables the interrupt master switch, stops sound VSync and the scanline effect, then disables DMA channels 1, 2, and 3 through their control-high registers. This FireRed/LeafGreen-family build has no RTC-protection call and passes `0xDF`, excluding the SIO-register reset bit.

Names were aligned with [pret/pokefirered](https://github.com/pret/pokefirered) at commit `037335f4c725d7c9aecdac87066f2002b4bd7e14`, then independently checked against this ROM's function boundary, direct-call targets, hardware addresses, and constants.


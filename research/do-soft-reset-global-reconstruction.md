# Pokemon LeafGreen DoSoftReset global reconstruction

The existing Japanese reconstruction remains the origin reference. All 7 cataloged releases (Japanese, English, German, French, Italian, Spanish) disable IME, stop sound VSync and the scanline effect, disable DMA channels 1 through 3, and invoke SoftReset. Observed variants: no-rtc-preserve-sio.

RTC-family builds call `SiiRtcProtect` and reset with mask `0xFF`; FireRed/LeafGreen builds omit RTC protection and preserve SIO registers with mask `0xDF`. Per-release maps retain ranges, hashes, ordered call targets, hardware writes, and raw-free CFGs. No ROM instructions or binaries are published.

Naming and behavior are corroborated by `pret/pokefirered` at `ce6406d8c2eaf46d543c8a2606de0c3cb1951982`, `src/main.c`.

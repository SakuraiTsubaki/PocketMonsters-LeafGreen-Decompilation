# LeafGreen ArcTan2 and CpuSet BIOS stub reconstruction

bpg-j-rev0-retail is the Japanese origin reference. All 7 builds (Japanese, English, German, French, Italian, Spanish) verify ArcTan2 SWI 0x0A and CpuSet SWI 0x0B at SDK-layout offsets from the LZ77 VRAM wrapper, including Ruby debug. CpuSet has duplicate signatures in 7 build(s), so only the candidate at the verified -4/-8 position is selected. Pinned libagbsyscall sources corroborate symbols and calling conventions. No ROM bytes are published.

# BPGJ rev0 RNG reconstruction

The verified Japanese ROM reaches `Random` at `0x0804448C` from `VBlankIntr`; `SeedRng` begins at `0x080444AC`. Publication-safe CFGs close both straight-line Thumb functions at one return with no calls.

Literal and instruction-shape validation proves the 32-bit recurrence `state = 1103515245 * state + 24691`, returning bits 31..16. Both routines address `gRngValue` at `0x03005040`; their function-range hashes match the equivalent Ruby, Sapphire, and FireRed routines despite relocation.

Names and semantics are corroborated by pinned primary source `pret/pokefirered@037335f4c725d7c9aecdac87066f2002b4bd7e14`, `src/random.c`. No ROM instruction bytes are published.

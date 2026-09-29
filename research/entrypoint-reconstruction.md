# Japanese ROM entrypoint reconstruction

The selected Japanese target begins with ARM word `0xea00007f`, branching from `0x08000000` to `0x08000204` under ARM PC+8 semantics. The checked-in assembly preserves the exact entry word and the evidence remains gated by the selected target SHA-256. No ROM binary is stored.

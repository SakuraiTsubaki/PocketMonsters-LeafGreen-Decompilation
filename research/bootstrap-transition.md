# Bootstrap ARM-to-Thumb transition

The Japanese target follows twelve ARM words from `0x08000204` to `bx r1` at `0x08000230`. Literal `0x080003a5` at `0x08000244` proves the next executed code is Thumb at `0x080003a4`.

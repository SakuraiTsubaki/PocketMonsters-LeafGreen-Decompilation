# LeafGreen key input reconstruction

The Japanese release `bpg-j-rev0-retail` is the origin reference. All 7 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain exactly one InitKeys and ReadKeys pair matching the `pointer` profile. Options are read through the gSaveBlock2Ptr indirection.

The pair establishes repeat delays 5 and 40, derives active-high keys from REG_KEYINPUT with mask 0x03FF, implements repeat behavior, applies L-equals-A mode, and records watched-key presses. Per-release maps retain ranges, hashes, validated literals and control-flow counts without ROM instruction bytes. Naming and behavior are corroborated by `pret/pokefirered` at `037335f4c725d7c9aecdac87066f2002b4bd7e14`, `src/main.c`.

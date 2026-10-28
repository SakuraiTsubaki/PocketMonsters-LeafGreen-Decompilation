# LeafGreen InitFlashTimer reconstruction

`bpg-j-rev0-retail` is the Japanese origin reference. All 7 cataloged releases (Japanese, English, German, French, Italian, Spanish) preserve the `frlg` profile: timer 2 is bound to interrupt-table slot 7 through `SetFlashTimerIntr`. Per-release maps retain calls and hashes without ROM bytes or instruction halfwords.

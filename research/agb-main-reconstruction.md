# BPGJ revision 0 `AgbMain` reconstruction

The verified Japanese LeafGreen CFG covers the non-returning function at
`0x080003A4..0x080004AB`, with 29 direct calls and a back edge from
`0x080004AA` to the frame loop at `0x0800041A`.

The call sequence and state accesses match `pret/pokefirered` `src/main.c` at
commit `037335f4c725d7c9aecdac87066f2002b4bd7e14`. Unlike Ruby/Sapphire, this
loop initializes GPU state, RFU, DMA requests, backgrounds, heap and fonts; it
also stops RFU before soft reset and clears sprite-copy requests on the receive
path. These differences are preserved in a separate LeafGreen implementation.

BPGJ revision 0 writes white to the first background palette entry and executes
both `rfu_REQ_stopMode` and `rfu_waitREQComplete`. The revision-dependent flash
failure callback gate present in later builds is not inserted here because it
is absent from this verified Japanese rev0 CFG. No ROM instruction bytes are
published.



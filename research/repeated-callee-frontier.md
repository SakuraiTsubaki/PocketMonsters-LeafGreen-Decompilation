# Repeated bootstrap callee frontier

The BPGJ revision 0 bootstrap calls `0x080004b0` three times. A publication-safe
Thumb trace reaches the return at `0x08000552`, covers 82 instruction positions,
records seven direct call sites and twelve branch edges, and omits raw ROM
halfwords. This is the next behavior-reconstruction frontier.

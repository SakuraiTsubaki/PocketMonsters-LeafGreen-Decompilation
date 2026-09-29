# Thumb entry reachable control flow

Exact-hash analysis starts at the proven Thumb target `0x080003a4`. Conservative traversal reaches 116 halfwords across `0x080003a4`–`0x080004ac`, records 12 direct edges and 29 BL calls, and does not follow callees. No return is reachable in this graph; this is evidence for a non-returning bootstrap path, not a claimed complete function boundary. The scan ceiling is `0x080043a4`.


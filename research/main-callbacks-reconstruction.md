# Main callback reconstruction

The existing BPGJ revision-zero callback reconstruction is now tied to four exact ROM ranges. It covers link handling, save/quest-log initialization, guarded callback dispatch through the save-failure and help systems, and callback2/state assignment. Names follow `pret/pokefirered`; addresses, offsets, and hashes come from the verified Japanese ROM.

The C source and map contain no verbatim ROM byte extracts. LeafGreen and FireRed retain separate evidence for their differing callback body.

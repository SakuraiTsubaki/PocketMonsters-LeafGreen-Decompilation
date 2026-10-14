# BPGJ-rev0 trainer-ID helper reconstruction

The verified Japanese ROM contains the following four-byte trainer-ID helpers:

- `SetTrainerId`: `0x080541C0..0x080541D0`, SHA-256 `b219139d5a72a06b84b59c718f14ddff68a10a2a3e7c77994251bbc8cd5ca40b`.
- `CopyTrainerId`: `0x080541D0..0x080541EC`, SHA-256 `e2ede032f2797356414ff7d8a4c5803c4350847c7d86acc47bf4ba92bb5e75e5`.

The setters serialize a 32-bit value in little-endian order. Copy helpers move exactly four bytes; the Emerald-specific getter reconstructs the same little-endian value. Every function has one observed return, and none calls another routine.

Names and behavior are corroborated by `pret/pokefirered` commit `037335f4c725d7c9aecdac87066f2002b4bd7e14`, `src/new_game.c`. The ROM digests and publication-safe CFGs are authoritative here. No ROM instruction bytes are published.

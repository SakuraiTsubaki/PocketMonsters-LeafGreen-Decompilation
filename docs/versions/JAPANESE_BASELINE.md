# Japanese Baseline — Pokémon LeafGreen

This document records the current evidence for the Japanese releases that serve as the historical baseline for the LeafGreen decompilation project.

## Baseline rule

The Japanese release is the comparison origin for regional research. Later regional builds remain separate branches whenever localization, code, data, assets, events, fixes, product identity, or distribution context differs.

No retail ROM image is required or committed. Identity and reconstruction work begins from public documentation, public reverse-engineering repositories, hardware evidence, hashes, and reproducible analysis.

## Confirmed identity

| Field | Rev 0 | Rev 1 |
| --- | --- | --- |
| Title | ポケットモンスター リーフグリーン | ポケットモンスター リーフグリーン |
| Platform | Game Boy Advance | Game Boy Advance |
| Market | Japan | Japan |
| Language | Japanese | Japanese |
| Product/build identifier | AGB-BPGJ-0 | AGB-BPGJ-1 |
| Retail product code | AGB-BPGJ-JPN | revision branch of AGB-BPGJ-JPN |
| SHA-1 | `5946f1b59e8d71cc61249661464d864185c92a5f` | `de9d5a844f9bfb63a4448cccd4a2d186ecf455c3` |
| Repository role | Primary historical baseline | Japanese revision branch |

For Rev 0, public physical-dump evidence also records:

- CRC32: `0A48556B`
- MD5: `138a71a5be83f3f3d7af3d31916a5fc7`
- SHA-256: `2957b392dc09fc8df45a660af5493368d7bd378d299862f4cc115998e9da0bf2`

## Official release context

The Pokémon Company official Japanese product page records FireRed and LeafGreen as Game Boy Advance titles released in Japan on **2004-01-29**. It also documents Wireless Adapter support and communication/linkage with other Generation III titles.

Official sources:

- https://www.pokemon.co.jp/game/gba/fl/
- https://www.pokemon.co.jp/game/gba/fl/equipment.html

## Physical-cartridge and revision evidence

The Game Boy hardware database records separate Japanese LeafGreen variant identities:

- `AGB-BPGJ-0` — Pocket Monsters - LeafGreen (Japan)
- `AGB-BPGJ-1` — Pocket Monsters - LeafGreen (Japan) (Rev 1)

A public physical Rev 0 dump report records the full hash set listed above.

Sources:

- https://gbhwdb.gekkio.fi/cartridges/AGB-BPGJ-0/
- https://gbhwdb.gekkio.fi/cartridges/AGB-BPGJ-0/fexcollects-1.html

## Rev 1 hash evidence

The Rev 1 SHA-1 currently recorded is:

- `de9d5a844f9bfb63a4448cccd4a2d186ecf455c3`

Public hash reference:

- https://github.com/40Cakes/pokebot-gen3/blob/main/modules/roms.py

The exact Japanese Rev 0 ↔ Rev 1 code/data delta has not yet been reproduced in this repository.

## Public reconstruction coverage gap

`pret/pokefirered` explicitly targets **English Pokémon FireRed and LeafGreen**. It records English LeafGreen Rev 0 / Rev 1 matching targets, making it a major structural/source reference but not a matching Japanese reconstruction.

Japanese-specific scripts, text, graphics, audio, events, wireless behavior, e-Reader-related differences, region checks, and revision changes must be investigated separately.

Source:

- https://github.com/pret/pokefirered

## Evidence classification

| Finding | Level | Reason |
| --- | --- | --- |
| Japanese release date 2004-01-29 | Observed | Official Japanese Pokémon site |
| `AGB-BPGJ-0` / `AGB-BPGJ-1` existence | Observed | Public cartridge database |
| Rev 0 full hash set | Observed | Direct physical-dump report |
| Rev 1 SHA-1 | Observed / public hash inventory | Independent public ROM-identification tooling |
| Exact Rev 0 ↔ Rev 1 differences | Unverified in repository | Must be reconstructed from public evidence |
| Japanese matching decompilation | Not yet reproduced | Public `pret/pokefirered` target is English |

## Next tasks

1. Cross-check Rev 1 CRC32/MD5/SHA-256 and physical-cartridge evidence.
2. Reconstruct exact Japanese Rev 0 ↔ Rev 1 differences.
3. Inventory Japanese LeafGreen source, symbols, maps, scripts, text, graphics, audio, save, wireless, e-Reader, events, and GameCube-link research.
4. Compare against public English `pret/pokefirered` without assuming byte identity.
5. Track Sevii Islands, National Dex unlocking, Mystery Gift, Wireless Adapter, and Colosseum linkage as region/revision-sensitive subsystems.

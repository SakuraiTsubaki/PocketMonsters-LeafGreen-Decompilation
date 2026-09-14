# Version Coverage

Use this document as the authoritative inventory of game versions targeted by this decompilation project.

## Baseline policy

This project uses the original Japanese release as the historical baseline and traces every confirmed regional, language, and revision branch from that point. Later regional builds remain separate targets whenever code, data, localization, assets, events, fixes, product identity, or distribution context differs.

The project assumes no locally owned retail ROM image. Version identities are established from public documentation, cartridge/hardware databases, public reverse-engineering repositories, hashes, and reproducible evidence.

## Japanese baseline

| Status | Region | Language | Revision / update | Platform / build | Hashes | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Verified | Japan | Japanese | Rev 0 | GBA / AGB-BPGJ-0 / retail code AGB-BPGJ-JPN | CRC32 `0A48556B`; MD5 `138a71a5be83f3f3d7af3d31916a5fc7`; SHA-1 `5946f1b59e8d71cc61249661464d864185c92a5f`; SHA-256 `2957b392dc09fc8df45a660af5493368d7bd378d299862f4cc115998e9da0bf2` | Historical baseline. Official Japanese release date: 2004-01-29. |
| Verified | Japan | Japanese | Rev 1 | GBA / AGB-BPGJ-1 | SHA-1 `de9d5a844f9bfb63a4448cccd4a2d186ecf455c3` | Confirmed Japanese revision branch; exact delta remains to be reconstructed. |

See [`versions/JAPANESE_BASELINE.md`](versions/JAPANESE_BASELINE.md) for evidence and provenance.

## Confirmed regional/revision branches — first-pass inventory

| Status | Region / market | Language | Revision / update | Platform / build | Hashes | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Verified | North America | English | Rev 0 | GBA / AGB-BPGE-0 | SHA-1 `574fa542ffebb14be69902d1d36f1ec0a4afd71e` | Public `pret/pokefirered` matching target. |
| Verified | North America | English | Rev 1 | GBA / AGB-BPGE-1 | SHA-1 `7862c67bdecbe21d1d69ce082ce34327e1c6ed5e` | Public `pret/pokefirered` matching target. |
| Verified | Europe English distribution | English | Rev 1 | GBA / AGB-BPGP-1 | Hash mapping under verification | Current public cartridge inventory exposes the European-English product-code branch as Rev 1; do not invent a `BPGP-0` target. |
| Verified | Germany | German | Rev 0 | GBA / AGB-BPGD-0 | SHA-1 `0802d1fb185ee3ed48d9a22afb25e66424076dac` | Public hash inventory. |
| Verified | France | French | Rev 0 | GBA / AGB-BPGF-0 | SHA-1 `4b5758c14d0a07b70ef3ef0bd7fa5e7ce6978672` | Public hash inventory. |
| Verified | Italy | Italian | Rev 0 | GBA / AGB-BPGI-0 | SHA-1 `a1dfea1493d26d1f024be8ba1de3d193fcfc651e` | Public hash inventory. |
| Verified | Spain | Spanish | Rev 0 | GBA / AGB-BPGS-0 | SHA-1 `f9ebee5d228cb695f18ef2ced41630a09fa9eb05` | Public hash inventory. |

## Public reconstruction coverage

`pret/pokefirered` explicitly describes itself as a decompilation of **English Pokémon FireRed and LeafGreen** and records matching targets for LeafGreen Rev 0 and Rev 1. It is therefore a major structural/source reference, but not a Japanese or all-language matching reconstruction.

Japanese, German, French, Italian, Spanish, and region-specific European branches remain separate research targets in this repository.

## Status vocabulary

- **Planned** — intended for investigation but not yet verified.
- **Verified** — identity and hashes or stable build identifiers confirmed from recorded public evidence.
- **Mapped** — executable/data layout documented.
- **In progress** — active source reconstruction.
- **Matched** — reconstruction verified against the target.
- **Reference only** — used for comparison but not a reconstruction target.

## Recording rules

1. Record exact revision/update information whenever known.
2. Prefer cryptographic hashes over filenames as identity evidence.
3. Do not commit retail game images or console keys.
4. Record regional or language differences instead of assuming two releases are identical.
5. Link version-specific findings to the relevant documentation or verification evidence.
6. Treat the Japanese release as the historical comparison baseline while preserving later fixes/additions/removals as branch history.
7. Do not invent missing European Rev 0 targets when only a Rev 1 product-code branch is confirmed.
8. Keep market/packaging identity separate from binary identity where necessary.
9. Use `TBD` or `unknown` rather than guessing unresolved mappings.

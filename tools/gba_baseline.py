#!/usr/bin/env python3
"""Generate a reproducible first-pass binary map for a local GBA ROM."""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import struct

GBA_ROM_BASE = 0x08000000
GBA_ROM_END = 0x0A000000


def digest(data: bytes, name: str) -> str:
    h = hashlib.new(name); h.update(data); return h.hexdigest()


def ascii_field(raw: bytes) -> str:
    return raw.rstrip(b"\0").decode("ascii", errors="replace")


def gba_header(data: bytes) -> dict[str, object]:
    if len(data) < 0xC0: raise ValueError("file is too small to contain a complete GBA header")
    computed = (-(sum(data[0xA0:0xBD]) + 0x19)) & 0xFF; stored = data[0xBD]
    return {"title": ascii_field(data[0xA0:0xAC]), "game_code": ascii_field(data[0xAC:0xB0]), "maker_code": ascii_field(data[0xB0:0xB2]), "fixed_value": data[0xB2], "main_unit_code": data[0xB3], "device_type": data[0xB4], "revision": data[0xBC], "header_checksum": stored, "computed_header_checksum": computed, "header_checksum_valid": stored == computed}


def decode_entry_branch(data: bytes) -> dict[str, object] | None:
    if len(data) < 4: return None
    instr = struct.unpack_from("<I", data, 0)[0]
    if (instr & 0x0F000000) != 0x0A000000: return {"instruction": f"0x{instr:08X}", "kind": "not_arm_branch"}
    imm24 = instr & 0x00FFFFFF
    if imm24 & 0x00800000: imm24 -= 0x01000000
    target = 8 + (imm24 << 2)
    return {"instruction": f"0x{instr:08X}", "kind": "arm_branch", "target_offset": target, "target_address": f"0x{GBA_ROM_BASE + target:08X}"}


def block_hashes(data: bytes, block_size: int) -> list[dict[str, object]]:
    return [{"offset": o, "size": len(data[o:o + block_size]), "sha256": digest(data[o:o + block_size], "sha256")} for o in range(0, len(data), block_size)]


def scan_rom_pointers(data: bytes, sample_limit: int) -> dict[str, object]:
    refs=[]; targets=Counter(); total=0
    for source in range(0, len(data)-3, 4):
        value=struct.unpack_from("<I", data, source)[0]
        if not (GBA_ROM_BASE <= value < GBA_ROM_END): continue
        target=value-GBA_ROM_BASE
        if target >= len(data): continue
        total += 1; targets[target >> 16] += 1
        if len(refs) < sample_limit: refs.append({"source_offset": source, "value": f"0x{value:08X}", "target_offset": target})
    return {"aligned_pointer_count": total, "sample_limit": sample_limit, "sample": refs, "target_64k_blocks": [{"block": b, "offset": b << 16, "references": c} for b,c in sorted(targets.items())]}


def scan_thumb_returns(data: bytes, sample_limit: int) -> dict[str, object]:
    hits=[]; total=0
    for o in range(0, len(data)-1, 2):
        if data[o:o+2] == b"\x70\x47":
            total += 1
            if len(hits) < sample_limit: hits.append(o)
    return {"bx_lr_halfword_count": total, "sample_limit": sample_limit, "sample_offsets": hits, "warning": "heuristic signature; data may contain false positives"}


def build_report(path: Path, block_size: int, sample_limit: int) -> dict[str, object]:
    data=path.read_bytes()
    return {"schema_version": 1, "source": {"filename": path.name, "size": len(data), "sha1": digest(data,"sha1"), "sha256": digest(data,"sha256")}, "header": gba_header(data), "entrypoint": decode_entry_branch(data), "blocks": {"block_size": block_size, "hashes": block_hashes(data, block_size)}, "rom_pointers": scan_rom_pointers(data, sample_limit), "thumb_signatures": scan_thumb_returns(data, sample_limit)}


def main() -> int:
    p=argparse.ArgumentParser(description="Generate a first-pass GBA ROM decompilation baseline")
    p.add_argument("rom", type=Path); p.add_argument("--block-size", type=lambda x:int(x,0), default=0x10000); p.add_argument("--sample-limit", type=int, default=4096); p.add_argument("--out", type=Path); a=p.parse_args()
    if not a.rom.is_file(): p.error(f"ROM not found: {a.rom}")
    if a.block_size <= 0: p.error("--block-size must be positive")
    if a.sample_limit < 0: p.error("--sample-limit must be non-negative")
    try: report=build_report(a.rom,a.block_size,a.sample_limit)
    except ValueError as exc: p.error(str(exc))
    rendered=json.dumps(report,indent=2,ensure_ascii=False)+"\n"
    if a.out: a.out.parent.mkdir(parents=True,exist_ok=True); a.out.write_text(rendered,encoding="utf-8")
    else: print(rendered,end="")
    return 0

if __name__ == "__main__": raise SystemExit(main())

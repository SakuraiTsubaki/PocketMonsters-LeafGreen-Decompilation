#!/usr/bin/env python3
"""Create a metadata-only inventory for a locally supplied target build."""
from __future__ import annotations
import argparse, hashlib, json
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
SENSITIVE_FILENAMES={"prod.keys","title.keys"}; SENSITIVE_SUFFIXES={".keys"}; CHUNK_SIZE=1024*1024

def sha256_file(path:Path)->str:
    d=hashlib.sha256()
    with path.open("rb") as h:
        for chunk in iter(lambda:h.read(CHUNK_SIZE),b""): d.update(chunk)
    return d.hexdigest()
def is_sensitive(path:Path)->bool: return path.name.lower() in SENSITIVE_FILENAMES or path.suffix.lower() in SENSITIVE_SUFFIXES
def iter_files(target:Path)->Iterable[tuple[Path,Path]]:
    if target.is_file(): yield target,Path(target.name); return
    for p in sorted(p for p in target.rglob("*") if p.is_file()): yield p,p.relative_to(target)
def build_inventory(args:argparse.Namespace)->dict:
    target=args.target.resolve()
    if not target.exists(): raise SystemExit(f"Target does not exist: {target}")
    files=[]; omitted=0; total=0
    for absolute,relative in iter_files(target):
        if is_sensitive(absolute): omitted+=1; continue
        size=absolute.stat().st_size; total+=size
        files.append({"path":relative.as_posix(),"size":size,"sha256":sha256_file(absolute),"suffix":absolute.suffix.lower()})
    return {"schema_version":1,"target_id":args.target_id,"product":args.product,"region":args.region,"language":args.language,"version":args.version,"update":args.update,"verification":"Observed","generated_at_utc":datetime.now(timezone.utc).isoformat(),"source_kind":"file" if target.is_file() else "directory","source_name":target.name,"file_count":len(files),"total_bytes":total,"omitted_sensitive_files":omitted,"files":files,"notes":["Generated from a local target supplied by the researcher.","No retail content or key material is embedded in this manifest.","Local absolute paths are intentionally not recorded."]}
def parse_args()->argparse.Namespace:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("target",type=Path); p.add_argument("--target-id",required=True); p.add_argument("--product",required=True); p.add_argument("--region",default="TBD"); p.add_argument("--language",default="TBD"); p.add_argument("--version",default="TBD"); p.add_argument("--update",default="base"); p.add_argument("--output",type=Path,required=True); return p.parse_args()
def main()->None:
    args=parse_args(); inv=build_inventory(args); args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(inv,indent=2,ensure_ascii=False)+"\n",encoding="utf-8"); print(f"Wrote {args.output}: {inv['file_count']} files, {inv['total_bytes']} bytes")
if __name__=="__main__": main()

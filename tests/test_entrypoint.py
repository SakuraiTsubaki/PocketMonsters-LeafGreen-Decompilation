from __future__ import annotations
import hashlib,json,re,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class EntrypointTests(unittest.TestCase):
 def test_entry_evidence_and_source_agree(self):
  r=json.loads((ROOT/"analysis"/"leafgreen-jp-entrypoint.json").read_text(encoding="utf-8"));s=(ROOT/"src"/"rom_entry.s").read_text(encoding="utf-8");self.assertEqual(r["source_sha256"],"2957b392dc09fc8df45a660af5493368d7bd378d299862f4cc115998e9da0bf2");self.assertEqual((r["instruction_word"],r["target_address"]),(0xEA00007F,0x08000204));self.assertEqual(int(re.search(r"\.word 0x([0-9a-f]+)",s).group(1),16),r["instruction_word"])
 def test_manifest_hashes_outputs(self):
  m=json.loads((ROOT/"manifests"/"entrypoint.json").read_text(encoding="utf-8"));
  for o in m["outputs"]:self.assertEqual(hashlib.sha256((ROOT/o["path"]).read_bytes()).hexdigest(),o["sha256"])
if __name__=="__main__":unittest.main()

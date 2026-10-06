import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
class Tests(unittest.TestCase):
 def test_ordered_behavior_and_map(self):
  m=json.loads((ROOT/'analysis/leafgreen-jp-vblank-intr-map.json').read_text());s=(ROOT/'src/vblank_intr.c').read_text();s=s[s.index('void VBlankIntr'):]
  self.assertEqual(m['target']['release'],'BPGJ-rev0');self.assertEqual(m['function']['address'],0x08000724);self.assertEqual(m['function']['range_end_exclusive'],0x080007A8);self.assertFalse(m['rom_code_and_literals']['raw_bytes_published'])
  tokens=['if(gWirelessCommType!=0)','if(gMain.vblankCounter1)','(*gMain.vblankCounter1)++','gMain.vblankCallback()','gMain.vblankCounter2++','CopyBufferedValuesToGpuRegs()','ProcessDma3Requests()','sVcountBeforeSound=(uint8_t)REG_VCOUNT','m4aSoundMain()','sVcountAfterSound=(uint8_t)REG_VCOUNT','TryReceiveLinkBattleData()','Random()','UpdateWirelessStatusIndicatorSprite()','INTR_CHECK|=INTR_FLAG_VBLANK']
  p=[s.index(t) for t in tokens];self.assertEqual(p,sorted(p));self.assertEqual(m['proven_offsets']['vblankCounter1_pointer'],0x20)
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/vblank-intr-reconstruction.json').read_text());self.assertFalse(m['raw_rom_bytes_included'])
  for o in m['outputs']:self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256'])
if __name__=='__main__':unittest.main()


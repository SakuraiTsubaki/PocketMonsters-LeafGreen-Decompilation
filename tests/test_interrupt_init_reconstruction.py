import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
class Tests(unittest.TestCase):
 def test_map_and_behavior(self):
  m=json.loads((ROOT/'analysis/leafgreen-jp-interrupt-init-map.json').read_text());s=(ROOT/'src/interrupt_init.c').read_text();self.assertEqual(m['target']['release'],'BPGJ-rev0');self.assertEqual(m['version_difference'],{'vblank_enable':'EnableInterrupts call','serial_timer3_restore':False});self.assertEqual(m['dma']['byte_count'],0x800);self.assertIn('EnableInterrupts(INTR_FLAG_VBLANK)',s);self.assertNotIn('RestoreSerialTimer3IntrHandlers',s);self.assertFalse(m['rom_code_and_literals']['raw_bytes_published'])
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/interrupt-init-reconstruction.json').read_text());self.assertFalse(m['raw_rom_bytes_included'])
  for o in m['outputs']:self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256'])
if __name__=='__main__':unittest.main()

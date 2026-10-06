import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
class Tests(unittest.TestCase):
 def test_functions_and_behavior(self):
  m=json.loads((ROOT/'analysis/leafgreen-jp-display-serial-interrupt-map.json').read_text());s=(ROOT/'src/display_serial_interrupts.c').read_text()
  self.assertEqual([f['address'] for f in m['functions']],['0x080007DC','0x0800080C','0x08000844']);self.assertFalse(m['rom_code_and_literals']['raw_bytes_published'])
  self.assertIn('if(gMain.hblankCallback)gMain.hblankCallback()',s);self.assertIn('sVcountAtIntr=(uint8_t)REG_VCOUNT;m4aSoundVSync()',s);self.assertIn('if(gMain.serialCallback)gMain.serialCallback()',s)
  for flag in ('HBLANK','VCOUNT','SERIAL'):self.assertEqual(s.count('INTR_FLAG_'+flag),3)
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/display-serial-interrupt-reconstruction.json').read_text());self.assertFalse(m['raw_rom_bytes_included'])
  for o in m['outputs']:self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256'])
if __name__=='__main__':unittest.main()


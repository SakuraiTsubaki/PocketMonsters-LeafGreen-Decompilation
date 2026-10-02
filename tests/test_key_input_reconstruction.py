import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
class Tests(unittest.TestCase):
 def test_game_specific_map_and_source(self):
  m=json.loads((ROOT/'analysis/leafgreen-jp-key-input-map.json').read_text());s=(ROOT/'src/key_input.c').read_text();self.assertEqual(m['target']['release'],'BPGJ-rev0');self.assertEqual([f['address'] for f in m['functions']],[0x080005C0,0x080005E8]);self.assertEqual(m['rom_code_range']['sha256'],'7d473529a37c87cd9a0236adaa8d6ba1fda7a635bc1165b493b7887ac7846d63');self.assertIn('gSaveBlock2Ptr->optionsButtonMode',s);self.assertFalse(m['rom_code_range']['raw_bytes_published'])
 def test_behavioral_reconstruction(self):
  s=(ROOT/'src/key_input.c').read_text()
  for token in ('gMain.keyRepeatCounter--','gMain.newAndRepeatedKeys = keyInput','gMain.newKeys |= A_BUTTON','gMain.watchedKeysPressed = 1'):self.assertIn(token,s)
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/key-input-reconstruction.json').read_text());self.assertFalse(m['raw_rom_bytes_included'])
  for o in m['outputs']:self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256'])
if __name__=='__main__':unittest.main()

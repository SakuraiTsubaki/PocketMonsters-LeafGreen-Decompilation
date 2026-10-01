import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
class Tests(unittest.TestCase):
 def setUp(self):
  self.cfg=json.loads((ROOT/'analysis/leafgreen-jp-thumb-entry-cfg.json').read_text())
  self.map=json.loads((ROOT/'analysis/leafgreen-jp-agb-main-map.json').read_text())
  self.source=(ROOT/'src/main_loop.c').read_text()
 def test_all_verified_calls_are_named(self):
  actual={(x['address'],x['target']) for x in self.map['direct_calls']}
  expected={(x['source'],x['target']) for x in self.cfg['calls']}
  self.assertEqual(actual,expected)
  self.assertTrue(all(x['name'] for x in self.map['direct_calls']))
  self.assertEqual(len(actual),29)
 def test_loop_and_three_dispatches(self):
  edge=self.map['function']['loop_back_edge']
  self.assertIn({'source':edge['source'],'target':edge['target'],'kind':'branch'},self.cfg['edges'])
  calls=[x for x in self.map['direct_calls'] if x['name']=='UpdateLinkAndCallCallbacks']
  self.assertEqual(len(calls),3);self.assertEqual(self.source.count('UpdateLinkAndCallCallbacks();'),3)
 def test_frlg_specific_behavior_is_preserved(self):
  for token in ('InitGpuRegManager();','InitRFU();','ClearDma3Requests();','InitHeap(gHeap,HEAP_SIZE);','rfu_REQ_stopMode();','rfu_waitREQComplete();','ClearSpriteCopyRequests();'):
   self.assertIn(token,self.source)
  self.assertNotIn('gFlashMemoryPresent',self.source)
 def test_manifest_hashes_outputs(self):
  manifest=json.loads((ROOT/'manifests/agb-main-reconstruction.json').read_text())
  for output in manifest['outputs']:
   self.assertEqual(hashlib.sha256((ROOT/output['path']).read_bytes()).hexdigest(),output['sha256'])
if __name__=='__main__':unittest.main()


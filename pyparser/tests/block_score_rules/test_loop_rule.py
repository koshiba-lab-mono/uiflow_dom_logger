from __future__ import annotations
import unittest
import os
import sys


sys.path.append(".")
from pyparser.blocks.assignable_children_block_factory import (
    AssignableChildrenBlockFactory,
)
from pyparser.block_score_rules.loop_rule import LoopRule

with open(os.path.join(__file__, "..", "../imgs/block_dom5.svg"), "r", encoding="utf-8") as f:
    block_dom5 = f.read()


class TestLoopRule(unittest.TestCase):
    def test_loop_rule(self):
        """
        for or while or "ずっと" が使われているブロックスクリプトを適切に評価できる
        """
        factory = AssignableChildrenBlockFactory()

        blocks_collection = factory.create_instances(block_dom5)

        actual_score = LoopRule().score(blocks_collection)
        expected_score = 3 + 1 + 2 + 4  # while(3) + ずっと(1) + for(2) + nest for(4)
        self.assertEqual(actual_score, expected_score)


if __name__ == "__main__":
    unittest.main()

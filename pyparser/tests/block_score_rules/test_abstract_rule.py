from __future__ import annotations

import os
import sys
import unittest

from bs4 import BeautifulSoup

sys.path.append(".")

from pyparser.block_score_rules.abstract_score_rule import AbstactScoreRule
from pyparser.blocks.assignable_children_block_factory import AssignableChildrenBlockFactory

with open(os.path.join(__file__, "..", "../imgs/block_dom7_1.svg"), "r", encoding="utf-8") as f:
    block_dom7_1 = f.read()

with open(os.path.join(__file__, "..", "../imgs/block_dom7_2.svg"), "r", encoding="utf-8") as f:
    block_dom7_2 = f.read()

with open(os.path.join(__file__, "..", "../imgs/block_dom7_3.svg"), "r", encoding="utf-8") as f:
    block_dom7_3 = f.read()

block_dom7 = block_dom7_1 + block_dom7_2 + block_dom7_3


class TestAbstractRule(unittest.TestCase):
    def test_abstract_rule(self):
        """
        抽象化（関数の定義や利用）を行っているスクリプトを適切に評価できる．
        """

        factory = AssignableChildrenBlockFactory()
        blocks_collection = factory.create_instances(block_dom7)
        actual_score = AbstactScoreRule().score(blocks_collection)
        expected_score = 4 + 4 + 1 + 1 + 2  # 定義(4) * 2 + 使用(1), 使用(1), 使用2回目(2)

        self.assertEqual(actual_score, expected_score)


if __name__ == "__main__":
    unittest.main()

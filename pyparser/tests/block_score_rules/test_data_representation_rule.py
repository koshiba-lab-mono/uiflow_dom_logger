from __future__ import annotations
import unittest
import os
import sys

sys.path.append(".")

from pyparser.blocks.assignable_children_block_factory import (
    AssignableChildrenBlockFactory,
)
from pyparser.block_score_rules.data_representation_rule import DataRepresentationRule


with open(os.path.join(__file__, "..", "../imgs/block_dom8.svg"), "r", encoding="utf-8") as f:
    block_dom8 = f.read()


class TestDataRepresentationRule(unittest.TestCase):
    def test_data_representation_rule(self):
        """
        データ表現に関わるブロックを利用しているスクリプトを, 適切に評価できる.
        """

        factory = AssignableChildrenBlockFactory()
        blocks_collection = factory.create_instances(block_dom8)
        actual_score = DataRepresentationRule().score(blocks_collection)
        expected_score = 1 + 3 + 3 + 3 + 2  # 絵文字利用(1) + センサー値表示ラベル利用(3) * 3 + ラベル利用(2)

        self.assertEqual(actual_score, expected_score)


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations
import unittest
import sys
import os

sys.path.append(".")

from pyparser.blocks.assignable_children_block_factory import (
    AssignableChildrenBlockFactory,
)
from pyparser.block_score_rules.logic_rule import LogicRule


with open(os.path.join(os.path.dirname(__file__), "../imgs/block_dom4.svg"), encoding="utf-8") as f:
    block_dom5 = f.read()


class TestLogicRule(unittest.TestCase):
    def test_logic_rule(self):
        """
        if文が使われているブロックスクリプトを適切に点数付けできる
        """
        factory = AssignableChildrenBlockFactory()

        blocks_collection = factory.create_instances(block_dom5)

        actual_score = LogicRule().score(blocks_collection)
        expected_score = 2 + 1 + 3 + 4  # if-else + if + 論理演算子 + ifの入れ子
        self.assertEqual(actual_score, expected_score)


if __name__ == "__main__":
    unittest.main()

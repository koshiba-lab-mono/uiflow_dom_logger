from __future__ import annotations
import unittest
import os
import sys

sys.path.append(".")
from pyparser.blocks.assignable_children_block_factory import AssignableChildrenBlockFactory
from pyparser.block_score_rules.variable_data_rule import VariableDataRule


with open(os.path.join(os.path.dirname(__file__), "../imgs/block_dom6.svg"), "r", encoding="utf-8") as f:
    block_dom6 = f.read()


class TestVariableDataRule(unittest.TestCase):
    def test_variable_data_rule(self):
        """
        変数，配列，連想配列が使われているブロックスクリプトを適切に評価できる
        """

        factory = AssignableChildrenBlockFactory()

        blocks_collection = factory.create_instances(block_dom6)
        rule = VariableDataRule()
        actual_score = 0

        for blocks in blocks_collection:
            actual_score += rule.score(blocks)

        expected_score = 1 + 1 + 1 + 3 + 2 + 1

        self.assertEqual(actual_score, expected_score)


if __name__ == "__main__":
    unittest.main()

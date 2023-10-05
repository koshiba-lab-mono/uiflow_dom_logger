from __future__ import annotations

import os
import sys
import unittest

sys.path.append(".")
from pyparser.block_score_rules.variable_data_score_rule import VariableDataScoreRule
from pyparser.blocks.assignable_children_block_factory import AssignableChildrenBlockFactory

with open(
    os.path.join(os.path.dirname(__file__), "../imgs/block_dom6_1.svg"),
    "r",
    encoding="utf-8",
) as f:
    block_dom6_1 = f.read()

with open(
    os.path.join(os.path.dirname(__file__), "../imgs/block_dom6_2.svg"),
    "r",
    encoding="utf-8",
) as f:
    block_dom6_2 = f.read()

block_dom6 = block_dom6_1 + block_dom6_2


class TestVariableDataRule(unittest.TestCase):
    def test_variable_data_rule(self):
        """
        変数，配列，連想配列が使われているブロックスクリプトを適切に評価できる
        """

        factory = AssignableChildrenBlockFactory()

        blocks_collection = factory.create_instances(block_dom6)
        rule = VariableDataScoreRule()

        actual_score = rule.score(blocks_collection)

        expected_score = 1 + 1 + 1 + 4 + 3 + 1

        self.assertEqual(actual_score, expected_score)


if __name__ == "__main__":
    unittest.main()

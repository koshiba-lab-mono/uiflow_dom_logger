import unittest
import sys
import os

sys.path.append(".")
from pyparser.blocks.assignable_children_block_factory import (
    AssignableChildrenBlockFactory,
)
from pyparser.block_score_policy import CTCPolicyScore

with open(
    os.path.join(__file__, "..", "imgs/test_ctc_policy_score1.svg"),
    "r",
    encoding="utf-8",
) as f:
    block_dom1 = f.read()

with open(
    os.path.join(__file__, "..", "imgs/test_ctc_policy_score2.svg"),
    "r",
    encoding="utf-8",
) as f:
    block_dom2 = f.read()

with open(
    os.path.join(__file__, "..", "imgs/test_ctc_policy_score3.svg"),
    "r",
    encoding="utf-8",
) as f:
    block_dom3 = f.read()

block_dom = block_dom1 + block_dom2 + block_dom3


class TestCTCPolicyScore(unittest.TestCase):
    def test_ctc_policy_sum_score(self):
        """
        全てのルールを適用した総得点を計算できる.
        """
        factory = AssignableChildrenBlockFactory()
        blocks_collection = factory.create_instances(block_dom)
        scorer = CTCPolicyScore()
        actual_score = scorer.comply_with_all(blocks_collection)
        expected_score = (4 + 1) + (1 + 2) + (1 + 4 + 3 + 3) + (3 + 1 + 1) + (1 + 1 + 1)
        self.assertEqual(actual_score, expected_score)

    def test_ctc_policy_each_score(self):
        """
        それぞれのルールの点数を参照できる．
        """

        factory = AssignableChildrenBlockFactory()
        blocks_collection = factory.create_instances(block_dom)
        scorer = CTCPolicyScore()
        actual_score = scorer.each_score(blocks_collection)
        expected_score = [
            ("LoopScoreRule", 3),
            ("LogicScoreRule", 1 + 4 + 3 + 3),
            ("VariableDataScoreRule", 1 + 1 + 1 + 1 + 1),
            ("AbstractRule", 4 + 1),
            ("DataRepresentationScoreRule", 1 + 2),
        ]

        self.assertAlmostEqual([s[1] for s in actual_score], [s[1] for s in expected_score])


if __name__ == "__main__":
    unittest.main()

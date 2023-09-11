from __future__ import annotations

from .block_score_rule import BlockScoreRule
from ..blocks.block import Block

FUNCTION_BLOCK_COLOR = "#995ba5"


def is_use_fucntion_block(block: Block):
    path = block.select_one(".blocklyPath")
    return (path.get("fill") == FUNCTION_BLOCK_COLOR) and block.is_top_cutout()


# 抽象化（関数）利用得点
class AbstractScoreRule(BlockScoreRule):
    def __init__(self):
        self.seen_function_count: dict[str, int] = {}  # 関数名, 使用数

    def score(self, blocks_collection: list[list[Block]]) -> int:
        """
        関数ブロックが定義されている -> 抽象化得点+4
        関数の使用 -> 使用数がそのまま得点になる -> +1 ~
        """

        score = 0
        for blocks in blocks_collection:
            for block in blocks:
                score += self._score_one_block(block)

        return score

    def _score_one_block(self, block: Block):
        score = 0
        # 関数の定義ブロック
        if "関数" in block.words():
            score += 4
        # 関数の利用ブロック
        if is_use_fucntion_block(block):
            function_name = block.words()[0]
            if function_name in self.seen_function_count:
                self.seen_function_count[function_name] += 1
            else:
                self.seen_function_count[function_name] = 1
            score += self.seen_function_count[function_name]

        return score

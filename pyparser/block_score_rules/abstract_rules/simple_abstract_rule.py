from __future__ import annotations

from ...blocks.block import Block
from ..block_score_rule import BlockScoreRule
from .abstract_score_rule import is_use_fucntion_block


class SimpleAbstractScoreRule(BlockScoreRule):
    def score(self, blocks_collection: list[list[Block]]) -> int:
        """
        関数ブロックの定義 or 使用 + 1点
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
            score += 1

        # 関数の利用ブロック
        if is_use_fucntion_block(block):
            score += 1

        return score

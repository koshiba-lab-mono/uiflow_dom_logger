from __future__ import annotations

from ...blocks.block import Block
from ..block_score_rule import BlockScoreRule
from .logic_score_rule import isin_logical_operators


class SimpleLogicScoreRule(BlockScoreRule):
    def score(self, blocks_collection: list[list[Block]]) -> int:
        # if or if-else or 倫理演算子 +1点

        score = 0
        for blocks in blocks_collection:
            for block in blocks:
                score += self._score_one_block(block)

        self.seen_block = {}
        return score

    def _score_one_block(self, block: Block) -> int:
        # if or if-else
        if "もし" in block.words():
            return 1

        # 倫理演算子
        if isin_logical_operators(block.words()):
            return 1

        return 0

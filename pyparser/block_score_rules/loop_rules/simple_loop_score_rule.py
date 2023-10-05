from __future__ import annotations

from ...blocks.block import Block
from ..block_score_rule import BlockScoreRule


def is_while_block(block: Block):
    for word in block.words():
        if "繰り返す：続ける条件" in word or "繰り返す：終わる条件" in word:
            return True
    return False


class SimpleLoopScoreRule(BlockScoreRule):
    def __init__(self):
        self.seen_block: set[Block] = set()

    def score(self, blocks_collection: list[list[Block]]) -> int:
        # ずっと or while or for +1点

        score = 0
        for blocks in blocks_collection:
            for block in blocks:
                score += self._score_one_block(block)

        return score

    def _score_one_block(self, block: Block) -> int:
        # ずっと
        if "ずっと" in block.words():
            return 1

        # for
        if "回繰り返す" in block.words():
            return 1

        # while
        if is_while_block(block):
            return 1

        return 0

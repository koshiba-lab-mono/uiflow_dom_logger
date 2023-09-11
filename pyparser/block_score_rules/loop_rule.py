from __future__ import annotations

from .block_score_rule import BlockScoreRule
from ..blocks.block import Block


def is_while_block(block: Block):
    for word in block.words():
        if "繰り返す：続ける条件" in word or "繰り返す：終わる条件" in word:
            return True
    return False


class LoopRule(BlockScoreRule):
    def __init__(self):
        self.seen_block: set[Block] = set()

    def score(self, blocks_collection: list[list[Block]]) -> int:
        score = 0
        for blocks in blocks_collection:
            for block in blocks:
                score += self._score_one_block(block)

        return score

    def _score_one_block(self, block: Block) -> int:
        score = 0
        if block in self.seen_block:
            return score

        # ずっと
        if "ずっと" in block.words():
            score += 1

        # for
        if "回繰り返す" in block.words():
            score += 2
            # for or while の入れ子
            for child in block.children:
                if "回繰り返す" in child.words() or is_while_block(child):
                    score += 4
                    self.seen_block.add(child)
        # while
        if is_while_block(block):
            score += 3
            # for or while の入れ子
            for child in block.children:
                if "繰り返す" in child.words() or is_while_block(child):
                    score += 4
                    self.seen_block.add(child)

        return score

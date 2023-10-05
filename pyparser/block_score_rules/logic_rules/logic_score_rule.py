from __future__ import annotations

from ...blocks.block import Block
from ..block_score_rule import BlockScoreRule

LOGICAL_OPERATORS_SIMBOLS = {"=", "≠", "<", "≤", ">", "≥"}


def isin_logical_operators(strings: list[str]):
    for operator in LOGICAL_OPERATORS_SIMBOLS:
        for string in strings:
            if operator in string:
                return True
    return False


class LogicScoreRule(BlockScoreRule):
    def __init__(self):
        self.seen_block: set[Block] = set()

    def score(self, blocks_collection: list[list[Block]]) -> int:
        score = 0
        for blocks in blocks_collection:
            for block in blocks:
                score += self._score_one_block(block)

        self.seen_block = {}
        return score

    def _score_one_block(self, block: Block) -> int:
        score = 0
        if block in self.seen_block:
            return score

        # if - else
        if "もし" in block.words() and "そうでなければ" in block.words():
            score += 2
            # if(-else) の入れ子
            for child in block.children:
                if "もし" in child.words():
                    score += 4
                    self.seen_block.add(child)

        # if
        elif "もし" in block.words():
            score += 1
            # if(-else) の入れ子
            for child in block.children:
                if "もし" in child.words():
                    score += 4
                    self.seen_block.add(child)

        # 倫理演算子
        if isin_logical_operators(block.words()):
            score += 3

        return score

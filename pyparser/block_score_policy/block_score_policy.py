from abc import abstractmethod, ABCMeta

from ..block_score_rules.block_score_rule import BlockScoreRule
from ..blocks.block import Block


class BlockScorePolicy(metaclass=ABCMeta):
    def __init__(self):
        self.rules: list[BlockScoreRule] = []

    def add(self, rule: BlockScoreRule):
        self.rules.append(rule)

    def comply_with_all(self, blocks: list[Block]):
        score = 0
        for rule in self.rules:
            score += rule.score(blocks)

        return score

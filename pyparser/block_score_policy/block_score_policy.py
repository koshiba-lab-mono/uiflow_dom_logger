from abc import abstractmethod, ABCMeta

from ..block_score_rules.block_score_rule import BlockScoreRule
from ..blocks.block import Block


class BlockScorePolicy(metaclass=ABCMeta):
    def __init__(self):
        self.rules: list[BlockScoreRule] = []

    def add(self, rule: BlockScoreRule):
        self.rules.append(rule)

    def comply_with_all(self, blocks_collection: list[list[Block]]) -> int:
        score = 0
        for rule in self.rules:
            score += rule.score(blocks_collection)

        return score

    def rule_names(self) -> list[str]:
        return [rule.__class__.__name__ for rule in self.rules]

    def each_score(self, blocks_collection: list[list[Block]]) -> list[tuple[str, int]]:
        name_scores: list[tuple[str, int]] = []
        for rule in self.rules:
            name_scores.append((rule.__class__.__name__, rule.score(blocks_collection)))
        return name_scores

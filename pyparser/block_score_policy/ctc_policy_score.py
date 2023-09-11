from __future__ import annotations

from .block_score_policy import BlockScorePolicy
from ..block_score_rules import (
    LoopScoreRule,
    LogicScoreRule,
    VariableDataScoreRule,
    AbstractScoreRule,
    DataRepresentationScoreRule,
)


class CTCPolicyScore(BlockScorePolicy):
    def __init__(self):
        super().__init__()
        self.add(LoopScoreRule())
        self.add(LogicScoreRule())
        self.add(VariableDataScoreRule())
        self.add(AbstractScoreRule())
        self.add(DataRepresentationScoreRule())

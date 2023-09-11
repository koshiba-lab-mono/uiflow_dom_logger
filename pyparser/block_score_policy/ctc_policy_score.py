from __future__ import annotations

from .block_score_policy import BlockScorePolicy
from ..block_score_rules import (
    LoopRule,
    LogicRule,
    VariableDataRule,
    AbstactRule,
    DataRepresentationRule,
)


class CTCPolicyScore(BlockScorePolicy):
    def __init__(self):
        super().__init__()
        self.add(LoopRule())
        self.add(LogicRule())
        self.add(VariableDataRule())
        self.add(AbstactRule())
        self.add(DataRepresentationRule())

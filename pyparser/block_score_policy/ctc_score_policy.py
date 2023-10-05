from __future__ import annotations

from ..block_score_rules import (
    AbstractScoreRule,
    DataRepresentationScoreRule,
    LogicScoreRule,
    LoopScoreRule,
    VariableDataScoreRule,
)
from .block_score_policy import BlockScorePolicy


class CTCScorePolicy(BlockScorePolicy):
    def __init__(self):
        super().__init__()
        self.add(LoopScoreRule())
        self.add(LogicScoreRule())
        self.add(VariableDataScoreRule())
        self.add(AbstractScoreRule())
        self.add(DataRepresentationScoreRule())

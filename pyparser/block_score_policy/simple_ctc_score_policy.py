from __future__ import annotations

from ..block_score_rules import (
    SimpleAbstractScoreRule,
    SimpleDataRepresentationScoreRule,
    SimpleLogicScoreRule,
    SimpleLoopScoreRule,
    SimpleVariableDataScoreRule,
)
from .block_score_policy import BlockScorePolicy


class SimpleCTCScorePolicy(BlockScorePolicy):
    def __init__(self):
        super().__init__()
        self.add(SimpleLoopScoreRule())
        self.add(SimpleLogicScoreRule())
        self.add(SimpleVariableDataScoreRule())
        self.add(SimpleAbstractScoreRule())
        self.add(SimpleDataRepresentationScoreRule())

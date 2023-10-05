from __future__ import annotations

from abc import ABCMeta, abstractmethod

from ..blocks.block import Block


class BlockScoreRule(metaclass=ABCMeta):
    @abstractmethod
    def score(blocks_collection: list[list[Block]]) -> int:
        ...

from __future__ import annotations

from .variable_data_score_rule import is_variable_block, is_list_block, is_map_block
from ..block_score_rule import BlockScoreRule
from ...blocks.block import Block


# データ（変数や配列）利用加点
class SimpleVariableDataScoreRule(BlockScoreRule):
    def score(self, blocks_collection: list[list[Block]]) -> int:
        score = 0

        for blocks in blocks_collection:
            for block in blocks:
                score += self._score_one_block(block)

        return score

    def _score_one_block(self, block: Block) -> int:
        if is_variable_block(block):
            # 変数に関わるブロック利用していると加点
            return 1
        if is_list_block(block):
            # 配列操作に関わるブロックを利用している
            return 1
        if is_map_block(block):
            # 連想配列に関わるブロックを利用している
            return 1

        return 0

from __future__ import annotations

from ...blocks.block import Block
from ..block_score_rule import BlockScoreRule

VARIABLE_COLOR = "#791e94"


def is_variable_block(block: Block):
    path = block.select_one(".blocklyPath")
    path_color = path.get("fill")
    return path_color == VARIABLE_COLOR


def is_list_block(block: Block):
    for word in block.words():
        if "リスト" in word:
            return True
    return False


def is_map_block(block: Block):
    for word in block.words():
        if "マップ" in word:
            print("sample")
            return True
    return False


# データ（変数や配列）利用加点
class VariableDataScoreRule(BlockScoreRule):
    def score(self, blocks_collection: list[list[Block]]) -> int:
        score = 0

        for blocks in blocks_collection:
            for block in blocks:
                score += self._score_one_block(block)

        return score

    def _score_one_block(self, block: Block) -> int:
        score = 0
        if is_variable_block(block):
            # 変数に関わるブロック利用していると加点
            score += 1
        if is_list_block(block):
            # 配列操作に関わるブロックを利用している
            score += 3
        if is_map_block(block):
            # 連想配列に関わるブロックを利用している
            score += 4

        return score

from __future__ import annotations

from bs4 import Tag

from .block_score_rule import BlockScoreRule
from ..blocks.block import Block

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
            return True
    return False


# データ（変数や配列）利用加点
class VariableDataRule(BlockScoreRule):
    def score(self, blocks: list[Block]) -> int:
        score = 0

        for block in blocks:
            if is_variable_block(block):
                # 変数に関わるブロック利用していると加点
                score += 1

            if is_list_block(block):
                # 配列操作に関わるブロックを利用している
                score += 2

            if is_map_block(block):
                # 連想配列に関わるブロックを利用している
                score += 3

        return score

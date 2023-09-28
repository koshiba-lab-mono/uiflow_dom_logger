from __future__ import annotations

from ..block_score_rule import BlockScoreRule
from ...blocks.block import Block


# データ表現利用得点ルール
class DataRepresentationScoreRule(BlockScoreRule):
    def score(self, blocks_collection: list[list[Block]]) -> int:
        """
        絵文字利用 +1
        数値を画面上に表現するラベルブロックを利用している +2
        """
        #

        score = 0
        for blocks in blocks_collection:
            for block in blocks:
                score += self._score_one_block(block)

        return score

    def _score_one_block(self, block: Block) -> int:
        words = block.words()

        if "絵文字を表示色" in words:
            return 1

        # ラベル表示ブロックの使用
        if "ラベル" in words and "を表示" in words:
            # 　表示する数値がセンサー値や変数だった場合
            if block.children and block.children[0].is_value_block():
                return 3
            else:
                return 2

        return 0

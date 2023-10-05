from __future__ import annotations

from ...blocks.block import Block
from ..block_score_rule import BlockScoreRule


class SimpleDataRepresentationScoreRule(BlockScoreRule):
    def score(self, blocks_collection: list[list[Block]]) -> int:
        """
        絵文字利用 +1
        数値を画面上に表現するラベルブロックを利用している +1
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
            return 1

        return 0

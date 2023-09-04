from __future__ import annotations
from bs4 import BeautifulSoup, Tag

from pyparser.blocks.block import Block
from .block import Block
from .block_factory import IBlockFactory
from ..utils.utils import get_transform_value


class AssignableChildrenBlockFactory(IBlockFactory):
    def create_instances(self, uiflow_html: str) -> list[list[Block]]:
        soup = BeautifulSoup(uiflow_html, "html.parser")
        draggable_block_dom_trees = soup.select("svg > .blocklyDraggable")
        blocks_collection = [
            self._parse_blocks_from_dom_tree(tree) for tree in draggable_block_dom_trees
        ]
        return blocks_collection

    def _parse_blocks_from_dom_tree(self, dom_tree: Tag) -> list[Block]:
        ret_blocks: list[Block] = []

        # (Tag, ParentTag)
        draggable_block_tags: list[tuple[Tag, Block | None]] = [(dom_tree, None)]

        while True:
            if not draggable_block_tags:
                break

            children, parent = draggable_block_tags.pop()
            block = Block("")

            if parent:
                parent.add_children(block)

            for child in children:
                child_classes: list[str] | None = child.get("class")

                # classがblockDrabbableを持っていなければ，その要素はblockの中の要素(pathやtext)である
                if (child_classes is None) or (not "blocklyDraggable" in child_classes):
                    block.add_html(str(child))
                    continue

                if "blocklyInsertionMarker" in child_classes:
                    continue

                # blockDrabbableを持っているchildは，現在イテレーション中のブロックの子，又は，兄弟に動かせるblock(s) を持っている
                relative_child_x, _ = get_transform_value(child)

                # 基準点より右にあれば次のchildブロックは子要素である
                if round(relative_child_x) > 0:
                    draggable_block_tags.append((child, block))

                # それいがい(大体の場合真下)にあれば次のchildブロックは兄弟要素である
                else:
                    draggable_block_tags.append((child, parent))

            ret_blocks.append(block)

        return ret_blocks

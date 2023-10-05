from __future__ import annotations

from abc import ABCMeta, abstractmethod

from bs4 import BeautifulSoup, Tag

from ..blocks.block import Block
from .block import Block


class IBlockFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_instances(self, uiflow_html: str) -> list[list[Block]]:
        ...


class BlockFactory(IBlockFactory):
    def create_instances(self, uiflow_html: str) -> list[list[Block]]:
        soup = BeautifulSoup(uiflow_html, "html.parser")
        draggable_block_dom_trees = soup.select("svg > .blocklyDraggable")
        blocks_collection = [self._parse_blocks_from_dom_tree(tree) for tree in draggable_block_dom_trees]
        return blocks_collection

    def _parse_blocks_from_dom_tree(self, dom_tree: Tag) -> list[Block]:
        ret_blocks: list[Block] = []

        draggable_block_tags: list[Tag] = [dom_tree]
        while True:
            if not draggable_block_tags:
                break

            block_html: str = ""
            children = draggable_block_tags.pop()
            for child in children:
                child_classes: list[str] | None = child.get("class")

                # classがblockDrabbableを持っていなければ，その要素はblockの中の文である
                if (child_classes is None) or (not "blocklyDraggable" in child_classes):
                    block_html += str(child)
                    continue

                if "blocklyDisabled" in child_classes:
                    continue

                if "blocklyInsertionMarker" in child_classes:
                    continue

                # blockDrabbableを持っているdomは，動かせるblock(s) を持っている
                draggable_block_tags.append(child)

            ret_blocks.append(Block(block_html))

        return ret_blocks

from dataclasses import dataclass
from typing import ClassVar

from bs4 import BeautifulSoup

from .block_factory import BlockFactory


@dataclass(frozen=True)
class UiflowBlockDom:
    date: int
    html: str
    block_factory: ClassVar[BlockFactory] = BlockFactory()

    def __post_init__(self):
        object.__setattr__(self, "soup", BeautifulSoup(self.html, "html.parser"))

    def blocks(self):
        return self.block_factory.create_instances(self.html)

from __future__ import annotations
from dataclasses import dataclass
from typing import ClassVar
import datetime

from bs4 import BeautifulSoup
from .block_factory import IBlockFactory
from .assignable_children_block_factory import AssignableChildrenBlockFactory


@dataclass(frozen=True)
class UiflowBlockDOM:
    date: int | datetime.datetime
    html: str
    block_factory: ClassVar[IBlockFactory] = AssignableChildrenBlockFactory()

    def __post_init__(self):
        if isinstance(self.date, int):
            object.__setattr__(
                self,
                "date",
                datetime.datetime.fromtimestamp(self.date / 1000, tz=datetime.timezone(datetime.timedelta(hours=9))),
            )

        object.__setattr__(self, "soup", BeautifulSoup(self.html, "html.parser"))

    def blocks(self):
        return self.block_factory.create_instances(self.html)

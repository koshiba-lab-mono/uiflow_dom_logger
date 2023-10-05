from __future__ import annotations

import datetime
import json
from pathlib import Path

from bs4 import BeautifulSoup

from .assignable_children_block_factory import AssignableChildrenBlockFactory
from .block import Block

block_factory = AssignableChildrenBlockFactory()


class UiflowBlockDOM:
    def __init__(self, date: int, html: str):
        self.date: datetime.datetime = datetime.datetime.fromtimestamp(
            date / 1000, tz=datetime.timezone(datetime.timedelta(hours=9))
        )
        self.html: str = html

    def blocks(self) -> list[Block]:
        return block_factory.create_instances(self.html)

    @classmethod
    def load_instances(cls, json_path: Path) -> list[UiflowBlockDOM]:
        with open(json_path, "r", encoding="utf-8") as f:
            dict_data: list[dict] = json.load(f)
        return [cls(**datum) for datum in dict_data]

    @property
    def soup(self) -> BeautifulSoup:
        return BeautifulSoup(self.html, "html.parser")

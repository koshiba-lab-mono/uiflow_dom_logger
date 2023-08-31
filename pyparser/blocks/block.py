from __future__ import annotations
from dataclasses import dataclass
from bs4 import BeautifulSoup, ResultSet, Tag


@dataclass(frozen=True)
class Block:
    html: str

    def __post_init__(self):
        object.__setattr__(self, "soup", BeautifulSoup(self.html, "html.parser"))

    def select(self, query: str) -> ResultSet[Tag]:
        return self.soup.select(query)

    def select_one(self, query: str) -> Tag:
        return self.soup.select_one(query)

    def words(self):
        return self.soup.get_text().replace("\xa0", "")

    def is_top_cutout(self) -> bool:
        """
        上に切り欠きがあるかどうか
        """

        path = self.select_one(".blocklyPath")
        return "l 6,4  3,0  6,-4" in path.get("d")

    def is_value_block(self) -> bool:
        """
        値ブロック（左に盛りがあるブロックかどうか）
        """
        path = self.select_one(".blocklyPath")
        return "c 0,-10  -8,8  -8,-7.5" in path.get("d")

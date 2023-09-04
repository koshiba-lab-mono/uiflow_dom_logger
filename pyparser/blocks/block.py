from __future__ import annotations
from dataclasses import dataclass, field
from bs4 import BeautifulSoup, ResultSet, Tag


@dataclass(frozen=True)
class Block:
    html: str
    parent: Block | None = None
    _children: list[Block] = field(default_factory=list, compare=False)

    @property
    def soup(self):
        return BeautifulSoup(self.html, "html.parser")

    @property
    def children(self):
        return self._children.copy()

    # AssignableChildrenBlockFactory内でしか使わない
    def add_html(self, html: str):
        object.__setattr__(self, "html", self.html + html)

    # AssignableChildrenBlockFactory内でしか使わない
    def add_children(self, block: Block):
        self._children.append(block)

    def select(self, query: str) -> ResultSet[Tag]:
        return self.soup.select(query)

    def select_one(self, query: str) -> Tag:
        return self.soup.select_one(query)

    def words(self) -> list[str]:
        return [tag.get_text().replace("\xa0", "") for tag in self.soup.select("text")]

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

    def has_child(self) -> bool:
        """
        子要素をもっているか(C型ブロック)どうか
        """
        return not not self.children

import os
import sys
import unittest

sys.path.append(".")
from pyparser.blocks.assignable_children_block_factory import AssignableChildrenBlockFactory
from pyparser.blocks.block_factory import BlockFactory

block_dom1_path = os.path.join(__file__, "..", "./imgs/block_dom1.svg")
block_dom2_path = os.path.join(__file__, "..", "./imgs/block_dom2.svg")
block_dom3_path = os.path.join(__file__, "..", "./imgs/block_dom3.svg")

with open(block_dom1_path, "r", encoding="utf-8") as f:
    block_dom1 = f.read()
with open(block_dom2_path, "r", encoding="utf-8") as f:
    block_dom2 = f.read()
with open(block_dom3_path, "r", encoding="utf-8") as f:
    block_dom3 = f.read()


class TestBlockFactory(unittest.TestCase):
    def test_block_factory(self):
        """
        ブロックを適切な数に分け，インスタンスを作成できる
        """
        factory = BlockFactory()

        # ![image](./imgs/block_dom1.png)
        blocks1 = factory.create_instances(block_dom1)

        # ![image](./imgs/block_dom2.png)
        blocks2 = factory.create_instances(block_dom2)

        self.assertEqual(len(blocks1[0]), 2)  # setup + speakerblock
        self.assertEqual(len(blocks2[0]), 9)  # setup + speakerblock*9

    def test_assinable_child_block_factory(self):
        """
        ブロックがC字型のような子要素を持てるブロックの場合,
        childrenプロパティを生成し, その子要素を参照できる
        """

        factory = AssignableChildrenBlockFactory()

        # ![block_dom3](./imgs/block_dom3.png)
        blocks_collection = factory.create_instances(block_dom3)

        has_children_block_num = 0
        for block in blocks_collection[0]:
            if not block.children:
                return
            has_children_block_num += 1

        self.assertEqual(has_children_block_num, 3)


if __name__ == "__main__":
    unittest.main()

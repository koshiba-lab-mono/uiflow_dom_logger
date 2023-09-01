import unittest
import json
import sys

sys.path.append(".")
from pyparser.blocks.block_factory import BlockFactory


with open("pyparser/tests/sample.json", "r", encoding="utf-8") as f:
    dataset = json.load(f)


class TestBlockFactory(unittest.TestCase):
    def test_block_factory(self):
        factory = BlockFactory()
        blocks1 = factory.create_instances(dataset[-2]["html"])
        blocks2 = factory.create_instances(dataset[-4]["html"])

        self.assertEqual(
            len(blocks1[0]), 2
        )  # setup + speakerblock ![image](./dataset[-2].png)
        self.assertEqual(
            len(blocks2[0]), 9
        )  # setup + speakerblock*9 ![image](./dataset[-4].png)


if __name__ == "__main__":
    unittest.main()

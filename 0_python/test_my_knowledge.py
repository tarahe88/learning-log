import unittest
from aa_my_knowledge import ShoppingList

class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList({"纸巾": 8, "帽子": 30, "拖鞋": 16})

    def test_get_item_count(self):        # 方法一定要以test开头才能被unittest当作测试用例
        self.assertEqual(self.shopping_list.get_item_count(),3)

    def test_get_total_price(self):
        self.assertEqual(self.shopping_list.get_total_price(),54)
# 打开终端  python -m unittest
if __name__ == "__main__":
    unittest.main()  # 这个测试为0也不知道啥意思










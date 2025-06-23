import unittest

from src.work import Product, Category


class TestProductAndCategory(unittest.TestCase):

    def setUp(self):
        self.product1 = Product("Товар 1", "Описание 1", 100, 10)
        self.product2 = Product("Товар 2", "Описание 2", 200, 5)
        self.category = Category("Категория 1", "Описание категории", [self.product1, self.product2])

    def test_product_initialization(self):
        self.assertEqual(self.product1.name, "Товар 1")
        self.assertEqual(self.product1.price, 100)
        self.assertEqual(self.product1.quantity, 10)

    def test_set_price(self):
        self.product1.price = 150
        self.assertEqual(self.product1.price, 150)

    def test_set_price_negative(self):
        with self.assertRaises(ValueError):
            self.product1.price = -50

    def test_new_product(self):
        products_list = []
        new_product = Product.new_product({"name": "Товар 3", "description": "Описание 3", "price": 300, "quantity": 2}, products_list)
        self.assertEqual(len(products_list), 1)
        self.assertEqual(new_product.name, "Товар 3")

    def test_add_product_to_category(self):
        new_product = Product("Товар 3", "Описание 3", 300, 2)
        self.category.add_product(new_product)
        self.assertEqual(len(self.category.products), 3)

    def test_invalid_product_in_category(self):
        with self.assertRaises(ValueError):
            self.category.add_product("Некорректный продукт")


if __name__ == "__main__":
    unittest.main()

import unittest

from src.work import Product, Category, ProductIterator


class TestProduct(unittest.TestCase):
    def test_product_initialization(self):
        product = Product("Товар", "Описание", 100, 10)
        self.assertEqual(product.name, "Товар")
        self.assertEqual(product.price, 100)
        self.assertEqual(product.quantity, 10)

    def test_product_price_update(self):
        product = Product("Товар", "Описание", 100, 10)
        product.price = 150
        self.assertEqual(product.price, 150)

        product.price = -50
        self.assertEqual(product.price, 150)

    def test_product_addition(self):
        product_a = Product("Товар A", "Описание A", 100, 10)
        product_b = Product("Товар B", "Описание B", 200, 2)
        self.assertEqual(product_a + product_b, 1400)


class TestCategory(unittest.TestCase):
    def test_category_initialization(self):
        category = Category("Категория", "Описание категории")
        self.assertEqual(category.name, "Категория")
        self.assertEqual(category.product_count, 1)

    def test_add_product(self):
        category = Category("Категория", "Описание категории")
        product = Product("Товар 1", "Описание 1", 50, 5)
        category.add_product(product)
        self.assertEqual(category.product_count, 1)

    def test_add_invalid_product(self):
        category = Category("Категория", "Описание категории")
        with self.assertRaises(ValueError):
            category.add_product("Не товар")

    def test_product_iterator(self):
        category = Category("Категория", "Описание категории")
        product1 = Product("Товар 1", "Описание 1", 50, 5)
        product2 = Product("Товар 2", "Описание 2", 70, 3)
        category.add_product(product1)
        category.add_product(product2)

        iterator = ProductIterator(category)
        products_list = [product for product in iterator]

        self.assertEqual(len(products_list), 2)
        self.assertEqual(products_list[0].name, "Товар 1")
        self.assertEqual(products_list[1].name, "Товар 2")


if __name__ == '__main__':
    unittest.main()

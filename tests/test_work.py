import unittest


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
        Category.category_count += 1

    def add_product(self, product):
        self.products.append(product)
        Category.product_count += 1


class TestProductCategory(unittest.TestCase):

    def setUp(self):
        self.product1 = Product("Samsung Galaxy S23", "Latest model", 180000.0, 5)
        self.product2 = Product("iPhone 15", "New generation", 210000.0, 8)
        self.category = Category("Smartphones", "Devices for communication and more")

    def test_product_creation(self):
        self.assertEqual(self.product1.name, "Samsung Galaxy S23")
        self.assertEqual(self.product1.price, 180000.0)
        self.assertEqual(self.product1.quantity, 5)

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Smartphones")
        self.assertEqual(self.category.description, "Devices for communication and more")
        self.assertEqual(len(self.category.products), 0)

    def test_add_product(self):
        self.category.add_product(self.product1)
        self.assertEqual(len(self.category.products), 1)
        self.assertEqual(Category.product_count, 1)

        self.category.add_product(self.product2)
        self.assertEqual(len(self.category.products), 2)
        self.assertEqual(Category.product_count, 2)

    def test_category_count(self):
        self.assertEqual(Category.category_count, 2)


if __name__ == '__main__':
    unittest.main()

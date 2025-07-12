import unittest

from src.work import Product, Smartphone, LawnGrass, Category


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product1 = Product("Товар1", "Описание1", 100, 10)

    def test_price_setter_getter(self):
        self.product1.price = 150
        self.assertEqual(self.product1.price, 150)

    def test_price_setter_invalid(self):
        original_price = self.product1.price
        self.product1.price = -50  # Попробуем установить отрицательную цену
        self.assertEqual(self.product1.price, original_price)  # Убедимся, что цена не изменилась

    def test_add_products(self):
        self.product2 = Product("Товар2", "Описание2", 200, 5)
        total_value = self.product1.add(self.product2)
        self.assertEqual(total_value, (100 * 10) + (200 * 5))


class TestSmartphone(unittest.TestCase):
    def setUp(self):
        self.smartphone = Smartphone("iPhone", "Описание", 1000, 5, 90, "Модель", "128GB", "Black")

    def test_initialization(self):
        self.assertEqual(self.smartphone.name, "iPhone")
        self.assertEqual(self.smartphone.price, 1000)


class TestLawnGrass(unittest.TestCase):
    def setUp(self):
        self.lawn_grass = LawnGrass("Газон", "Описание", 50, 100, "Россия", "7 дней", "Зеленый")

    def test_initialization(self):

        self.assertEqual(self.lawn_grass.country, "Россия")


class TestCategory(unittest.TestCase):
    def setUp(self):
        self.category = Category("Электроника", "Различные устройства")
        self.product = Product("Телефон", "Описание", 500, 2)

    def test_add_product(self):
        self.category.add_product(self.product)
        self.assertIn(self.product, self.category.products)

    def test_add_invalid_product(self):

        with self.assertRaises(ValueError):
            self.category.add_product("Некорректный продукт")


if __name__ == '__main__':
    unittest.main()

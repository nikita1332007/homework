import unittest
from unittest.mock import patch
from io import StringIO

from src.work import Product, Smartphone, LawnGrass, Category


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product1 = Product("Товар1", "Описание1", 100, 10)

    def test_price_setter_getter(self):
        self.product1.price = 150
        self.assertEqual(self.product1.price, 150)

    def test_price_setter_invalid(self):
        original_price = self.product1.price
        self.product1.price = -50
        self.assertEqual(self.product1.price, original_price)

    @patch('builtins.input', return_value='y')
    def test_price_setter_lower_price_confirm_yes(self, mocked_input):
        self.product1.price = 100
        self.product1.price = 50  # Понижаем цену
        self.assertEqual(self.product1.price, 50)

    @patch('builtins.input', return_value='n')
    def test_price_setter_lower_price_confirm_no(self, mocked_input):
        original_price = self.product1.price
        self.product1.price = 50
        self.assertEqual(self.product1.price, 100)

    def test_add_products(self):
        product2 = Product("Товар2", "Описание2", 200, 5)
        total_value = self.product1.add(product2)
        self.assertEqual(total_value, (100 * 10) + (200 * 5))

    def test_add_products_different_class_raises(self):
        smartphone = Smartphone("iPhone", "Описание", 1000, 5, 90, "Модель", "128GB", "Black")
        with self.assertRaises(TypeError):
            self.product1.add(smartphone)

    def test_logging_on_creation(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Product("Тест", "Описание", 10, 1)
            output = fake_out.getvalue()
            self.assertIn("Создан объект класса Product", output)


class TestSmartphone(unittest.TestCase):
    def setUp(self):
        self.smartphone = Smartphone("iPhone", "Описание", 1000, 5, 90, "Модель", "128GB", "Black")

    def test_initialization(self):
        self.assertEqual(self.smartphone.name, "iPhone")
        self.assertEqual(self.smartphone.price, 1000)
        self.assertEqual(self.smartphone.memory, "128GB")
        self.assertEqual(self.smartphone.color, "Black")

    def test_add_smartphone(self):
        sp2 = Smartphone("Samsung", "Описание2", 800, 3, 85, "Модель2", "64GB", "White")
        self.assertEqual(self.smartphone.add(sp2), 1000 + 800)

    def test_add_smartphone_with_other_product(self):
        product = Product("Товар", "Описание", 500, 2)
        self.assertEqual(self.smartphone.add(product), NotImplemented)

    def test_logging_on_creation(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Smartphone("TestPhone", "Desc", 500, 2, 80, "ModelX", "256GB", "Red")
            output = fake_out.getvalue()
            self.assertIn("Создан объект класса Smartphone", output)


class TestLawnGrass(unittest.TestCase):
    def setUp(self):
        self.lawn_grass = LawnGrass("Газон", "Описание", 50, 100, "Россия", "7 дней", "Зеленый")

    def test_initialization(self):
        self.assertEqual(self.lawn_grass.country, "Россия")
        self.assertEqual(self.lawn_grass.color, "Зеленый")

    def test_add_lawngrass(self):
        lg2 = LawnGrass("Газон", "Описание", 30, 50, "Россия", "7 дней", "Зеленый")
        result = self.lawn_grass.add(lg2)
        self.assertIsInstance(result, LawnGrass)
        self.assertEqual(result.price, 80)
        self.assertEqual(result.quantity, 150)
        self.assertEqual(result.country, "Россия")

    def test_add_lawngrass_with_other_product(self):
        product = Product("Товар", "Описание", 20, 2)
        self.assertEqual(self.lawn_grass.add(product), NotImplemented)

    def test_logging_on_creation(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            LawnGrass("TestGrass", "Desc", 40, 20, "Россия", "5 дней", "Желтый")
            output = fake_out.getvalue()
            self.assertIn("Создан объект класса LawnGrass", output)


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

    def test_product_count(self):
        self.assertEqual(self.category.product_count, 0)
        self.category.add_product(self.product)
        self.assertEqual(self.category.product_count, 1)


if __name__ == '__main__':
    unittest.main()

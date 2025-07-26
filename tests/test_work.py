import unittest
from unittest.mock import patch
from io import StringIO

from src.work import Category, Product, LawnGrass, Smartphone


class TestProduct(unittest.TestCase):
    def test_product_creation_and_logging(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            p = Product("Test", "Desc", 100, 5)
            output = fake_out.getvalue()
            self.assertIn("Создан объект класса Product с параметрами:", output)
            self.assertEqual(p.name, "Test")
            self.assertEqual(p.price, 100)
            self.assertEqual(p.quantity, 5)

    def test_invalid_quantity_raises(self):
        with self.assertRaises(ValueError):
            Product("Test", "Desc", 50, 0)

    @patch('builtins.input', lambda *args: 'y')
    def test_price_setter_decrease_confirm(self):
        p = Product("Test", "Desc", 100, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            p.price = 50
            output = fake_out.getvalue()
            self.assertIn("Цена обновлена.", output)
            self.assertEqual(p.price, 50)

    @patch('builtins.input', lambda *args: 'n')
    def test_price_setter_decrease_decline(self):
        p = Product("Test", "Desc", 100, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            p.price = 50
            output = fake_out.getvalue()
            self.assertIn("Цена не изменена.", output)
            self.assertEqual(p.price, 100)

    def test_price_setter_invalid_value(self):
        p = Product("Test", "Desc", 100, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            p.price = -1
            output = fake_out.getvalue()
            self.assertIn("Цена не должна быть нулевая или отрицательная", output)
            self.assertEqual(p.price, 100)

    def test_add_method_type_error(self):
        p1 = Product("Test", "Desc", 100, 1)
        p2 = Smartphone("Phone", "Smartphone", 300, 1, 90, "X", "64GB", "Black")
        with self.assertRaises(TypeError):
            p1.add(p2)

    def test_add_method_sum(self):
        p1 = Product("Test", "Desc", 10, 2)
        p2 = Product("Test2", "Desc2", 5, 3)
        self.assertEqual(p1.add(p2), (10*2)+(5*3))


class TestSmartphone(unittest.TestCase):
    def test_smartphone_creation(self):
        s = Smartphone("Phone", "Smartphone", 200, 2, 90, "ModelX", "128GB", "Black")
        self.assertEqual(s.model, "ModelX")
        self.assertEqual(s.price, 200)

    def test_add_two_smartphones(self):
        s1 = Smartphone("Phone1", "Desc", 200, 1, 90, "ModelA", "128GB", "Black")
        s2 = Smartphone("Phone2", "Desc", 300, 1, 92, "ModelB", "256GB", "White")
        self.assertEqual(s1.add(s2), 500)

    def test_add_smartphone_and_product(self):
        s = Smartphone("Phone", "Desc", 200, 1, 90, "ModelX", "64GB", "Red")
        p = Product("Test", "Desc", 100, 1)
        self.assertEqual(s.add(p), NotImplemented)


class TestLawnGrass(unittest.TestCase):
    def test_lawngrass_creation(self):
        l = LawnGrass("Grass", "Green grass", 50, 10, "Russia", 15, "Green")
        self.assertEqual(l.country, "Russia")
        self.assertEqual(l.price, 50)

    def test_add_two_lawngrass(self):
        l1 = LawnGrass("Grass", "Desc", 30, 3, "USA", 10, "Green")
        l2 = LawnGrass("Grass", "Desc", 20, 7, "USA", 10, "Green")
        l3 = l1.add(l2)
        self.assertIsInstance(l3, LawnGrass)
        self.assertEqual(l3.price, 50)
        self.assertEqual(l3.quantity, 10)

    def test_add_lawngrass_and_product(self):
        l = LawnGrass("Grass", "Desc", 30, 3, "USA", 10, "Green")
        p = Product("Test", "Desc", 100, 1)
        self.assertEqual(l.add(p), NotImplemented)


class TestCategory(unittest.TestCase):
    def test_category_creation_and_add(self):
        c = Category("Category1", "Description")
        self.assertEqual(c.product_count, 0)

        p = Product("Test", "Desc", 10, 1)
        c.add_product(p)
        self.assertEqual(c.product_count, 1)
        self.assertIn(p, c.products)

    def test_add_invalid_product_raises(self):
        c = Category("Cat", "Desc")
        with self.assertRaises(ValueError):
            c.add_product("Not a product")

    def test_middle_price_empty_category(self):
        c = Category("Empty", "No products")
        self.assertEqual(c.middle_price(), 0)

    def test_middle_price_with_products(self):
        c = Category("Cat", "Desc")
        p1 = Product("Test1", "Desc1", 10, 1)
        p2 = Product("Test2", "Desc2", 20, 1)
        c.add_product(p1)
        c.add_product(p2)
        self.assertEqual(c.middle_price(), 15)

    def test_category_count_classmethod(self):
        with self.assertRaises(AttributeError):
            Category.category_count()


if __name__ == '__main__':
    unittest.main()

class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        self.products = []
        Category.category_count += 1

    def add_product(self, product):
        self.products.append(product)
        Category.product_count += 1

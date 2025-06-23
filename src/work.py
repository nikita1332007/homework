class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []
        Category.category_count += 1
        for product in self.products:
            self.add_product(product)

    def add_product(self, product):
        self.products.append(product)
        Category.product_count += 1

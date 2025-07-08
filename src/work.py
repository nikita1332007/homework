class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:
            confirmation = input(f"Цена понижается с {self.__price} до {value}. Вы согласны? (y/n): ")
            if confirmation.lower() == 'y':
                self.__price = value
                print("Цена обновлена.")
            else:
                print("Цена не изменена.")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_info, products_list):
        existing_product = next((p for p in products_list if p.name == product_info['name']), None)

        if existing_product:
            existing_product.quantity += product_info['quantity']
            existing_product.price = max(existing_product.price, product_info['price'])
            return existing_product
        else:
            new_product = cls(
                product_info['name'],
                product_info['description'],
                product_info['price'],
                product_info['quantity']
            )
            products_list.append(new_product)
            return new_product

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return (self.price * self.quantity) + (other.price * other.quantity)
        return NotImplemented


class Category:
    category_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise ValueError("Только объекты класса Product могут быть добавлены.")

    @property
    def products(self):
        return self.__products

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов на складе: {total_quantity} шт."


class ProductIterator:
    def __init__(self, category):
        self._category = category
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._category.products):
            product = self._category.products[self._index]
            self._index += 1
            return product
        raise StopIteration

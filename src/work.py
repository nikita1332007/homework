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

    def add(self, other):
        if not isinstance(other, Product):
            raise TypeError("Нельзя складывать продукты различных классов.")
        return (self.price * self.quantity) + (other.price * other.quantity)

    def __add__(self, other):
        return self.add(other)


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period

        self.color = color


class Category:
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Только объекты класса Product и его наследников могут быть добавлены.")
        self.__products.append(product)

    @property
    def products(self):
        return self.__products

    @property
    def product_count(self):
        return len(self.__products)

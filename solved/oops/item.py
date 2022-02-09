class Item(object):
    all = []
    pay_rate = 0.20

    def __init__(self, name: str, price: float, quantity=0) -> None:
        # input validation
        assert price >= 0, "Price should be greater than 0"
        assert quantity >= 0, "Quantity should be 0 or more."

        # object instantiation
        self.__name = name
        self.__price = price
        self.quantity = quantity
        Item.all.append(self)

    # to set a read-only attribute
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    def apply_discount(self, discount=None):
        self.__price = self.__price * discount

    def apply_increment(self):
        self.__price = self.__price + (self.__price * self.pay_rate)

    def __repr__(self) -> str:
        return f'Item(name={self.__name}, price={self.__price}, quantity={self.quantity})'

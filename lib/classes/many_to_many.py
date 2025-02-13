

class Coffee:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3 and not hasattr(self, "name"):
            self._name = value
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters.")

    def orders(self):
        return [order for order in Order.all if order.coffee is self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        return sum([order.price for order in self.orders()]) / self.num_orders() if self.num_orders() != 0 else 0

class Customer:
    
    all = []
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 1 and len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Coffee name must be a string with 1 to 15 characters.")
        
    def orders(self):
        return [order for order in Order.all if order.customer is self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        return Order(self, coffee, float(price))

    @classmethod
    def most_aficionado(self, coffee):
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be a coffee object.")
        if coffee_all_orders := [
            order for order in Order.all if order.coffee is coffee
        ]:
            return max(
                Customer.all,
                key=lambda customer: sum(
                    order.price
                    for order in coffee_all_orders
                    if order.customer is customer
                ),
            )
        return None
    
class Order:
    all = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if isinstance(value, float) and value >= 1.0 and value <= 10.0 and not hasattr(self, "price"):
            self._price = value
        else:
            raise ValueError("Order price must be a float between 1.0 and 10.0.")
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise ValueError("Order customer must be an instance of Customer.")
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise ValueError("Order coffee must be an instance of Coffee.")

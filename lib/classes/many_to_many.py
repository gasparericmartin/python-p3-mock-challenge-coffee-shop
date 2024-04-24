class Coffee:

    all = []

    def __init__(self, name):
        self.name = name
        
        Coffee.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, 'name') and isinstance(name, str) and len(name) >= 3:
            self._name = name
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        unique_list = []
        total_list = [order.customer for order in Order.all if order.coffee == self]

        for customer in total_list:
            if customer not in unique_list:
                unique_list.append(customer)

        return unique_list
    
    def num_orders(self):
        return len([order for order in Order.all if order.coffee == self])
    
    def average_price(self):
        total = 0
        price_list = [order.price for order in Order.all if order.coffee == self]

        for price in price_list:
            total += price
        
        avg = total / len(price_list)
        return avg

class Customer:

    all = []

    def __init__(self, name):
        self.name = name

        Customer.all.append(self)
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        unique_list = []
        total_list = [order.coffee for order in Order.all if order.customer == self]

        for coffee in total_list:
            if coffee not in unique_list:
                unique_list.append(coffee)

        return unique_list
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        Order.all.append(self)
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if not hasattr(self, 'price') and isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price = price

    def customer(self):
        return self.customer
    
    def coffee(self):
        return self.coffee
class Vehicle:
    def __init__(self, type: str, model: str, price: int, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money: int, owner: str):
        if self.price <= money:
            if self.owner is None:
                self.owner = owner
                return f'Successfully bought a {self.type}. Change: {(money - self.price):.2f}'
            else:
                return 'Car already sold'
        return 'Sorry, not enough money'

    def sell(self):
        if self.owner is not None:
            self.owner = None
        return 'Vehicle has no owner'

    def __repr__(self):
        if self.owner is not None:
            return f'{self.model} {self.type} is owned by: {self.owner}'
        return f'{self.model} {self.type} is on sale: {self.price}'


# test code
vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)

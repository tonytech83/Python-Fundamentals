class Inventory:

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item: str):
        if len(self.items) >= self.__capacity:
            return 'not enough room in the inventory'
        else:
            self.items.append(item)

    def get_capacity(self):
        return self.__capacity

    # created private method used to calculate the left items in __repr__ method
    def __get_item_count(self):
        return len(self.items)

    def __repr__(self):
        return f'Items: {", ".join(self.items)}.\nCapacity left: {self.get_capacity() - self.__get_item_count()}'


# test code
inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)

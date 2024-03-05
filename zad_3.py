class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (f"Property: Area - {self.area}"
                f" sq. meters, Rooms - {self.rooms}, "
                f"Price - ${self.price}, "
                f"Address - {self.address}")


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House: {super().__str__()}, Plot - {self.plot} sq. meters"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat: {super().__str__()}, Floor - {self.floor}"


# Creating instances
house1 = House(200, 5, 500000, "123 Main St", 500)
flat1 = Flat(80, 3, 250000, "456 Side St", 2)

# Displaying instances
print(house1)
print("\n")
print(flat1)

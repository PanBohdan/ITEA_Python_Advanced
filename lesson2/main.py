class Car:
    _wheels = 4
    _seats = 4
    _doors = 4
    _engine = 'V6'
    _type = 'Car'

    def set_wheels(self, seats):
        self._seats = seats

    def set_seats(self, wheels):
        self._wheels = wheels

    def set_doors(self, doors):
        self._doors = doors

    def set_engine(self, engine):
        self._engine = engine

    def get_wheels(self):
        return self._wheels

    def get_seats(self):
        return self.seats

    def get_doors(self):
        return self._doors

    def set_engine(self):
        return self._engine


class Truck(Car):
    _type = 'Truck'
    _engine = 'V12'  # idk cars
    _wheels = 8
    _cargo = []

    def add_to_cargo(self, what_to_add):
        self._cargo.append(what_to_add)

    def view_cargo(self):
        print(self._cargo)

    def remove_cargo(self):
        print(f"Removed cargo {self._cargo}")
        self._cargo.clear()


some_car = Car()
some_truck = Truck()
print(some_car.get_wheels())
print(some_truck.get_wheels())
some_truck.add_to_cargo('Cargo one')
some_truck.add_to_cargo('Cargo two')
some_truck.add_to_cargo('Cargo three')
some_truck.view_cargo()
some_truck.remove_cargo()
some_truck.view_cargo()


class Shop:
    global_sold_items = 0

    def __init__(self, shop_name, number_of_sold_items):
        self.shop_name = shop_name
        self.number_of_sold_items = number_of_sold_items
        Shop.global_sold_items += number_of_sold_items

    def sell_items(self, number_of_items):
        self.number_of_sold_items += number_of_items
        Shop.global_sold_items += number_of_items

    def show_all_sold_items(self):
        print(f"all shops sold {Shop.global_sold_items} items")

    def show_sold_items(self):
        print(f"{self.shop_name} sold {self.number_of_sold_items} items")


shop_1 = Shop('shop 1', 50)
shop_2 = Shop('shop 2', 10)
shop_1.show_all_sold_items()
shop_1.sell_items(20)
shop_2.show_all_sold_items()
shop_2.show_sold_items()
shop_1.show_sold_items()
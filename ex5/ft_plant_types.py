#!/usr/bin/env python3


class Plant:
    def __init__(self, name, height, age):
        self._name = name
        self._height = float(height)
        self._age = int(age)

    def grow(self, amount):
        self._height = round(self._height + float(amount), 1)

    def age(self):
        self._age += 1

    def show(self):
        print(f"{self._name}:  {self._height:.1f}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self):
        self.is_blooming = True

    def show(self):
        super().show()
        print(f"Color:  {self.color}")
        if self.is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)

    def produce_shade(self):
        print(
            f"{self._name} now produces a shade of {self._height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )

    def show(self):
        super().show()
        print(f"Trunk diameter:  {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = int(nutritional_value)

    def grow_and_age(self, days):
        for _ in range(days):
            self.grow(2.1)
            self.age()
            self.nutritional_value += 1

    def show(self):
        super().show()
        print(f"Harvest season:  {self.harvest_season}")
        print(f"Nutritional value:  {self.nutritional_value}")


def main():
    print("=== Garden Plant Types ===")

    print("=== Flower ===")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree ===")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable ===")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow_and_age(20)
    tomato.show()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3


class Plant:
    class Stats:
        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def add_grow(self):
            self._grow_calls += 1

        def add_age(self):
            self._age_calls += 1

        def add_show(self):
            self._show_calls += 1

        def show(self):
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, {self._show_calls} show")

    def __init__(self, name, height, age):
        self._name = name
        self._height = float(height)
        self._age = int(age)
        self._stats = Plant.Stats()

    @staticmethod
    def is_older_than_year(days):
        return int(days) > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def grow(self, amount):
        self._height = round(self._height + float(amount), 1)
        self._stats.add_grow()

    def age(self, days=1):
        for _ in range(days):
            self._age += 1
        self._stats.add_age()

    def show(self):
        print(f"{self._name}:  {self._height:.1f}cm, {self._age} days old")
        self._stats.add_show()

    def show_stats(self):
        print(f"[Statistics for {self._name}]")
        self._stats.show()


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
    class TreeStats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._shade_calls = 0

        def add_shade(self):
            self._shade_calls += 1

        def show(self):
            super().show()
            print(f"{self._shade_calls} shade")

    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)
        self._stats = Tree.TreeStats()

    def produce_shade(self):
        print(
            f"{self._name} now produces a shade of {self._height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )
        self._stats.add_shade()

    def show(self):
        super().show()
        print(f"Trunk diameter:  {self.trunk_diameter:.1f}cm")


class Seed(Flower):
    def __init__(self, name, height, age, color, seeds):
        super().__init__(name, height, age, color)
        self.seeds = int(seeds)

    def grow(self, amount):
        super().grow(amount)
        self.seeds += 1

    def age(self, days=1):
        super().age(days)
        self.seeds += days

    def show(self):
        super().show()
        print(f"Seeds:  {self.seeds}")


def show_any_plant_stats(plant):
    plant.show_stats()


def main():
    print("=== Garden statistics ===")
    print("=== Check year-old ===")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()

    print("=== Flower ===")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.show_stats()
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    rose.show_stats()
    print()

    print("=== Tree ===")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.show_stats()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.show_stats()
    print()

    print("=== Seed ===")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    for _ in range(20):
        sunflower.grow(1.5)
        sunflower.age()
    sunflower.bloom()
    sunflower.show()
    show_any_plant_stats(sunflower)
    print()

    print("=== Anonymous ===")
    unknown = Plant.create_anonymous()
    unknown.show()
    show_any_plant_stats(unknown)


if __name__ == "__main__":
    main()

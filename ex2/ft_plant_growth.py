#!/usr/bin/env python3


class Plant:
    def __init__(self, name, height, age, daily_growth):
        self.name = name
        self.height = float(height)
        self.age = int(age)
        self.daily_growth = float(daily_growth)

    def grow(self):
        self.height = round(self.height + self.daily_growth, 1)

    def age_one_day(self):
        self.age += 1

    def show(self):
        print(f"{self.name}:  {self.height:.1f}cm, {self.age} days old")


def main():
    rose = Plant("Rose", 25.0, 30, 0.8)

    print("=== Garden Plant Growth ===")
    rose.show()

    initial_height = rose.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age_one_day()
        rose.show()

    growth = round(rose.height - initial_height, 1)
    print(f"Growth this week:  {growth:.1f}cm")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3


class Plant:
    def __init__(self, name, height, age):
        self._name = name

        if height < 0:
            print(f"{name}:  Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = float(height)

        if age < 0:
            print(f"{name}:  Error, age can't be negative")
            self._age = 0
        else:
            self._age = int(age)

    def set_height(self, new_height):
        if new_height < 0:
            print(f"{self._name}:  Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = float(new_height)
        print(f"Height updated:  {self._height:.0f}cm")

    def set_age(self, new_age):
        if new_age < 0:
            print(f"{self._name}:  Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = int(new_age)
        print(f"Age updated:  {self._age} days")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def show(self):
        print(f"{self._name}:  {self._height:.1f}cm, {self._age} days old")


def main():
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()

    rose.set_height(25)
    rose.set_age(30)
    print()

    rose.set_height(-5)
    rose.set_age(-1)
    print()

    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()

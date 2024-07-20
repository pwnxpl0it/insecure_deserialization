class Person:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def summary(self):
        print(f"My name is {self.name}, I am {self.age} years old!")


robert = Person("Robert", 18)



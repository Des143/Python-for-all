class Animal:
    def __init__(self, name, species):
        self._name = name  # Encapsulation: protected attribute
        self._species = species

    def make_sound(self):
        """Generic sound method to be overridden by subclasses"""
        return "Some generic animal sound"

    def get_info(self):
        """Return information about the animal"""
        return f"Name: {self._name}, Species: {self._species}"


class Dog(Animal):
    def __init__(self, name, breed):
        """Inheritance: Call parent class constructor"""
        super().__init__(name, species="Dog")
        self._breed = breed

    def make_sound(self):
        """Method overriding: Specific implementation for dogs"""
        return "Woof! Woof!"

    def get_info(self):
        """Extended method to include breed information"""
        return f"{super().get_info()}, Breed: {self._breed}"


# Demonstration of the classes
def main():
    # Create an animal instance
    generic_animal = Animal("Generic Pet", "Unknown")
    print(generic_animal.get_info())
    print(generic_animal.make_sound())

    # Create a dog instance
    my_dog = Dog("Buddy", "Labrador")
    print(my_dog.get_info())
    print(my_dog.make_sound())


if __name__ == "__main__":
    main()
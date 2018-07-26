class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self, count=1):
        print(self.name + " is " + str(count) + " sitting.")

    def roll_over(self):
        print(self.name + " rolled over!")

my_dog = Dog('wille', 6)
print("My dog's name is " + my_dog.name + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit(3)
my_dog.roll_over()
my_dog.sit()



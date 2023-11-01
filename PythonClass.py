# 类的定义
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        pass

# 继承和多态
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# 封装和访问控制
class Person:
    def __init__(self, name, age):
        self.__name = name  # 将属性设置为私有
        self.age = age

    def get_name(self):
        return self.__name  # 通过公有方法访问私有属性

# 静态方法和类方法
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def subtract(cls, a, b):
        return a - b

# 抽象类
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

# 实例化对象
dog = Dog("Buddy", "Dog")
cat = Cat("Whiskers", "Cat")

person = Person("Alice", 30)
print(f"{person.get_name()} is {person.age} years old.")  # 访问私有属性通过公有方法

result1 = MathUtils.add(5, 3)  # 调用静态方法
result2 = MathUtils.subtract(8, 2)  # 调用类方法

circle = Circle(5)
area = circle.area()

# 输出
print(dog.speak())  # Dog类的speak方法
print(cat.speak())  # Cat类的speak方法
print(f"5 + 3 = {result1}")  # 调用静态方法
print(f"8 - 2 = {result2}")  # 调用类方法
print(f"Circle with radius {circle.radius} has an area of {area}")  # 调用抽象类的实现

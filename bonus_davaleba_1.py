# მაგალითი_1

from math import sqrt


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        point_1 = (other.x - self.x) ** 2
        point_2 = (other.y - self.y) ** 2
        return sqrt(point_1 + point_2)


x1 = int(input("შეიყვანეთ x1 კოორდინატი: "))
y1 = int(input("შეიყვანეთ y1 კოორდინატი: "))
a = Point(x1, y1)
x2 = int(input("შეიყვანეთ x2 კოორდინატი: "))
y2 = int(input("შეიყვანეთ y2 კოორდინატი: "))
b = Point(x2, y2)
print(a)
print(b)
distance = a + b
print(distance)


# მაგალითი_2

def ways(steps=int(input("შეიყვანეთ საფეხურების რაოდენობა: "))):
    leader1 = 1
    leader2 = 1
    for i in range(2, steps + 1):
        count = leader1 + leader2
        leader2 = leader1
        leader1 = count
    return leader1


print(f"არსებობს კიბეზე ასვლის {ways()} გზა")


# მაგალითი_3

def roman_to_int(change=input("შეიყვანეთ რომაული რიცხვი: ").upper()):
    group = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0
    change = change.replace("IV", "IIII")
    change = change.replace("IX", "VIIII")
    change = change.replace("XL", "XXXX")
    change = change.replace("XC", "LXXXX")
    change = change.replace("CD", "CCCC")
    change = change.replace("CM", "DCCCC")
    for roman in change:
        number += group[roman]
    return number


print(f"თქვენ მიერ შემოყვანილი რომაული რიცხვი არის: {roman_to_int()}")


# მაგალითი_4


class Vector:

    def __init__(self, x=1, y=2):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        x3 = self.x + other.x
        y3 = self.y + other.y
        return Vector(x3, y3)

    def __mul__(self, scalar):
        if isinstance(scalar, int):
            x4 = scalar * self.x
            y4 = scalar * self.y
            return Vector(x4, y4)
        raise TypeError("სკალარის ტიპი უნდა იყოს ინტეჯერი")


num1 = Vector()
num2 = Vector(3, 4)
jami = num1 + num2
print(jami)
print(num1.__add__(num2))
c = num1 * 2
print(c)
print(num1.__mul__(2))

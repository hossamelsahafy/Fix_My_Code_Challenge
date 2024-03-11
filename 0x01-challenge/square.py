#!/usr/bin/python3
"""
Define square class
"""
class square():
"""Class Square"""
    width = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def Permiter_Of_My_Square(self):
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        return "{}".format(self.width)

if __name__ == "__main__":

    s = square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.Permiter_Of_My_Square())  # corrected method name


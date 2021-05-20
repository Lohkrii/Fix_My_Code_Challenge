#!/usr/bin/python3
""" Creates and instance of the class Square """


class Square():
    """ Class square initialization """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initializes the values and dimensions of the square """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """ Calculates the perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Prints the Dimensions of the square """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())

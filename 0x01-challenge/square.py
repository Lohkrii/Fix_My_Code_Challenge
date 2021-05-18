#!/usr/bin/python3
""" Instantiates a square class object """


class square():
    """ Is the class in question """
    width = 0

    def __init__(self, *args, **kwargs):
        """ Initializes the class """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Calculates the perimeter of the square """
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        """ Returns the size of the square """
        return "{}/{}".format(self.width, self.width)

if __name__ == "__main__":

    s = square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())

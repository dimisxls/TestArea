
# SOS χρησιμοποιούμε τους seters όταν τα χαρακτηριστικα της κλασης είναι κρύφα (κάτω παύλα)

from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def print(self):
        print(f"({self.x}, {self.y})")


class Line:
    def __init__(self, point_A = None, point_B = None):
        if point_A is None:
            self.__point_A = Point(0,0)
        else:
            self.__point_A = point_A
        if point_B is None:
            self.__point_B = Point(0,0)
        else:
            self.__point_B = point_B

    def set_point_A(self, x,y):     # SOS χρησιμοποιούμε τους seters όταν τα χαρακτηριστικα της κλασης είναι κρύφα (κάτω παύλα)
        self.__point_A = Point(x,y)

    def set_point_B(self, point_B):     # SOS χρησιμοποιούμε τους seters όταν τα χαρακτηριστικα της κλασης είναι κρύφα (κάτω παύλα)
        self.__point_B = point_B

    def length(self):
        return sqrt((self.__point_A.x-self.__point_B.x)**2 + (self.__point_A.y-self.__point_B.y)**2)

    def print(self):
        self.__point_A.print()
        self.__point_B.print()

l=Line()
l.print()
l.set_point_A(1,1)           # Αν δεν ήταν κρυφά θα γράφαμε l.point_A(Point(1,1))
l.set_point_B(Point(4,5))    # Αν δεν ήταν κρυφά θα γράφαμε l.point_B(Point(1,1))
l.print()
print(l.length())


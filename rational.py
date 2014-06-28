class RationalNumber:
    """
    Rational Numbers with support for arthmetic operations.

        >>> a = RationalNumber(1, 2)
        >>> b = RationalNumber(1, 3)
        >>> a + b
        5/6
        >>> a - b
        1/6
        >>> a * b
        1/6
        >>> a/b
        3/2
    """
    def __init__(self, num, denom=1):
        n = gcd(num, denom)
        self.num=int(num/n)
        self.denom=int(denom/n)

	# Add a rational number to this rational number
    def __add__(self, secondRational):
        num=self.num*secondRational.denom+secondRational.num*self.denom
        denom=self.denom*secondRational.denom
        return RationalNumber(num, denom)

    def __sub__(self, secondRational):
        num=self.num*secondRational.denom-secondRational.num*self.denom
        denom=self.denom*secondRational.denom
        return RationalNumber(abs(num), denom)

    def __mul__(self, secondRational):
        if isinstance(secondRational, int):
            secondRational = RationalNumber(secondRational)
        num=self.num*secondRational.num
        denom=self.denom*secondRational.denom
        return RationalNumber(num, denom)

    def __rmul__(self, secondRational):
        #return RationalNumber.__mul__(self,secondRational)
        #return self.__mul__(secondRational)
        return self * secondRational

    def __truediv__(self, secondRational):
        num=self.num*secondRational.denom
        denom=self.denom*secondRational.num
        return num/denom

	# Return a string representation
    def __str__(self):
        return "%s/%s" % (self.num, self.denom)
		# add check so that 5/1 is returned as 5

    # Return a float for the rational number
    def __float__(self):
        return self.num/self.denom

    # Return an integer for the rational number
    def __int__(self):
        return int(self.num/self.denom)

    def __lt__(self, secondRational):
        return float(self) < float(secondRational)

    def __le__(self, secondRational):
        return float(self) <= float(secondRational)

    def __gt__(self, secondRational):
        return float(self) > float(secondRational)

    def __ge__(self, secondRational):
        return float(self) >= float(secondRational)

    # check for equality
    def __eq__(self, secondRational):
        return float(self) == float(secondRational)

    # Return num and denom using an index operator
    def __getitem__(self, index):
        if index==0:
            return num
        elif index==1:
            return denom
        else:
            raise IndexError ("Index must be '0' or '1'")

    __repr__ = __str__

def gcd(x,y):
    """
    >>> gcd(1424,3084)
    4
    >>> gcd(420,96)
    12
    """

    if x==y:
        return x

    else:
        if x>y:
            return gcd(x-y,y)
        else:
            return gcd(y-x,x)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    r1 = RationalNumber(4,5)
    r2 = RationalNumber(1,3)
    r3 = r1 + r2
    r4 = r1 - r2
    r5 = r1 * r2
    r6 = r2 * 5
    r7 = 5 * r2
    r8= r1 / r2
    print (r3)
    print (r4)
    print (r5)
    print (r6)
    print (r8)
    print (r1==r2)
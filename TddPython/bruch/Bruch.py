
class Bruch(object):
    """
    Bruch is a class, which has the capabilities to calculate a fraction with every
    possible mathematical usage scenario.

    :param int zaehler: numerator of the fraction
    :param int nenner: denominator of the fraction
    """

    def __iter__(self):
        """
        Overrides iterrator to make the class iterable,
        :return: returns iterator object, which can iterate over all the objects in the container
        :rtype: object
        """
        return (self.zaehler, self.nenner).__iter__()

    def __init__(self, zaehler=0, nenner=1):  # using default values for zaehler, nenner
        """
        Constructor of the class Bruch, to identify the given object of the Bruch class and set it to the correct value
        :param zaehler: represents the numerator throughout the application, is set to 0 as a default value
        :param nenner: represents the denominator throughout the application, is set to 1 as a default value
        :return: None
        :rtype: None
        """
        if isinstance(zaehler, Bruch):
            if zaehler.zaehler < 0 and zaehler.nenner < 0:
                self.zaehler, self.nenner = abs(zaehler.zaehler), abs(zaehler.nenner)
            else:
                self.zaehler, self.nenner = zaehler  # this is possible because iter is overwritten
        elif isinstance(zaehler, int) and isinstance(nenner, int):
            if nenner != 0:
                if zaehler < 0 and nenner < 0:
                    self.zaehler, self.nenner = abs(zaehler), abs(nenner)
                else:
                    self.zaehler, self.nenner = zaehler, nenner
            else:
                raise ZeroDivisionError("Please change the value of the denominator, a division by 0 is not possible")
        else:
            raise TypeError("Numerator and denominator have to be of type int to be allowed in a fraction")

    def __float__(self):
        """
        Overrides float to return the value of the fraction if the float method is called
        :return: the divided float value of the fraction is returned
        :rtype: float
        """
        return float(self.zaehler / self.nenner)  # because future division is not imported float has to be called

    def __int__(self):
        """
        Overrides the int method to return the parsed int value of the fraction
        :return: the parsed value of the current (self) fraction is being returned
        :rtype: int
        """
        return int(self.zaehler / self.nenner)

    def __invert__(self):
        """
        Overrides invert to return the reciprocal fraction of the current self fraction
        :return: returns the reciprocal fraction of self
        :rtype: Bruch
        """
        return Bruch(self.nenner, self.zaehler)

    def __neg__(self):
        """
        Overrides negation to return the fraction self with the unused algebraic sign
        :return: returns the negated fraction of self
        :rtype: Bruch
        """
        return Bruch(self.zaehler, -self.nenner)

    def __pow__(self, power):
        """
        Overrides power to return the fraction with the exponent (power) calculated correctly for the fraction self
        :param power: int with which the power will be calculated for the fraction
        :return: returns the fraction with the power calculated as an exponent
        :rtype: Bruch
        :raise TypeError: if the data type of power is not int
        """
        if isinstance(power, int):
            return Bruch(self.zaehler**power, self.nenner**power)
        else:
            raise TypeError("Please use an int, it is the only valid power data type possible")

    def __abs__(self):
        """
        Overrides the absolute value method and returns a fraction object containing both of the absolute values
        :return: a Bruch object containing zaehler first and nenner as the second value is returned
        :rtype: Bruch
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __makeBruch(other):
        """
        makeBruch not a predefined method and is static. It is used to make a Bruch object out of an int.
        :param other: a int value which shall be converted into a fraction object
        :return: returns the fraction object of for the parameter's int value (other/1)
        :rtype: Bruch
        """
        if isinstance(other, int):
            return Bruch(other, 1)
        else:
            raise TypeError("Please use an int for the other parameter of makeBruch")

    def __eq__(self, other):
        """
        Overrides the equals method and returns whether the self fraction is equal or not equal to another
        :param other: another fraction or int which self is compared to
        :return: returns whether the other fraction is equal or not equal to the current one
        :rtype: bool
        """
        if isinstance(other, int):
            if int(self) == other:
                return True
            else:
                return False
        if isinstance(other, Bruch):
            if self.zaehler == other.zaehler and self.nenner == other.nenner:
                return True
            else:
                return False

    def __ne__(self, other):
        """
        Overrides not equals method and returns whether the self fraction is not equal to the other fraction
        :param other: another fraction or int type which self is compared to
        :return: returns whether the other fraction is not equal or equal
        :rtype: bool
        """
        if isinstance(other, Bruch):
            if self.zaehler != other.zaehler or self.nenner != other.nenner:
                return True

    def __ge__(self, other):
        """
        Overrides greater than or equal to and returns whether other is greater than or equal to self
        :param other: another fraction or numeric data type which self is compared to
        :return: returns whether self is greater than or equal to other
        :rtype: bool
        """
        return float(self) >= float(other)

    def __gt__(self, other):
        """
        Overrides greater than and returns whether other is greater than self
        :param other: another fraction or numeric data type which self is compared to
        :return: returns whether self is greater than other
        :rtype: bool
        """
        return float(self) > float(other)

    def __le__(self, other):
        """
        Overrides lower than or equal to and returns whether other is lower than or equal to self
        :param other: another fraction or numeric data type which self is compared to
        :return: returns whether self is lower than or equal to other
        :rtype: bool
        """
        return float(self) <= float(other)

    def __lt__(self, other):
        """
        Overrides lower than and returns whether other is lower than self
        :param other: another fraction or numeric data type which self is compared to
        :return: returns whether self is lower than other
        :rtype: bool
        """
        return float(self) < float(other)

    def __repr__(self):
        """
        Overrides the representation method which returns a string of the current given fraction
        :return: the value of the fraction parsed to a string is returned
        :rtype: str
        """
        if self.nenner == 1:
            return "("+str(self.zaehler)+")"
        else:
            return "("+str(self.zaehler)+"/"+str(self.nenner)+")"

    def __add__(self, other):
        """
        Overrides the add method to add a fraction or an int and return a float
        :param other: int or fraction, which shall be added
        :return: float value of the added variables
        :rtype: float
        :raise TypeError: incompatible types - other than int or fraction
        """
        if isinstance(other, int) or isinstance(other, Bruch):
            return float(self) + float(other)
        else:
            raise TypeError("Please use int or a fraction object for your addition")

    def __radd__(self, other):
        """
        Overrides the right add method to right add a fraction or an int and return a float
        :param other: int or fraction, which shall be added
        :return: float value of the right added variables
        :rtype: float
        :raise TypeError: incompatible types - other than int or fraction
        """
        if isinstance(other, int) or isinstance(other, Bruch):
            return float(self) + float(other)

    def __iadd__(self, other):
        """
        Overrides the in-place add method to add a in-place add a fraction or an int and return a fraction
        :param other: int or fraction, which shall be in-place added
        :return: fraction of the in-place added values
        :rtype: Bruch
        :raise TypeError: incompatible types - other than int or fraction
        """
        if isinstance(other, Bruch):
            self.zaehler += other.zaehler*self.nenner
            self.nenner *= other.nenner
            return Bruch(self.zaehler, self.nenner)
        elif isinstance(other, int):
            self.zaehler += other*self.nenner
            return Bruch(self.zaehler, self.nenner)
        else:
            raise TypeError("Please use int or a fraction object for your augmented assignment addition")

    def __sub__(self, other):
        """
        Overrides the subtraction method to subtract a fraction or an int and return a float
        :param other: int or fraction, which shall be subtracted
        :return: float value of the completed subtraction
        :rtype: float
        :raise TypeError: incompatible types - other than int or fraction
        """
        if isinstance(other, int):
            zaehler, nenner = other, 1
            neuNenner = self.nenner * nenner
            neuZaehler = nenner * self.zaehler - zaehler * self.nenner
            return Bruch(neuZaehler, neuNenner)
        if isinstance(other, Bruch):
            neunenner = self.nenner * other.nenner
            neuzaehler = other.nenner * self.zaehler - other.zaehler * self.nenner
            return Bruch(neuzaehler, neunenner)
        else:
            raise TypeError("Please use int or a fraction object for your subtraction")

    def __rsub__(self, other):
        """
        Overrides the right subtraction method to right subtract a fraction or an int and return a float
        :param other: int or fraction, which shall be subtracted
        :return: float value of the completed right subtraction
        :rtype: float
        :raise TypeError: incompatible types - other than int or fraction
        """
        if isinstance(other, int):
            zaehler, nenner = other, 1
            neunenner = self.nenner * nenner
            neuzaehler = zaehler * self.nenner - nenner * self.zaehler
            return Bruch(neuzaehler, neunenner)
        elif isinstance(other, Bruch):
            neunenner = self.nenner * other.nenner
            neuzaehler = other.zaehler * self.nenner - other.nenner * self.zaehler
            return Bruch(neuzaehler, neunenner)
        else:
            raise TypeError("Please use int or a fraction object for your subtraction")

    def __isub__(self, other):
        """
        Overrides the in-place subtraction method to subtract a fraction or an int and return a float
        :param other: int or fraction, which shall be subtracted
        :return: float value of the completed subtraction
        :rtype: float
        :raise TypeError: incompatible types - other than int or fraction
        """
        if isinstance(other, int):
            self.zaehler -= other * self.nenner
            return self
        elif isinstance(other, Bruch):
            self.zaehler = other.nenner * self.zaehler - other.zaehler * self.nenner
            self.nenner *= other.nenner
            return self
        else:
            raise TypeError("Please use int or a fraction object for your in-place subtraction")

    def __mul__(self, other):
        """
        Overrides the multiplication method to multiply a fraction or an int and return the calculated fraction
        :param other: int or fraction, which shall be multiplied with self
        :return: fraction of the completed multiplication
        :rtype: Bruch
        :raise TypeError: incompatible types - other than int or fraction
        """
        if isinstance(other, int):
            neuzaehler = self.zaehler * other
            return Bruch(neuzaehler, self.nenner)
        elif isinstance(other, Bruch):
            neuzaehler = self.zaehler * other.zaehler
            neunenner = self.nenner * other.nenner
            return Bruch(neuzaehler, neunenner)
        else:
            raise TypeError("Please use int or a fraction object for your multiplication")

    def __rmul__(self, other):
        """
        Overrides the right multiplication method to right multiply a fraction or an int and return the calculated fraction
        :param other: int or fraction, which shall be multiplied with self
        :return: fraction of the completed multiplication
        :rtype: Bruch
        :raise TypeError: incompatible types - other than int or fraction
        """
        if isinstance(other, int) or isinstance(other, Bruch):
            return float(self) * float(other)
        else:
            raise TypeError("Please use int or a fraction object for your right multiplication")

    def __imul__(self, other):
        """
        Overrides the in-place multiplication method to multiply a fraction or an int and return the calculated fraction
        :param other: int or fraction, which shall be multiplied with self
        :return: fraction of the completed multiplication
        :rtype: Bruch
        :raise TypeError: incompatible types - other than int or fraction
        """
        if isinstance(other, int):
            self.zaehler *= other
            return self
        elif isinstance(other, Bruch):
            self.zaehler *= other.zaehler
            self.nenner *= other.nenner
            return self
        else:
            raise TypeError("Please use int or a fraction object for your multiplication")

    def __truediv__(self, other):
        """
        Overrides the division method to divide a fraction or an int and return the calculated fraction
        truediv is used because of compatibility issues to python 3.x
        :param other: int or fraction, which shall be divided by self
        :return: fraction of the completed division
        :rtype: Bruch
        :raise TypeError: incompatible types - other than int or fraction
        """
        if isinstance(other, int):
            neunenner = self.nenner * other
            return Bruch(self.zaehler, neunenner)
        elif isinstance(other, Bruch):
            neuzaehler = self.zaehler * other.nenner
            neunenner = self.nenner * other.zaehler
            return Bruch(neuzaehler, neunenner)
        else:
            raise TypeError("Please use int or a fraction object for your division")

    def __rtruediv__(self, other):
        """
        Overrides the right division method to right divide a fraction or an int and return the calculated fraction
        :param other: int or fraction, which shall be divided by self
        :return: fraction of the completed division
        :rtype: Bruch
        :raise TypeError: incompatible types - other than int or fraction
        """
        if self.zaehler == 0:
            raise ZeroDivisionError("Please use a value for the numerator which is not 0")
        elif isinstance(other, int):
            neunenner = self.nenner * other
            return Bruch(self.zaehler, neunenner)
        elif isinstance(other, Bruch):
            neuzaehler = self.nenner * other.zaehler
            neunenner = self.zaehler * other.nenner
            return Bruch(neuzaehler, neunenner)
        else:
            raise TypeError("Please use int or a fraction object for your division")

    def __itruediv__(self, other):
        """
        Overrides the in-place division method to in-place divide a fraction or an int and return the calculated fraction
        :param other: int or fraction, which shall be divided by self
        :return: fraction of the completed division
        :rtype: Bruch
        :raise TypeError: incompatible types - other than int or fraction
        """
        if isinstance(other, int):
            self = self / other
            return self
        elif isinstance(other, Bruch):
            self = self / other
            return self
        else:
            raise TypeError("Please use int or a fraction object for your in-place division")
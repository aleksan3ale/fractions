"""
This file contains definition of a fraction class.

You should put complete class here. It must be named `Fragion` and must have the following properties:

- four basic mathematical operators defined;
- elegant conversion to string in the form '3/2';
- simplification and clean-up on construction: both attribute divided by the greatest common divisor
  sign in the nominator, denominator not zero (ValueError should be raised in such case), both attributes
  must be integers (ValueError if not),
- method `value` returning float value of the fraction.
"""
from math import gcd


class Fraction(object):
    nom = None  # nominator
    den = None  # denominator

    def __init__(self, nom, den):
        if den == 0:
            raise ValueError("0 in denominator")

        elif den < 0:
            den = - den
            nom = - nom

            if nom == 0:
                self.nom = int(nom)
                self.den = int(den)

            elif gcd(nom, den) > 1:
                den1 = den // gcd(nom, den)
                nom = nom // gcd(nom, den)
                den = den1 // gcd(nom, den)

        elif nom < 0 and den < 0:
            nom = - nom
            den = - den

        elif nom == 0:
            self.nom = int(nom)
            self.den = int(den)

        elif gcd(nom, den) > 1:
            den1 = den // gcd(nom, den)
            nom = nom // gcd(nom, den)
            den = den1 // gcd(nom, den)

        else:
            den = den
            nom = nom

        self.nom = int(nom)
        self.den = int(den)

    # addition
    def __add__(self, other):
        if (self.nom * other.den + self.den * other.nom) == 0:
            return 0
        else:
            return Fraction(self.nom * other.den + self.den * other.nom, self.den * other.den)

    # multiplication
    def __mul__(self, other):
        if self.nom * other.nom == 0:
            return 0
        else:
            return Fraction(self.nom * other.nom, self.den * other.den)

    # division
    def __truediv__(self, other):
        if (self.nom * other.den) == 0:
            return 0
        else:
            return Fraction(self.nom * other.den, self.den * other.nom)

    # subtraction
    def __sub__(self, other):
        if (self.nom * other.den - self.den * other.nom) == 0:
            return 0
        else:
            return Fraction(self.nom * other.den - self.den * other.nom, self.den * other.den)

    # formating
    def __str__(self):
        return "{0.nom}/{0.den}".format(self)

    def __eq__(self, other):
        return self.nom == other.nom and self.den == other.den
    def :
        fracv = fracv.value()
        return fracv

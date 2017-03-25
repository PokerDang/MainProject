# encoding: utf-8

def gcd(a,b):
    if not a>b:
        a,b=b,a
        while b!=0:
            remainder = a%b
            print a,":",b,":"
            a,b=b,remainder
    return a

def lcm(a,b):
    return (a*b)/gcd(a,b)

class Rational(object):
    def __init__(self,number,denom=1):
        print 'in constructor'
        self.numer = number
        self.denom = denom

    def __str__(self):
        print 'in str'
        return str(self.numer)+'/'+str(self.denom)

    def __repr__(self):
        print 'in repr'
        return self.__str__()

    def __add__(self, f):
        print 'in add'

        theLcm = lcm(self.denom,f.denom)
        numeratorSum = (theLcm/self.denom * self.numer) + \
                       (theLcm/f.denom * f.numer)
        return Rational(numeratorSum,theLcm)

    def __sub__(self,f):
        print 'in sub'
        theLcm = lcm(self.denom,f.denom)
        numeratorDiff = (theLcm/self.denom * self.numer) - \
                        (theLcm/f.denom * f.numer)
        return Rational(numeratorDiff,theLcm)


def main():
    oneHalf = Rational(1,2)
    twoFifths=Rational(2,5)
    theSum = oneHalf + twoFifths
main()
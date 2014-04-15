import unittest
import CaesarianShift as cs
ut = unittest

# Here's our "unit".
def IsOdd(n):
    return n % 2 == 1

# Here's our "unit tests".
class CypherGenerationTests(unittest.TestCase):
    def testCaesarianShift(self):
        # test _isCapLtr function
        self.assert_(cs._isCapLtr('A'))
        self.assert_(cs._isCapLtr('M'))
        self.assert_(cs._isCapLtr('Z'))

        # test _isLwrLtr function
        self.assert_(cs._isLwrLtr('a'))
        self.assert_(cs._isLwrLtr('m'))
        self.assert_(cs._isLwrLtr('z'))

        # test _shiftChr function
        self.assert_(cs._shiftChr('a',10) == 'k')
        self.assert_(cs._shiftChr('z',5) == 'e')
        self.assert_(cs._shiftChr('B',10) == 'L')
        self.assert_(cs._shiftChr('Y',5) == 'D')

        # test encode function
        self.assert_(cs.encode("Hello World;",5) == "Mjqqt Btwqi;")
        self.assert_(cs.encode("Hello World7",22) == "Dahhk Sknhz7")
        self.assert_(cs.encode("Hello World.",5) == "Mjqqt Btwqi.")
        self.assert_(cs.encode("Hello World!",22) == "Dahhk Sknhz!")

        # test decode function
        self.assert_(cs.decode("Mjqqt Btwqi?",5) == "Hello World?")
        self.assert_(cs.decode("Dahhk Sknhz*",22) == "Hello World*")
        self.assert_(cs.decode("Mjqqt Btwqi]",5) == "Hello World]")
        self.assert_(cs.decode("Dahhk Sknhz_",22) == "Hello World_")

    

def main():
    ut.main()

if __name__ == '__main__':
    main()
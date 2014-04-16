import unittest
import LtrUtil as lu
ut = unittest

# Here's our "unit tests".
class CypherGenerationTests(unittest.TestCase):
    def testCaesarianShift(self):

        # test isCapLtr function
        self.assert_(lu.isCapLtr('A'))
        self.assert_(lu.isCapLtr('M'))
        self.assert_(lu.isCapLtr('Z'))
        self.assert_(not lu.isCapLtr('a'))
        self.assert_(not lu.isCapLtr('m'))
        self.assert_(not lu.isCapLtr('z'))

        # test isLwrLtr function
        self.assert_(not lu.isLwrLtr('A'))
        self.assert_(not lu.isLwrLtr('M'))
        self.assert_(not lu.isLwrLtr('Z'))
        self.assert_(lu.isLwrLtr('a'))
        self.assert_(lu.isLwrLtr('m'))
        self.assert_(lu.isLwrLtr('z'))

        # test isLtr function
        self.assert_(lu.isLtr('A'))
        self.assert_(lu.isLtr('M'))
        self.assert_(lu.isLtr('Z'))
        self.assert_(lu.isLtr('a'))
        self.assert_(lu.isLtr('m'))
        self.assert_(lu.isLtr('z'))

        # test transformation functions
        self.assert_(lu.multLtr('H',7) == 'X')
        self.assert_(lu.multLtr('e',7) == 'c')
        self.assert_(lu.multLtr('l',7) == 'z')
        self.assert_(lu.multLtr('o',7) == 'u')
        self.assert_(lu.multLtr('W',7) == 'Y')
        self.assert_(lu.multLtr('r',7) == 'p')
        self.assert_(lu.multLtr('d',7) == 'v')
        self.assert_(lu.linearTransLtr('H',5,6) == 'P')
        self.assert_(lu.linearTransLtr('e',5,6) == 'a')
        self.assert_(lu.linearTransLtr('l',5,6) == 'j')
        self.assert_(lu.linearTransLtr('o',5,6) == 'y')
        self.assert_(lu.linearTransLtr('W',5,6) == 'M')
        self.assert_(lu.linearTransLtr('r',5,6) == 'n')
        self.assert_(lu.linearTransLtr('d',5,6) == 'v')

        # test shiftLtr function
        self.assert_(lu.shiftLtr('a',10) == 'k')
        self.assert_(lu.shiftLtr('z',5) == 'e')
        self.assert_(lu.shiftLtr('B',10) == 'L')
        self.assert_(lu.shiftLtr('Y',5) == 'D')


def main():
    ut.main()

if __name__ == '__main__':
    main()
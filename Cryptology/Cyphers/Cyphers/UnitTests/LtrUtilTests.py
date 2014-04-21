import unittest
import LtrUtil as lu
ut = unittest

class LtrUtilTests(ut.TestCase):
    def testLtrUtilIsCapLtr(self):
        # test isCapLtr function
        self.assert_(lu.isCapLtr('A'))
        self.assert_(lu.isCapLtr('M'))
        self.assert_(lu.isCapLtr('Z'))
        self.assert_(not lu.isCapLtr('a'))
        self.assert_(not lu.isCapLtr('m'))
        self.assert_(not lu.isCapLtr('z'))
        
    def testLtrUtilIsLwrLtr(self):
        # test isLwrLtr function
        self.assert_(not lu.isLwrLtr('A'))
        self.assert_(not lu.isLwrLtr('M'))
        self.assert_(not lu.isLwrLtr('Z'))
        self.assert_(lu.isLwrLtr('a'))
        self.assert_(lu.isLwrLtr('m'))
        self.assert_(lu.isLwrLtr('z'))
        
    def testLtrUtilIsLtr(self):
        # test isLtr function
        self.assert_(lu.isLtr('A'))
        self.assert_(lu.isLtr('M'))
        self.assert_(lu.isLtr('Z'))
        self.assert_(lu.isLtr('a'))
        self.assert_(lu.isLtr('m'))
        self.assert_(lu.isLtr('z'))
        
    def testLtrUtilMultLtr(self):
        # test multLtr function
        self.assert_(lu.multLtr('H',7) == 'X')
        self.assert_(lu.multLtr('e',7) == 'c')
        self.assert_(lu.multLtr('l',7) == 'z')
        self.assert_(lu.multLtr('o',7) == 'u')
        self.assert_(lu.multLtr('W',7) == 'Y')
        self.assert_(lu.multLtr('r',7) == 'p')
        self.assert_(lu.multLtr('d',7) == 'v')

    def testLtrUtilLinearTransLtr(self):
        self.assert_(lu.linearTransLtr('H',5,6) == 'P')
        self.assert_(lu.linearTransLtr('e',5,6) == 'a')
        self.assert_(lu.linearTransLtr('l',5,6) == 'j')
        self.assert_(lu.linearTransLtr('o',5,6) == 'y')
        self.assert_(lu.linearTransLtr('W',5,6) == 'M')
        self.assert_(lu.linearTransLtr('r',5,6) == 'n')
        self.assert_(lu.linearTransLtr('d',5,6) == 'v')
        
    def testLtrUtilShiftLtr(self):
        # test shiftLtr function
        self.assert_(lu.shiftLtr('a',10) == 'k')
        self.assert_(lu.shiftLtr('z',5) == 'e')
        self.assert_(lu.shiftLtr('B',10) == 'L')
        self.assert_(lu.shiftLtr('Y',5) == 'D')
        
    def testLtrUtilInvertLtr(self):
        # test shiftLtr function
        self.assert_(lu.invertLtr('a') == 'z')
        self.assert_(lu.invertLtr('z') == 'a')
        self.assert_(lu.invertLtr('B') == 'Y')
        self.assert_(lu.invertLtr('X') == 'C')
        self.assert_(lu.invertLtr('m') == 'n')
        self.assert_(lu.invertLtr('p') == 'k')
        self.assert_(lu.invertLtr('J') == 'Q')
        self.assert_(lu.invertLtr('I') == 'R')


def main():
    ut.main()

if __name__ == '__main__':
    main()
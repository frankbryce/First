import unittest
ut = unittest
    

import BifidUtil as bu
class BifidUtilTests(ut.TestCase):
    def testBifidUtilSetKey(self):
        # generate table correctly
        self.assert_(bu.SetKey("Harry Potter") == 
                                    ([['H','A','R','Y','P'],\
                                      ['O','T','E','B','C'],\
                                      ['D','F','G','I','K'],\
                                      ['L','M','N','Q','S'],\
                                      ['U','V','W','X','Z']]))

    def testBifidUtilGetRow(self):
        bu.SetKey("Harry Potter")

        # get the rows of letters correctly
        self.assert_(bu.GetRow('A') == 0)
        self.assert_(bu.GetRow('B') == 1)
        self.assert_(bu.GetRow('J') == 2)
        self.assert_(bu.GetRow('L') == 3)
        self.assert_(bu.GetRow('V') == 4)
        
    def testBifidUtilGetCol(self):
        bu.SetKey("Harry Potter")

        # get the columns of letters correctly
        self.assert_(bu.GetCol('O') == 0)
        self.assert_(bu.GetCol('M') == 1)
        self.assert_(bu.GetCol('R') == 2)
        self.assert_(bu.GetCol('Q') == 3)
        self.assert_(bu.GetCol('Z') == 4)
        
    def testBifidUtilGetChr(self):
        bu.SetKey("Harry Potter")

        # get the characters based on it's position in the table
        self.assert_(bu.GetChr(4,2) == 'W')
        self.assert_(bu.GetChr(1,4) == 'C')
        self.assert_(bu.GetChr(1,2) == 'E')
        self.assert_(bu.GetChr(2,1) == 'F')
        self.assert_(bu.GetChr(4,3) == 'X')
        
    def testBifidUtilGenerateResult(self):
        bu.SetKey("Harry Potter")

        # generate result of bifid cipher
        self.assert_(bu.GenerateResult("Hello World") == 'AQCONRHRRH')
        
    def testBifidUtilGenerateInput(self):
        bu.SetKey("Harry Potter")

        # generate result of bifid cipher
        self.assert_(bu.GenerateInput("Aqcon Rhrrh") == 'HELLOWORLD')
        
    def testBifidUtilJToI(self):
        # get the columns of letters correctly
        self.assert_(bu.jtoi('qprAOISJDFWKEJFOIAJsdofijwepor') == 'QPRAOISIDFWKEIFOIAISDOFIIWEPOR')

import Bifid as b
class BifidTests(unittest.TestCase):
    def testBifidEncode(self):
        print b.encode("hello world","albus dumbledore")
        self.assert_(b.encode("hello world","albus dumbledore") == "FARMLPMNTD")
        self.assert_(b.encode("hello world","hermione granger") == "HFBOFEZERW")
        self.assert_(b.encode("hello world","ronald weasley") == "CROROVZWDT")
        self.assert_(b.encode("hello world","neville longbottom") == "ANMTVWZEIX")

    def testBifidDecode(self):
        self.assert_(b.decode("farml pmntd","albus dumbledore") == "HELLOWORLD")
        self.assert_(b.decode("hfbof ezerw","hermione granger") == "HELLOWORLD")
        self.assert_(b.decode("croro vzwdt","ronald weasley") == "HELLOWORLD")
        self.assert_(b.decode("anmtv wzeix","neville longbottom") == "HELLOWORLD")



def main():
    ut.main()

if __name__ == '__main__':
    main()
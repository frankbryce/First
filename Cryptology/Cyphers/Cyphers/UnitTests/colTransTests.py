import unittest
import ColTrans as ct
ut = unittest

#class ColTransTests(ut.TestCase):
#    def testColTransEncode(self):
#        # test encode function
#        self.assert_(ct.encode("Hello World",[1])             == "HELLOWORLD")
#        print ct.encode("Hello World",[3,1,2]) 
#        self.assert_(ct.encode("Hello World",[3,1,2])         == "EORLWLHLOD")
#        self.assert_(ct.encode("Hello World",[1,4,2,5,3])     == "HWLRODEOLL")
#        self.assert_(ct.encode("Hello World",[7,3,4,2,6,1,5]) == "WLELLDOOHR")
        
#    def testColTransDecode(self):
#        # test decode function
#        self.assert_(ct.decode("HelloWorld",[1])             == "HELLOWORLD")
#        self.assert_(ct.decode("EORLWLHLOD",[3,1,2])         == "HELLOWORLD")
#        self.assert_(ct.decode("HWLRODEOLL",[1,4,2,5,3])     == "HELLOWORLD")
#        self.assert_(ct.decode("WLELLDOOHR",[7,3,4,2,6,1,5]) == "HELLOWORLD")

    

def main():
    ut.main()

if __name__ == '__main__':
    main()
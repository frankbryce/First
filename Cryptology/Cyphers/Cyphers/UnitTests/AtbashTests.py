import unittest
import Atbash as a
ut = unittest

class AtbashTests(ut.TestCase):
    def testAtbashEncode(self):
        # test encode function
        self.assert_(a.encode("Hello World;") == "Svool Dliow;")
        
    def testAtbashDecode(self):
        # test decode function
        self.assert_(a.encode("Svool Dliow8") == "Hello World8")
    
def main():
    ut.main()

if __name__ == '__main__':
    main()
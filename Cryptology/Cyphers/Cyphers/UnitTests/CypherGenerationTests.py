import unittest
import CaesarianShift as cs
ut = unittest

class CaesarianShiftTests(ut.TestCase):
    def testCaesarianShiftEncode(self):
        # test encode function
        self.assert_(cs.encode("Hello World;",5) == "Mjqqt Btwqi;")
        self.assert_(cs.encode("Hello World7",22) == "Dahhk Sknhz7")
        self.assert_(cs.encode("Hello World.",5) == "Mjqqt Btwqi.")
        self.assert_(cs.encode("Hello World!",22) == "Dahhk Sknhz!")
        
    def testCaesarianShiftDecode(self):
        # test decode function
        self.assert_(cs.decode("Mjqqt Btwqi?",5) == "Hello World?")
        self.assert_(cs.decode("Dahhk Sknhz*",22) == "Hello World*")
        self.assert_(cs.decode("Mjqqt Btwqi]",5) == "Hello World]")
        self.assert_(cs.decode("Dahhk Sknhz_",22) == "Hello World_")

    

def main():
    ut.main()

if __name__ == '__main__':
    main()
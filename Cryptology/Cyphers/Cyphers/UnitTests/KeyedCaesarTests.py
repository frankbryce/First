import unittest
import KeyedCaesar as kc
ut = unittest

class KeyedCaesarTests(ut.TestCase):
    def testKeyedCaesarEncode(self):
        kc.SetKey('Harry Potter')

        # test encode function
        self.assert_(kc.encode("Hello World;",5) == "Mjqqt Btwqi;")
        self.assert_(kc.encode("Hello World7",22) == "Dahhk Sknhz7")
        self.assert_(kc.encode("Hello World.",5) == "Mjqqt Btwqi.")
        self.assert_(kc.encode("Hello World!",22) == "Dahhk Sknhz!")

    def testKeyedCaesarDecode(self):
        kc.SetKey('Harry Potter')

        # test decode function
        self.assert_(kc.decode("Mjqqt Btwqi?",5) == "Hello World?")
        self.assert_(kc.decode("Dahhk Sknhz*",22) == "Hello World*")
        self.assert_(kc.decode("Mjqqt Btwqi]",5) == "Hello World]")
        self.assert_(kc.decode("Dahhk Sknhz_",22) == "Hello World_")

    def testKeyedCaesarEncodeNoKey(self):
        kc.SetKey('')

        # test encode function
        self.assert_(kc.encode("Hello World;",5) == "Mjqqt Btwqi;")
        self.assert_(kc.encode("Hello World7",22) == "Dahhk Sknhz7")
        self.assert_(kc.encode("Hello World.",5) == "Mjqqt Btwqi.")
        self.assert_(kc.encode("Hello World!",22) == "Dahhk Sknhz!")
        
    def testKeyedCaesarDecodeNoKey(self):
        kc.SetKey('')

        # test decode function
        self.assert_(kc.decode("Mjqqt Btwqi?",5) == "Hello World?")
        self.assert_(kc.decode("Dahhk Sknhz*",22) == "Hello World*")
        self.assert_(kc.decode("Mjqqt Btwqi]",5) == "Hello World]")
        self.assert_(kc.decode("Dahhk Sknhz_",22) == "Hello World_")

    

def main():
    ut.main()

if __name__ == '__main__':
    main()
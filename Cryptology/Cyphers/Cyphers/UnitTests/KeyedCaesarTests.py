import unittest
import KeyedCaesar as kc
ut = unittest

class KeyedCaesarTests(ut.TestCase):
    def testKeyedCaesarEncode(self):
        kc.SetKey('Harry Potter')

        # test encode function
        self.assert_(kc.encode("Hello World;",5)  == "GCLLQAQVLB")
        self.assert_(kc.encode("Hello World7",22) == "YHEEDNDIEZ")
        self.assert_(kc.encode("Hello World.",5)  == "GCLLQAQVLB")
        self.assert_(kc.encode("Hello World!",22) == "YHEEDNDIEZ")

    def testKeyedCaesarDecode(self):
        kc.SetKey('Harry Potter')

        # test decode function
        kc.decode("Gcllq Aqvlb?",5)
        self.assert_(kc.decode("Gcllq Aqvlb?",5)  == "HELLOWORLD")
        self.assert_(kc.decode("Yheed Ndiez*",22) == "HELLOWORLD")
        self.assert_(kc.decode("Gcllq Aqvlb]",5)  == "HELLOWORLD")
        self.assert_(kc.decode("Yheed Ndiez_",22) == "HELLOWORLD")

    def testKeyedCaesarEncodeNoKey(self):
        kc.SetKey('')

        # test encode function
        self.assert_(kc.encode("Hello World;",5)  == "MJQQTBTWQI")
        self.assert_(kc.encode("Hello World7",22) == "DAHHKSKNHZ")
        self.assert_(kc.encode("Hello World.",5)  == "MJQQTBTWQI")
        self.assert_(kc.encode("Hello World!",22) == "DAHHKSKNHZ")
        
    def testKeyedCaesarDecodeNoKey(self):
        kc.SetKey('')

        # test decode function
        self.assert_(kc.decode("Mjqqt Btwqi?",5)  == "HELLOWORLD")
        self.assert_(kc.decode("Dahhk Sknhz*",22) == "HELLOWORLD")
        self.assert_(kc.decode("Mjqqt Btwqi]",5)  == "HELLOWORLD")
        self.assert_(kc.decode("Dahhk Sknhz_",22) == "HELLOWORLD")

    

def main():
    ut.main()

if __name__ == '__main__':
    main()
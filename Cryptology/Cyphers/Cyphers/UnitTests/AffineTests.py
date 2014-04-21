import unittest
import Affine as a
ut = unittest

class AffineTests(ut.TestCase):
    def testAffineEncode(self):
        # test encode function
        self.assert_(a.encode("Hello World;",5,2) == "Lwffu Iujfr;")
        self.assert_(a.encode("Hello World7",9,7) == "Srccd Xdeci7")
        self.assert_(a.encode("Hello World.",1,1) == "Ifmmp Xpsme.")
        self.assert_(a.encode("Hello World!",3,0) == "Vmhhq Oqzhj!")

    def testAffineDecode(self):
        # test decode function
        self.assert_(a.decode("Lwffu Iujfr?",5,2) == "Hello World?")
        self.assert_(a.decode("Srccd Xdeci*",9,7) == "Hello World*")
        self.assert_(a.decode("Ifmmp Xpsme]",1,1) == "Hello World]")
        self.assert_(a.decode("Vmhhq Oqzhj_",3,0) == "Hello World_")


def main():
    ut.main()

if __name__ == '__main__':
    main()
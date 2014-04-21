import unittest
import StrUtil as su
ut = unittest    

class StrUtilTests(ut.TestCase):
    def testStrUtilStripStr(self):
        self.assert_(su.StripStr('.a ,wjenr.,ajDNFz,xjsa .sanf.,sadjf we, na,jf.a,sjenf.ewa,j n') == \
                                 'AWJENRAJDNFZXJSASANFSADJFWENAJFASJENFEWAJN')

    def testStrUtilReformatStr(self):
        self.assert_(su.ReformatStr('HELLOWERSTL','Harry Potter') == 'Hello Werstl')

    def testStrUtilGenerateKeyedAlphabet(self):
        self.assert_(su.GenerateKeyedAlphabet('HARYPOTE','ABCDEFGHIKLMNOPQRSTUVWXYZ') == list('HARYPOTEBCDFGIKLMNQSUVWXZ'))


def main():
    ut.main()

if __name__ == '__main__':
    main()
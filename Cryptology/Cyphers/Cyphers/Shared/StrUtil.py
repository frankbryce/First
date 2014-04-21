import re
import LtrUtil as lu
from collections import OrderedDict as od
puncRegEx = re.compile("[,. ]+")

def StripStr(str):
    return puncRegEx.sub("",str.upper())

def GenerateKeyedAlphabet(key,alph):
    return list(od.fromkeys(key+alph))

def ReformatStr(str,format):
    i=0
    outstr = '';
    for c in format:
        if lu.isLtr(c):
            if c.isupper():
                outstr = outstr + str[i].upper()
            else:
                outstr = outstr + str[i].lower()
            i = i + 1
        else:
            outstr = outstr + c
    return outstr
    
    
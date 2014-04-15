A = 65
a = 97

def _isCapLtr(c):
    if (ord(c) < 65 or ord(c) > 90):
        return False
    return True

def _isLwrLtr(c):
    if (ord(c) < 97 or ord(c) > 122):
        return False
    return True

def _isLetter(c):
    if (_isCapLtr(c) or _isLwrLtr(c)):
        return True
    return False

def _shiftChr(c,s):
    if (_isCapLtr(c)):
        o = A
    elif (_isLwrLtr(c)):
        o = a
    else:
        return c
    return chr((ord(c)-o+s) % 26 + o)

def encode(str,shamt):
    return ''.join([ _shiftChr(c,shamt) for c in str ])

def decode(str,shamt):
    return ''.join([ _shiftChr(c,-shamt) for c in str ])

def decode(str):

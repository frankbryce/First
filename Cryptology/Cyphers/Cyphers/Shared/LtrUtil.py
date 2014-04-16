# ASCII
A = 65
a = 97

def isCapLtr(c):
    if (ord(c) < 65 or ord(c) > 90):
        return False
    return True

def isLwrLtr(c):
    if (ord(c) < 97 or ord(c) > 122):
        return False
    return True

def isLtr(c):
    if (isCapLtr(c) or isLwrLtr(c)):
        return True
    return False

def shiftLtr(c,s):
    if (isCapLtr(c)):
        o = A
    elif (isLwrLtr(c)):
        o = a
    else:
        return c
    return chr((ord(c)-o+s) % 26 + o)

def multLtr(c,m):
    if (isCapLtr(c)):
        o = A
    elif (isLwrLtr(c)):
        o = a
    else:
        return c
    return chr(((ord(c)-o)*m) % 26 + o)

def linearTransLtr(c,m,b):
    if (isCapLtr(c)):
        o = A
    elif (isLwrLtr(c)):
        o = a
    else:
        return c
    return chr(((ord(c)-o)*m+b) % 26 + o)
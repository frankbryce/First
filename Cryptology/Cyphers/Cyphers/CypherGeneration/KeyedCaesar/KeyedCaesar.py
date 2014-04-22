import StrUtil as su

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
keyedalph = []

def SetKey(key):
    global alphabet
    global keyedalph
    keyedalph = su.GenerateKeyedAlphabet(su.StripStr(key),alphabet)

def encode(str,shamt):
    str = su.StripStr(str)
    return ''.join([ keyedalph[(alphabet.index(c) + shamt) % 26] for c in str if c.isalpha() ])

def decode(str,shamt):
    str = su.StripStr(str)
    return ''.join([ alphabet[(keyedalph.index(c) - shamt) % 26] for c in str if c.isalpha() ])

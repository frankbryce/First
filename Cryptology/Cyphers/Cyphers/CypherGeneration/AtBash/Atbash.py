import LtrUtil

def encode(str):
    return ''.join([ LtrUtil.invertLtr(c) for c in str ])

def decode(str):
    return encode(str)

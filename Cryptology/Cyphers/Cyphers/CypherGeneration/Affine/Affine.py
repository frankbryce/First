import LtrUtil

def encode(str,m,b):
    return ''.join([ LtrUtil.linearTransLtr(c,m,b) for c in str ])

def decode(str,m,b):
    return ''.join([ LtrUtil.shiftLtr(c,-b) for c in str ])

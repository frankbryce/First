import LtrUtil
import modarith

def encode(str,m,b):
    assert m%13!=0 and m%2!=0
    return ''.join([ LtrUtil.linearTransLtr(c,m,b) for c in str ])

def decode(str,m,b):
    assert m%13!=0 and m%2!=0
    return ''.join([ LtrUtil.multLtr(LtrUtil.shiftLtr(c,-b),modarith.modinv(m,26)) for c in str ])

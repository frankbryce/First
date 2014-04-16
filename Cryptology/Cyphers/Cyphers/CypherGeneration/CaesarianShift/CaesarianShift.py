import LtrUtil

def encode(str,shamt):
    return ''.join([ LtrUtil.shiftLtr(c,shamt) for c in str ])

def decode(str,shamt):
    return ''.join([ LtrUtil.shiftLtr(c,-shamt) for c in str ])

import StrUtil as su

def encode(str,colOrder):
    str = su.StripStr(str)
    m = min(colOrder)
    colOrder[:] = [x - m for x in colOrder]
    return str

def decode(str,colOrder):
    str = su.StripStr(str)
    m = min(colOrder)
    colOrder[:] = [x - m for x in colOrder]
    return str

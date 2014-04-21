import StrUtil as s

alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' # intentionally missing 'j'
Table = []
Result = []

def SetKey(keyword):
    global Table
    keyword = jtoi(s.StripStr(keyword))
    keyalph = s.GenerateKeyedAlphabet(keyword,alphabet)
    Table = [keyalph[i:i+5] for i in xrange(0, len(keyalph), 5)]
    return Table

def jtoi(c):
    return c.upper().replace("J","I")

def GetRow(c):
    global Table
    c = jtoi(c)
    return [i for i,row in enumerate(Table) if c in row][0]

def GetCol(c):
    global Table
    c = jtoi(c)
    return [row.index(c) for _,row in enumerate(Table) if c in row][0]

def GetChr(r,c):
    global Table
    return Table[r][c]

def GenerateResult(str):
    str = jtoi(s.StripStr(str))
    nums = [GetRow(c) for c in str]+[GetCol(c) for c in str]
    numtuples = [nums[i:i+2] for i in xrange(0, len(nums), 2)]
    return ''.join([GetChr(r,c) for (r,c) in numtuples])

def GenerateInput(str):
    str = jtoi(s.StripStr(str))
    tuples = [[GetRow(c),GetCol(c)] for c in str]
    nums = [item for tuple in tuples for item in tuple]
    coords = [(nums[i],nums[i+len(nums)/2]) for i in range(len(nums)/2)]
    return ''.join([GetChr(r,c) for (r,c) in coords])
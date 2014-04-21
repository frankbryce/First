import BifidUtil as bu

currentKey = ''

def encode(str,keyword):
    global currentKey
    if keyword is not currentKey:
        bu.SetKey(keyword)
    return bu.GenerateResult(str)

def decode(str,keyword):
    global currentKey
    if keyword is not currentKey:
        bu.SetKey(keyword)
    return bu.GenerateInput(str)

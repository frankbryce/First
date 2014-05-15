# constants
import Constants

tape = []
initialPos = 0

def Initialize(filename):
    global tape, initialPos
    with open(filename) as f:
        content = f.readlines()
    tape = content[1].split()
    initialPos = int(content[0])

def Print():
    print tape
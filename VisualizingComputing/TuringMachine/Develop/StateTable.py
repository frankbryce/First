# constants
import Constants

states = []
alphabet = []
nextState = {}
nextMove = []

def Initialize(filename):
    global alphabet, states, nextState, nextMove
    with open(filename) as f:
        content = f.readlines()
    stateTable = [content[i].split() for i in range(len(content))]
    states = [stateTable[0][i] for i in range(len(stateTable[0]))[1:]]
    alphabet = [stateTable[i][0] for i in range(len(stateTable))[1:]]
    nextState = {alphabet[i] : [stateTable[i+1][j].split(':')[0] for j in range(len(stateTable[i+1]))[1:]] for i in range(len(alphabet))}
    nextMove = {alphabet[i] : [stateTable[i+1][j].split(':')[1] for j in range(len(stateTable[i+1]))[1:]] for i in range(len(alphabet))}

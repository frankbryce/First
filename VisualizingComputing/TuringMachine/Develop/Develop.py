import Constants
import StateTable
import TuringTape

def runDefault():
    run(Constants.DefaultStateFile,Constants.DefaultTapeFile)

def run(stateFile,tapeFile):
    StateTable.Initialize(stateFile)
    TuringTape.Initialize(tapeFile)
    moveint = {Constants.Left : -1, Constants.Stay : 0, Constants.Right : 1}

    currState = StateTable.states[0]
    currPos = TuringTape.initialPos
    nextState = currState
    nextPos = currPos
    try:
        while True:
            currPos = nextPos
            currState = nextState

            ltr = TuringTape.tape[currPos]
            stidx = StateTable.states.index(currState)
            move = StateTable.nextMove[ltr][stidx]

            nextPos = currPos + moveint[move]
            nextState = StateTable.nextState[ltr][stidx]
            TuringTape.Print()
            print currPos

    except Exception:
        print 'We are finished'
        TuringTape.Print()
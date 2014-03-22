import inst
import dec

# global variables
memory = []
registers = []
#next instruction
pReg = 0
#current instruction
iReg = 0
debug = 1

# display state
def disp():
    #global pReg
    #global iReg
    #global registers
    print("The Mythical Machine")
    print
    print("P reg  %06d"%pReg + "      I reg %06d"%iReg)
    print
    print("reg 0  %06d"%registers[0] + "      reg 5  %06d"%registers[5])
    print("reg 1  %06d"%registers[1] + "      reg 6  %06d"%registers[6])
    print("reg 2  %06d"%registers[2] + "      reg 7  %06d"%registers[7])
    print("reg 3  %06d"%registers[3] + "      reg 8  %06d"%registers[8])
    print("reg 4  %06d"%registers[4] + "      reg 9  %06d"%registers[9])

# initialization function
def init():
    global memory
    global registers
    global pReg
    memory = [0] * 1000
    registers = [0] * 10

    # write the program
    pReg = 100
    memory[100] = 031012
    memory[101] = 032013
    memory[102] = 051002
    

# add code here to read in assembly program
#  ... and store instructions in list of strings
init()

# add code here to iterate through the list,
#  executing them

while True:
    # get next instruction address
    iReg = pReg
    instr = memory[iReg]

    # decode the instruction
    op = dec.op(instr)
    mmm = dec.mmm(instr)
    r = dec.r(instr)
    s = dec.s(instr)

    # display state if debugging
    if debug == 1:
        print
        print(op)
        print(mmm)
        print(r)
        print(s)
        print

    # execute instruction and get next instruction address
    pReg = inst.arr[op](memory,registers,mmm,r,s,iReg)

    # display state if debugging
    if debug == 1:
        disp()

    # hack to make the program stop
    if pReg == -1:
        iReg = 0
        break

disp()

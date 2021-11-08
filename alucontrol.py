
'''
***************** ALU Control *******************

ALU requires control unit that is separate from main 
control unit. Main control unit defines alu_op as a 
function of type of instruction is being executed

'''
#%%
import myhdl 
from myhdl import block, always_comb
from definitions import *

@block
def alu_control(reset, instruction, alu_op, alu_decode):

    @always_comb
    def alucont():
        if reset.next == INACTIVE_HIGH:
            if alu_op == 2:
                if instruction[32:25] == 0:
                    if instruction[15:12] == 0:
                        alu_decode.next = ADD
                    elif instruction[15:12] == 1:
                        alu_decode.next = SLL
                    elif instruction[15:12] == 2:
                        alu_decode.next = SLT
                    elif instruction[15:12] == 3:
                        alu_decode.next = SLTU
                    elif instruction[15:12] == 4:
                        alu_decode.next = XOR
                    elif instruction[15:12] == 5:
                        alu_decode.next = SRL
                    elif instruction[15:12] == 6:
                        alu_decode.next = OR
                    elif instruction[15:12] == 7:
                        alu_decode.next = AND
                elif instruction[32:25] == 32:
                    if instruction[15:12] == 0:
                        alu_decode.next = SUB
                    elif instruction[15:12] == 5:
                        alu_decode.next = SRA
            elif alu_op == 0:
                alu_decode.next = ADD
            elif alu_op == 7:
                if instruction[15:12] == 0:
                    alu_decode.next = XOR

    return alucont
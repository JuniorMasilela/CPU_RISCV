
''''
****************** Control **********************

Instructions are categorized in different types to facilitate the control of operations 
The Data path for a specific instruction type is similar to support scalability. 

Once an instruction has been decoded, the next step is t configue control. 

RISCV defines bits[6:0], controlled by the control unit. 

- R-type :: Arithmetic + logic ops on registers 
- I-Type :: Arithmetic + Memory Load operations [ Based on data from instr + registers
- S-Type :: Store data operations [Based on data from instr + registers  
- SB-Type :: ncrement PC based on Jump or branch instruction

'''
#%%
from myhdl import block, always_comb, instance
from myhdl import Signal as signal
from definitions import *


@block
def ctrl(reset, opcode, branch, mem_rd, mem_to_reg, alu_op, mem_wr, alu_src, reg_wr):

    @always_comb
    def ctrl():

        if reset.next == INACTIVE_HIGH:

            # R Type 
            if opcode == RTYPE:
                alu_src.next = False
                mem_to_reg.next = False 
                reg_wr.next = True 
                mem_rd.next = False 
                mem_wr.next = False 
                branch.next = False
                alu_op.next = 2 

            # I Type
            elif opcode == ITYPE: 
                alu_src.next = True
                mem_to_reg.next = True 
                reg_wr.next = True 
                mem_rd.next = True 
                mem_wr.next = False 
                branch.next = False
                alu_op.next = 0

            elif opcode == STYPE: 
                alu_src.next = True
                mem_to_reg.next = False 
                reg_wr.next = False 
                mem_rd.next = False 
                mem_wr.next = True 
                branch.next = False
                alu_op.next = 0 

            elif opcode == JTYPE: 
                alu_src.next = False
                mem_to_reg.next = False 
                reg_wr.next = False 
                mem_rd.next = False 
                mem_wr.next = False 
                branch.next = True
                alu_op.next = 27
        
    return ctrl
        
# %%

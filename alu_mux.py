'''

ALU second input - Input Selection {MUX}: 

ALU input tends to be controlled by using the ALU Multiplexer. 
This requres that we store our values in the register file.
If the source is set then the data can be transferred to the ALU. 
'''
#%%
from myhdl import block, always_combo, _Signal
from definitions import *

@block 

def alu_mux(reset, im_gen, rdb, rdx, alu_src):

    @always_combo
    def almux():
        if reset.next == INACTIVE_HIGH: 
            if alu_src:
                rdx.next = im_gen
            else:
                rdx.next = rdb

    return almux
    
alu_mux.verilog_code
# %%

'''
*********** Python to Verilog conversion ************** 

One of the main utility funciton of using MyHDL is its ability 
    to easily convert python code to HDL's such as Verilog. 

'''

import alu, alu_mux, alucontrol, branch_taken, clock, control, wda_mux
import cpu_main, cpu_testbranch, cpu_top
import data_mem, instr_mem, imm_gen, jump_addr, reg_file
import decoder, definitions
import pc, pc_adder, pc_assign, pc_mux

# ALU conversion files - Verilog 
alu.convert(hdl='Verilog')
alu_mux.convert(hdl='Verilog')
alucontrol.convert(hdl='Verilog')

# Branch Taken.py conversion
branch_taken.convert(hdl='Verilog')

# Clock.py conversion 
clock.convert(hdl='Verilog')

# Control.py
control.convert(hdl='Verilog')

#CPU
cpu_top.convert(hdl='Verilog')
cpu_main.convert(hdl='Verilog')
cpu_testbranch.convert(hdl='Verilog')

# Data memory.py conversion 
data_mem.convert(hdl='Verilog')

# Instruction memory py conversion 
instr_mem.convert(hdl='Verilog')

# Decodeer py conversion 
decoder.convert(hdl='Verilog')

# Definitions py conversion 
definitions.convert(hdl='Verilog')

# Immediate generation py conversion 
imm_gen.convert(hdl='Verilog')

# Jump address py conversion 
jump_addr.convert(hdl='Verilog')

# Pc | adder | assign | Mux py conversion 
pc.convert(hdl='Verilog')
pc_adder.convert(hdl='Verilog')
pc_assign.convert(hdl='Verilog')
pc_mux.convert(hdl='Verilog')

# Register file py conversion 
reg_file.convert(hdl='Verilog')

# Wda MUX py conversion 
wda_mux.convert(hdl='Verilog')


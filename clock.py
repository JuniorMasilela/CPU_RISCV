# CLock
#
# Implements a fixed clock cycle that transitions very 10 ns (nanoseconds)from high to low or visa versa 
from myhdl import block,always, delay 
#%%
block

def clock(clk):
    @always(delay(10))
    def clck():
        clk.next = not clk 
    return clck 


# %%

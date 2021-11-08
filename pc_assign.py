

from myhdl import block, always, always_comb
from definitions import *

@block
def pc_assign(reset, read_addr, pc):

    @always_comb
    def assignment():
        if reset.next == INACTIVE_HIGH:
            read_addr.next = pc

    return assignment


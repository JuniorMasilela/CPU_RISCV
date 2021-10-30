# Program counter :: Selection MuX 
# Program Counter (PC) maintains a pointer or address index at instruction memory. CPU executes instruction that is stored on current PC register. 


from myhdl import block,always, always_comb

#Hardware component
#%%
@block
def pc_mux(reset, pc, pc_addr, jmp_addr, pc_sel):

    @always_comb
    def pmux():
        if reset.next == INACTIVE_HIGH:
            if pc_sel:
                pc.next = jmp_addr
            else:
                pc.next = pc_addr

    return pmux


# %%

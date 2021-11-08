'''
********************* Branch Taken ********************

The programs execution pointer oftens moves with respect to a logical decision 
When a condition is met, the execution pointer is transitioned to a specific 
function call. 

For XOR operation is used for decision making. 
    If all bits match --> 0 {Branch[taken]} 

This function is purposed to check if the the XOR result is zero. 
'''

#%%

from myhdl import block, always_comb

@block
def br_taken(result, brnch, pc_sel):

    @always_comb
    def taken():
        if ( not result) and (brnch):
            pc_sel.next = True
        else:
            pc_sel.next = False
            
    return taken 

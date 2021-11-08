from myhdl import block, always, always_comb, signal, intbv, c
import control, data_mem,instr_mem, alu, reg_file
import pc_adder, jump_addr,pc_mux, alu_mux, branch_taken
import wda_mux, alucontrol, imm_gen, pc_assign
from myhdl import instance, instances
from definitions import *

@block
def cpu_top(clk, reset):

    ra, rb, wa = [signal(intbv(0, min=0, max=(CPU_REGS - 1))) for _ in range(3)]
    wda, rda, rdb, rdx = [signal(intbv(0)[CPU_BITS:]) for _ in range(4)]
    alu_op = signal(intbv(0)[CPU_ALUW:])
    brnch, mem_rd, mem_to_rgs, mem_wr, alu_src, reg_wr = [signal(intbv(0)[1:]) for _ in range(6)]
    opcode = signal(intbv(0)[7:])
    result, read_data, pc, shl = [signal(intbv(0)[CPU_BITS:]) for _ in range(4)]
    pc_sel = signal(intbv(0)[1:])
    im_gen = signal(intbv(0)[CPU_BITS:])
    alu_decode = signal(intbv(0)[4:])

    step = signal(intbv(0)[1:])

    read_addr, instruction, pc_addr, jmp_addr = [signal(intbv(0)[CPU_BITS:]) for _ in range(4)]

    cont = control(reset, opcode, brnch, mem_rd, mem_to_rgs, alu_op, mem_wr, alu_src, reg_wr)
    dmem = data_mem(reset, clk, result, mem_wr, mem_rd, rdb, read_data)
    imem = instr_mem(reset, read_addr, instruction, ra, rb, wa, opcode)
    alux = alu(reset, alu_decode, rda, rdx, result)
    regf = reg_file(reset, clk, ra, rb, wa, wda, reg_wr, rda, rdb)
    padr = pc_adder(reset, step, pc, pc_addr)
    jadr = jump_addr(reset, read_addr, shl, jmp_addr)
    pcmx = pc_mux(reset, pc, pc_addr, jmp_addr, pc_sel)
    almx = alu_mux(reset, im_gen, rdb, rdx, alu_src)
    wdmx = wda_mux(reset, wda, mem_to_rgs, result, read_data)
    aluc = alucontrol(reset, instruction, alu_op, alu_decode)
    imgn = imm_gen(reset, instruction, im_gen)
    nxpc = pc_assign(reset, read_addr, pc)
    tken = branch_taken(result, brnch, pc_sel)

    @always(step.posedge)
    def cpu():
        if pc == 0:
            pc.next += 1

    @instance
    def event():
        idle = 7
        while True:
            for i in range(idle):
                yield clk.posedge
            if reset.next == INACTIVE_HIGH:
                step.next = not step
                idle = 3

    return instances()
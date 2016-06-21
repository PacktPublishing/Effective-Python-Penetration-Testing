from capstone import *
import pefile
pe = pefile.PE('md5sum.exe')

entryPoint = pe.OPTIONAL_HEADER.AddressOfEntryPoint
data = pe.get_memory_mapped_image()[entryPoint:]

cs = Cs(CS_ARCH_X86, CS_MODE_32)


for i in cs.disasm(data, 0x1000):
    print("0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str))



class CPU:
    # REGISTERS GO BELOW

    # The general purpose registers are below 16bit
    R0 = 0x0000
    R1 = 0x0000
    R2 = 0x0000
    R3 = 0x0000
    R4 = 0x0000
    R5 = 0x0000
    R6 = 0x0000
    R7 = 0x0000

    # Special Registers
    IP = 0x0000
    # stack pointer starts here so it has from 0xFF00 to 0xFFFF (256bytes) going downward. 0x0000 at the top and 0xFFFF at the bottom
    SP = 0xFF00

    # put flags as a class to make it a bit neater

    class FLAGS:
        Z = False   #Zero
        N = False   #Negative
        C = False   #Carry
        O = False   #Overflow

    # will need this later to control stopping/starting but just declaring for now
    HALT = False


#64 kb memory as 8bit
mem = bytearray(0xFFFF)




#declaring opcode self explanatory
opcode = mem[CPU.IP]


def reg_conv(value):
    if value == 0x000:
        return "R0"
    elif value == 0x01:
        return "R1"
    elif value == 0x02:
        return "R2"
    elif value == 0x03:
        return "R3"
    elif value == 0x04:
        return "R4"
    elif value == 0x05:
        return "R5"
    elif value == 0x06:
        return "R6"
    elif value == 0x07:
        return "R7"


#instruction set
while CPU.HALT == False:
    
    
    if opcode == 0x00:  #NOP do nothing
        CPU.IP += 0x0001

    elif opcode == 0x01:  #HALT stops execution
        CPU.HALT = True
        CPU.IP += 0x0001
    #MOV_REG_IMM move 16 bit immidiate value into a register
    elif opcode == 0x02:
        dest = reg_conv(mem[CPU.IP + 1])
        lo = mem[CPU.IP + 2]
        hi = mem[CPU.IP + 3]
        combined = (hi << 8) + lo     #shifts the hi value 8 binary bits to the left and adds the lo value to make the 16bit value from two 8 bits
        setattr(CPU, dest, combined)
        IP += 0x0004
    elif opcode == 0x03: #MOV_REG_REG takes a register as a destination and then takes another register and then copies the second registers contents into the first
        dest = reg_conv(mem[CPU.IP + 1])
        source = reg_conv(mem[CPU.IP + 2])
        source_name = getattr(CPU, source)
        setattr(CPU, dest, source_name)
       
        
        
        
        
        
        
        


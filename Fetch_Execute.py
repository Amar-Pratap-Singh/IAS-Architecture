from math import *
from IAS import *     
from Conversion import *

# Checking Left and right instructions
# Decoding opcodes
# Performing corresponding functions

class Fetch_Execute:
        
    def __init__(self, Memory, PC):
        self.PC = PC
        self.Memory = Memory
        self.ias = IAS(Memory, PC)
        
    def fetch_execute(self):
        ignore_left_instruct = False
        
        while True:                
            self.ias.MAR = self.ias.PC
            self.ias.MBR = self.ias.Memory[self.ias.MAR]
            L_instruc = self.ias.MBR[0:20]
            R_instruc = self.ias.MBR[20:40]

            print("\n\nPC = ", self.ias.PC)
            
            if (L_instruc == " "*20 or ignore_left_instruct):
                #Fetch
                self.ias.IR = R_instruc[0:8]
                self.ias.MAR = R_instruc[8:20]
 
                #Decode and Execute
                if (self.ias.IR == "00001010"):
                    self.ias.LOAD_MQ_AC(Binary_to_Decimal(self.ias.MQ))

                elif (self.ias.IR == "00001001"):
                    self.ias.LOAD_X_MQ(Binary_to_Decimal(self.ias.MAR))  

                elif (self.ias.IR == "00000001"):
                    self.ias.LOAD_X_AC(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00000010"):
                    self.ias.LOAD_minus_X_AC(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00000011"):
                    self.ias.LOAD_abs_X_AC(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00000100"):
                    self.ias.LOAD_abs_minus_X_AC(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00100001"):
                    self.ias.STOR(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00001101"):
                    self.ias.JUMP_left(Binary_to_Decimal(self.ias.MAR))
                    print("\nJUMP INSTRUCTION FOUND, JUMP TO PC = ", self.ias.PC)
                    continue

                elif (self.ias.IR == "00001110"):
                    self.ias.JUMP_right(Binary_to_Decimal(self.ias.MAR))
                    ignore_left_instruct = True

                    print("\nJUMP INSTRUCTION FOUND, JUMP TO PC = ", self.ias.PC)
                    continue

                elif (self.ias.IR == "00001111"):
                    jumped = self.ias.Cond_Jump_left(Binary_to_Decimal(self.ias.MAR))
                    if (jumped):
                        print("\nJUMP INSTRUCTION FOUND, JUMP TO PC = ", self.ias.PC)
                        continue

                elif (self.ias.IR == "00010000"): 
                    jumped = self.ias.Cond_Jump_right(Binary_to_Decimal(self.ias.MAR))
                    ignore_left_instruct = jumped
                    if (jumped):
                        print("\nJUMP INSTRUCTION FOUND, JUMP TO PC = ", self.ias.PC)
                        continue

                elif (self.ias.IR == "00000101"):
                    self.ias.ADD_X_AC(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00000111"):
                    self.ias.ADD_abs(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00000110"):
                    self.ias.SUB_AC_MX(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00001000"):
                    self.ias.SUB_abs(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00001100"):
                    self.ias.DIV_MX(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00010100"):
                    self.ias.LSH()

                elif (self.ias.IR == "00010101"):
                    self.ias.RSH()

                elif (self.ias.IR == "00000000"):
                    print("Right: IR = ", self.ias.IR, ", MAR = ", self.ias.MAR, ", MBR = ", self.ias.MBR, ", AC = ",self.ias.AC)
                    print("Program Halted!")
                    break
                
                else:
                    print("Opcode: ",self.ias.IR," not understood")
                    continue
                
                print("Right: IR = ", self.ias.IR, ", MAR = ", self.ias.MAR, ", MBR = ", self.ias.MBR, ", AC = ",self.ias.AC)

            else:

                #Fetch
                self.ias.IR = L_instruc[0:8]
                self.ias.MAR = L_instruc[8:20]
    
                #Decode and Execute
                if (self.ias.IR == "00001010"):
                    self.ias.LOAD_MQ_AC(self.ias.MQ)

                elif (self.ias.IR == "00001001"):
                    self.ias.LOAD_X_MQ(Binary_to_Decimal(self.ias.MAR))  

                elif (self.ias.IR == "00000001"):
                    self.ias.LOAD_X_AC(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00000010"):
                    self.ias.LOAD_minus_X_AC(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00000011"):
                    self.ias.LOAD_abs_X_AC(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00000100"):
                    self.ias.LOAD_abs_minus_X_AC(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00100001"):
                    self.ias.STOR(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00001101"):
                    self.ias.JUMP_left(Binary_to_Decimal(self.ias.MAR))
                    print("\nJUMP ENCOUNTERED, NEW PC = ", self.ias.PC)
                    continue

                elif (self.ias.IR == "00001110"):
                    self.ias.JUMP_right(Binary_to_Decimal(self.ias.MAR))
                    ignore_left_instruct = True

                    print("\nJUMP ENCOUNTERED, NEW PC = ", self.ias.PC)
                    continue

                elif (self.ias.IR == "00001111"):
                    jumped = self.ias.Cond_Jump_left(Binary_to_Decimal(self.ias.MAR))
                    if (jumped):
                        print("\nJUMP ENCOUNTERED, NEW PC = ", self.ias.PC)
                        continue

                elif (self.ias.IR == "00010000"): 
                    jumped = self.ias.Cond_Jump_right(Binary_to_Decimal(self.ias.MAR))
                    ignore_left_instruct = jumped
                    if (jumped):
                        print("\nJUMP ENCOUNTERED, NEW PC = ", self.ias.PC)
                        continue
                    
                elif (self.ias.IR == "00000101"):
                    self.ias.ADD_X_AC(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00000111"):
                    self.ias.ADD_abs(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00000110"):
                    self.ias.SUB_AC_MX(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00001000"):
                    self.ias.SUB_abs(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00001100"):
                    self.ias.DIV_MX(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00010100"):
                    self.ias.LSH()

                elif (self.ias.IR == "00010101"):
                    self.ias.RSH()

                elif (self.ias.IR == "00000000"):
                    print("Left : IR = ", self.ias.IR, ", MAR = ", self.ias.MAR, ", MBR = ", self.ias.MBR, ", AC = ", self.ias.AC)
                    print("Program Halted!")
                    break

                else:
                    print("Opcode: ",self.ias.IR," not understood")
                    continue
                
                print("Left : IR = ", self.ias.IR, ", MAR = ", self.ias.MAR, ", MBR = ", self.ias.MBR, ", AC = ", self.ias.AC)

                #Fetch
                self.ias.IR = R_instruc[0:8]
                self.ias.MAR = R_instruc[8:20]

                #Decode and Execute
                if (self.ias.IR == "00001010"):
                    self.ias.LOAD_MQ_AC(Binary_to_Decimal(self.ias.MQ))

                elif (self.ias.IR == "00001001"):
                    self.ias.LOAD_X_MQ(Binary_to_Decimal(self.ias.MAR))  

                elif (self.ias.IR == "00000001"):
                    self.ias.LOAD_X_AC(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00000010"):
                    self.ias.LOAD_minus_X_AC(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00000011"):
                    self.ias.LOAD_abs_X_AC(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00000100"):
                    self.ias.LOAD_abs_minus_X_AC(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00100001"):
                    self.ias.STOR(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00001101"):
                    self.ias.JUMP_left(Binary_to_Decimal(self.ias.MAR))
                    print("\nJUMP INSTRUCTION FOUND, JUMP TO PC = ", self.ias.PC)
                    continue

                elif (self.ias.IR == "00001110"):
                    self.ias.JUMP_right(Binary_to_Decimal(self.ias.MAR))
                    ignore_left_instruct = True

                    print("\nJUMP INSTRUCTION FOUND, JUMP TO PC = ", self.ias.PC)
                    continue

                elif (self.ias.IR == "00001111"):
                    jumped = self.ias.Cond_Jump_left(Binary_to_Decimal(self.ias.MAR))
                    if (jumped):
                        print("\nJUMP INSTRUCTION FOUND, JUMP TO PC = ", self.ias.PC)
                        continue

                elif (self.ias.IR == "00010000"): 
                    jumped = self.ias.Cond_Jump_right(Binary_to_Decimal(self.ias.MAR))
                    ignore_left_instruct = jumped
                    if (jumped):
                        print("\nJUMP INSTRUCTION FOUND, JUMP TO PC = ", self.ias.PC)
                        continue
                    
                elif (self.ias.IR == "00000101"):
                    self.ias.ADD_X_AC(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00000111"):
                    self.ias.ADD_abs(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00000110"):
                    self.ias.SUB_AC_MX(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00001000"):
                    self.ias.SUB_abs(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00001100"):
                    self.ias.DIV_MX(Binary_to_Decimal(self.ias.MAR))

                elif (self.ias.IR == "00010100"):
                    self.ias.LSH()

                elif (self.ias.IR == "00010101"):
                    self.ias.RSH()

                elif (self.ias.IR == "00000000"):
                    print("Right: IR = ", self.ias.IR, ", MAR = ", self.ias.MAR, ", MBR = ", self.ias.MBR, ", AC = ", self.ias.AC)
                    print("Program Halted!")
                    break

                else:
                    print("Opcode: ",self.ias.IR," not understood")  
                    continue

                print("Right: IR = ", self.ias.IR, ", MAR = ", self.ias.MAR, ", MBR = ", self.ias.MBR, ", AC = ", self.ias.AC)
            
            self.ias.PC = self.ias.PC + 1
            
from math import *
from Conversion import *

# Most of the functions of the IAS computer
class IAS:
    MAR = ""
    MBR = ""
    IBR = ""
    IR = ""
    AC = ""
    MQ = ""

    def __init__(self, Memory, PC):
        self.Memory = Memory
        self.PC = PC
    
    def LOAD_MQ_AC(self, MQ):
        IAS.AC = MQ
        
    def LOAD_X_MQ(self, X):
        IAS.MQ = self.Memory[X]
    
    def STOR(self, X):
        self.Memory[X] = IAS.AC
    
    def LOAD_X_AC(self, X):
        IAS.AC = self.Memory[X]

    def LOAD_minus_X_AC(self, X):
        if (self.Memory[X])[0] == "0":
            IAS.AC = "1" + (self.Memory[X])[1:len(self.Memory[X])]

        else:
            IAS.AC = "0" + (self.Memory[X])[1:len(self.Memory[X])]


    def LOAD_abs_X_AC(self, X):
        IAS.AC = "0" + (self.Memory[X])[1:len(self.Memory[X])]
    
    def LOAD_abs_minus_X_AC(self, X):
        # If memory[x] is 0, then it will remain 0
        if (Binary_to_Decimal(self.Memory[X]) == 0): 
            AC = "0" + (self.Memory[X])[1: len(self.Memory[X])]
        else:
            AC = "1" + (self.Memory[X])[1:len(self.Memory[X])]

    def JUMP_left(self, X):
        self.PC = X

    def JUMP_right(self, X):  # Jump to the right instruction
        self.PC = X
    
    def Cond_Jump_left(self, X):
        if (IAS.AC[0] == "0"):
            self.PC = X
            return True
        else:
            return False
    
    def Cond_Jump_right(self, X):
        if (IAS.AC[0] == "0"):
            self.PC = X
            return True
        else:
            return False
    
    def ADD_X_AC(self, X):
        signAC = 1
        signMX = 1

        if (IAS.AC[0] == "1"): 
            signAC = -1
        if ((self.Memory[X])[0] == "1"):
            signMX = -1
        
        AC_value = Binary_to_Decimal(IAS.AC[1: len(IAS.AC)])
        MX_value = Binary_to_Decimal((self.Memory[X])[1:len(self.Memory[X])])

        ans = AC_value*signAC + MX_value*signMX

        if ans < 0:
            IAS.AC = "1" + Decimal_to_Binary(abs(ans))

        else:
            IAS.AC = "0" + Decimal_to_Binary(ans)


    def ADD_abs(self, X):
        signAC = 1
        if (IAS.AC[0] == "1"):
            signAC = -1

        AC_value = Binary_to_Decimal(IAS.AC[1: len(IAS.AC)])
        MX_value = Binary_to_Decimal((self.Memory[X])[1:len(self.Memory[X])])
        ans = AC_value*signAC + MX_value

        if ans < 0:
            IAS.AC = "1" + Decimal_to_Binary(abs(ans))

        else:
            IAS.AC = "0" + Decimal_to_Binary(ans)


    def SUB_AC_MX(self, X):
        signAC = 1
        signMX = 1

        if (IAS.AC[0] == "1"): 
            signAC = -1
        if ((self.Memory[X])[0] == "1"):
            signMX = -1
        
        AC_value = Binary_to_Decimal(IAS.AC[1: len(IAS.AC)])
        # Data in the memory-> size = 40 bits?
        MX_value = Binary_to_Decimal((self.Memory[X])[1:len(self.Memory[X])])

        ans = AC_value*signAC - MX_value*signMX

        if ans < 0:
            IAS.AC = "1" + Decimal_to_Binary(abs(ans))

        else:
            IAS.AC = "0" + Decimal_to_Binary(ans)


    def SUB_abs(self, X):
        # AC - |M(X)|
        signAC = 1
        if (IAS.AC[0] == "1"):
            signAC = -1

        AC_value = Binary_to_Decimal(IAS.AC[1: len(IAS.AC)])
        MX_value = Binary_to_Decimal((self.Memory[X])[1:len(self.Memory[X])])
        ans = AC_value*signAC - MX_value

        if ans < 0:
            IAS.AC = "1" + Decimal_to_Binary(abs(ans))

        else:
            IAS.AC = "0" + Decimal_to_Binary(ans)


    #we have assumed the case of negative remainder

    def DIV_MX(self, X):
        signAC = 1
        signMX = 1

        if (IAS.AC[0] == "1"): signAC = -1
        if ((self.Memory[X])[0] == "1"): signMX = -1

        AC_value = Binary_to_Decimal(IAS.AC[1: len(IAS.AC)])
        MX_value = Binary_to_Decimal((self.Memory[X])[1 : 40]) 

        ac_to_be_stored = (signAC*AC_value) % (signMX*MX_value)
        mq_to_be_stored = (signAC*AC_value)//(signMX*MX_value)

        if (ac_to_be_stored > 0):
            IAS.AC = "0" + Decimal_to_Binary(ac_to_be_stored)
        else:
            IAS.AC = "1" + Decimal_to_Binary(abs(ac_to_be_stored))

        if (mq_to_be_stored > 0):
            IAS.MQ =  "0" + Decimal_to_Binary(mq_to_be_stored) 

        else:
            IAS.MQ =  "1" + Decimal_to_Binary(abs(mq_to_be_stored)) 

    
    def LSH(self):
        signAC = 1

        if (IAS.AC[0] == "1"): signAC = -1
        AC_value = Binary_to_Decimal(IAS.AC[1 : len(IAS.AC)])
        ac_to_be_stored = AC_value* 2 * signAC

        if (ac_to_be_stored > 0):
            IAS.AC = "0" + Decimal_to_Binary(ac_to_be_stored)
        
        else:
            IAS.AC = "1" + Decimal_to_Binary(abs(ac_to_be_stored))


    def RSH(self):
        signAC = 1

        if (IAS.AC[0] == "1"): signAC = -1
        AC_value = Binary_to_Decimal(IAS.AC[1 : len(IAS.AC)])
        ac_to_be_stored = (AC_value//2)*signAC

        if (ac_to_be_stored > 0):
            IAS.AC = "0" + Decimal_to_Binary(ac_to_be_stored)
        
        else:
            IAS.AC = "1" + Decimal_to_Binary(abs(ac_to_be_stored))


#We can also implement the address modification STOR, but not for now

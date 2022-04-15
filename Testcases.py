# sign-magnitude format
# The msb (most significant bit) is 0 means number is positive
# The msb (most significant bit) is 1 means number is negative

from Fetch_Execute import *
from IAS import *

#*********************TESTCASE-1**************************#
# Given two numbers
# Find whether the bigger of them is the square of the smaller one
# Smaller number should be stored in Memory[1] and bigger in Memory[0]
# Program returns "YES" or "NO" as the answer

print("TESTCASE-1\n")
Memory = [" "]*30

Memory[0] = "001" #7
Memory[1] = "011"  #3 
# Memory[2] to store the result of some operation
# Memory[3] to store the final result
Memory[4] = "00" #0
Memory[5] = "01" #1
Memory[6] = "0000000100000000000000001100000000000001" # LOAD M(0) to AC, DIV AC by M(1)
Memory[7] = "0000101000000000000000000110000000000001" # LOAD MQ to AC, SUB M(1) from AC
Memory[8] = "0010000100000000001000000100000000000010" # STOR AC into M(2), LOAD -|M(2)| to AC
Memory[9] = "                    00001111000000001100" # NULL, CONDITIONAL JUMP: JUMP + M(12, 0:19)
Memory[10] = "0000000100000000010000100001000000000011" # LOAD M(4) into AC, STOR AC into M(3)
Memory[11] = "0000000000000000000000000000000000000000" # HALT, HALT
Memory[12] = "0000000100000000010100100001000000000011" # LOAD M(5) into AC, STOR AC into M(3)
Memory[13] = "0000000000000000000000000000000000000000" # HALT, HALT

PC = 6
Fetch_Execute(Memory, PC).fetch_execute()
print("\nIs bigger number square of smaller number: ", end = " ")

if (Binary_to_Decimal(Memory[3]) == 1):
    print("YES")
else:
    print("NO")




#****************************TESTCASE-2**********************************#
# Given two numbers
# This program checks if both of them are equal are not
# If equal, then prints difference of them in the order they are given, else prints their sum

print("\n\nTESTCASE-2\n")
Memory2 = [" "]*30

Memory2[0] = "01111"  #1
Memory2[1] = "01111"  #15
# Memory2[2] to store result of some local operation
# Memory2[3] to store the value of result
Memory2[4] = "0000000100000000000000000110000000000001"  # LOAD M(0) to AC, SUB M(1) from AC
Memory2[5] = "0010000100000000001000000100000000000010"  # STOR AC into M(2) -> a-b, LOAD -|M(2)| to AC
Memory2[6] = "                    00001111000000001010"  # NULL, CONDITIONAL JUMP: JUMP + M(10, 0:19)
Memory2[7] = "0000000100000000000000000101000000000001"  # LOAD M(0) to AC, ADD M(1) to AC
Memory2[8] = "                    00100001000000000011"  # NULL, STOR AC into M(3) -> a+b
Memory2[9] = "0000000000000000000000000000000000000000"  # HALT, HALT
Memory2[10] = "0000000100000000001000100001000000000011" # LOAD M(2) -> a-b to AC, STOR AC into M(3)
Memory2[11] = "0000000000000000000000000000000000000000" # HALT, HALT

PC2 = 4 

Fetch_Execute(Memory2, PC2).fetch_execute()
print("\nRESULT: ", Binary_to_Decimal(Memory2[3]))
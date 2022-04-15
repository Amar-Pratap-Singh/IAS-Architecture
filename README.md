# IAS-Architecture

___________________________________________________________________________
Code files brief description
___________________________________________________________________________

The entire code is distributed over 4 files.

1. Conversion.py   
    # Contains only two functions- Binary_to_Decimal() and Decimal_to_Binary()  
    # These two functions are used very frequently in rest of the code

2. IAS.py
    # This python file can be thought of as the "brain of the code".
    # This python file contains all(most of) the functions which are defined in the Princeton Architecture or in the IAS computer
    # These functions are actually methods defined under a class to make it modular.

3. Fetch_Execute.py
    # This python file contains a method "fetch_execute()" which is the "heart of this code."
    # The method:
        # checks for the left and right instructions and take appropriate action, in every possible case. 
        # decodes the opcode
        # call the specified function (functions which are defined in IAS.py) for the opcode

    # All the operations (in second point) are done with the help of a single instance of the class, defined in IAS.py

4. Testcases.py
    # This consists of MACHINE LEVEL LANGUAGE CODE
    # It feeds the "Fetch_Execute.py" file by giving inputs
    

________________________________________________________________________________
HOW TO RUN THE CODE?
________________________________________________________________________________

# NO EXTRA LIBRARY of python is required.
# Make sure all the python files are in the same directory.
# Run "Testcases.py" file.
# Get the expected Output:)
# The default value given to some variable in the "Testcases.py" can be changed to any legal value.
# Remember the binary numbers used in whole of the code follows "sign-magnitude format".

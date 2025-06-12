# OLang
## Installation:
1. Run the setup.bat file on your computer.
2. Click "Yes" if a pop-up appears asking for administrator permissions.
3. After installation, restart your computer.

## Creating a program using OLang:
1. Create a file on your computer with an .o extension.
2. Edit a file in a text editor and add your OLang code there.
3. Run OLang file by double-clicking the file.

## Language syntax:
| Statements |

print - Prints a text
    PARAMS: TEXT: str, *_VARS[]: str[]
    - print TEXT
    - print Variable t = _t
nl - Prints a newline
    PARAMS: *NUMBER: number | _NAME (variable name): str
    / Print one newline /
    - nl
    / Print multiple newlines /
    - nl NUMBER
var - Interacts with a variable
    PARAMS: NAME: str, OPERANT: str, *VALUE: number | _NAME (variable name): str
    / Assigning a variable /
    - var NAME = VALUE
    / Operations on variable /
    - var NAME += VALUE
    - var NAME -= VALUE
    - var NAME *= VALUE
    - var NAME /= VALUE
    - var NAME //= VALUE
    - var NAME **= VALUE
    - var NAME %= VALUE
    / Printing a variable specification /
    - var NAME =>
    / Setting a keyboard input as a variable value /
    - var NAME =<
    / Storing a random value from 0 to 1
    - var NAME =?
    / Flooring the value in a variable
    - var NAME \=
    / Ceiling the value in a variable
    - var NAME =\
    / Rounding the value in a variable
    - var NAME \
    / Convert a variable into an intiger /
    - var NAME =i
    / Convert a variable into a float /
    - var NAME =f
    / Conver a variable into a string /
    - var NAME =s
if - If the statement is false, no action up until endif will be executed
    PARAMS: STATEMENTS[] (connectors: || - or, && - and, /\ - xor)
    - if _t > 2
    - if _t <= 2
    - if _t == _t2
    / If at least one statement is correct, the code inside will execute /
    - if 2 < _t || _t == 0
    / If all statements are correct, the code inside will execute
    - if 7 > _t && 9 < _t
    / If only one statement is correct, the code instide will execute /
    - if _t < 5 /\ _t > 7
endif - The end of if structure
    - endif
wait - Wait a given amount of seconds before the next action
    PARAMS: seconds: int
    - wait 5
    - wait 3600
return - Stops the execution of the program
    PARAMS: *code: int
    - return
    - return 0
    - return 6
# - One line long comment
    - # This is a comment

--------------------------------------
* - optional param

| Status codes |

0: "No error"
    - Code ended without any errors
1: "Syntax error"
    - The line might have a typo
    - The statement does not have required params
2: "Type error"
    - Cannot use this type for a specific calucation
    - Cannot compare strings or strings with numbers
3: "Math error"
    - Cannot divide by 0
    - Cannot calculate a modulo d where d equals 0
4: "Variable name error"
    - The variable name is reserved
    - The variable name is too long
    - The variable name contains _
5: "Variable assign error"
    - Could not assign the variable
6: "Variable not defined"
    - The variable does not exist
    - The variable was called before declaration
7: "Unexpected endif"
    - Encountered endif which is not connected to a if statement
8: "Structural error"
    - Function does not have a return statement
    - Main does not have a return statement

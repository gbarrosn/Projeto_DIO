# Compound interest calculator
#### Video Demo:  <URL HERE>
#### Description:
It is really hard to decide what to do in the final project, specially with so many ideas in my mind. 
    
So i've decided to build a compound interest calculator, inspired by some research about the topic when studying for an exam to work at a bank. The core concept of it isn't just to calculate the values and showing it, but the possibility to simulate various situations, and also being able to record the simulatons in a csv file, witch is lightweight and portable. The code in python can be adapted to work at a website backend or just be used in the command line, as a simple, fast and practical tool.

The usage is: " python3 compound_interest.py"

The user then gets promted for a starting value, in integers, then the fee tax, in floating point, then the number of periods to calculate, in integer value, then y/n questons about details of the deposits, and the csv file.

Explanation of the code:

    The first section of the code lines 3 to 37 are declarations of some functions, yn_choice prompts the classic Y/n option in the terminal, truncate, that truncates a float to a determined number of decimal places, get_int and get_float are inspired by the ones in the cs50's library. 

        Usage of the functions:

            yn_choice(message, default)
                Message being the message that is going to be prompted, and the default value should not be changed.

            truncate(number, number of decimal places)
                truncates floats without rounding

            get_int and get_float (message, error message)
                inspired by the course's functions, asks for an integer os float prompting a message, and if the value isn't validated, prompts the error message and reprompts for input
    
    After the first section, the user gets prompted for the initial value, the fees per period, and the nu,ber of periods, some variables are declared, then the option to record the csv file is asked, if yes, the user gets pompted to insert the name of the file., and the program asks if the user will make month deposits, and if they will be the same every month. If yes, user inputs the fixed amount, if not, the user will have to input the value each period.

        The code computes the value period by period, writing the file as it goes, preventing it from lots of RAM consumption.

        at the end of the block, the file closes, saving it's content, and preventing memory leaks.

    The last section runs if the user won't record the files in a csv file, just prompting in the terminal the values.
    


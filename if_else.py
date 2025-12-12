"""
Conditional flow
Only execute certain parts of the code when the conditions
you define have been met.
"""

# This is how to read a number from a user and store it into input_number
input_string = input("Please enter a number: ")  # read from the command line
input_number = int(input_string)  # convert the text entered into a number

# This is how to trigger a piece of code to execute only when a condition is met
if input_number == 100:
    # the number is exactly equal to 100
    print("This number is exactly 100")
elif input_number < 100 and input_number >= 95:
    # when the 1st condition fails, the next one is checked
    # you can chain conditions together with words 'and' and 'or'
    print("This number is greater than 95")
else:
    # None of the conditions have been met
    print("This doesn't meet any of my criteria")

"""
Other possible conditions: 
> greater than
>= greater than or equal to
< less than
<= less than or equal to
!= not equal to
"""

"""
The problem:
Ask the user to enter a number between 1 and 100.
If the number entered is outside this range, tell them to stop being so edgy.
If the number is in a range 5 above or below 50, print out 'pretty good number'.
If the number is exactly 22, print out 'you found the secret number'.
Otherwise, print out 'thanks for trying'
"""

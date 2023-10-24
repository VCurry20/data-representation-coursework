# Assignment 04

# Write a program in python that will read a file from a repository
# The program should then replace all instances of the text "Andrew" with my name
# The program should then commit throse changes and push the fail back to the repository



















# Question 3
# Write a function which takes in a string and replaces all occurrences of 'e' with '*' and returns the resulting string

def replace_char(string):
    new_str = ""
    for c in string:
        if c ==  "e":
            new_str += "*"
        else:
            new_str += c
    return new_str


print(replace_char("veronica"))
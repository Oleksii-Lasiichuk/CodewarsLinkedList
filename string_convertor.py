""" 
in the excersize you gave the list of all problems, but they are too long -
and also are using empty spaces between words so i made a program that 
converts it to normal title for a folder
"""


def convert(string: str) -> str:
    result = ''.join([ el.lower() if el.isalpha() else '_' for el in string])
    return result

string_to_convert = 'Can you get the loop?'

print(convert(string_to_convert))

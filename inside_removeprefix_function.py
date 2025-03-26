#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function 
# parameter. Create a program that do the same functionality without using removeprefix() function.

#ask user for a string and the letters the user wants to remove

string = input('Please enter a string: ')

remove_letter = input('From the beginning, what letter/s would you like to remove?: ')

#check in the letter is in the string and use lstrip function

try:
    print(string.lstrip(remove_letter))
    
except:
    print(f'{remove_letter} is not in {string}')
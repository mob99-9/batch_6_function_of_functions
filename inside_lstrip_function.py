#Prog01. lstrip() remove the space characters at the beginning of the string. 
# Create a program that do the same functionality without using lstrip() function.

#ask user for a string

string = input('Please enter a string with spaces at the beginning: ')

#use split and join function on a new string with the given string

new_string = string.split()
new_string = " ".join(new_string)

#print string

print (new_string)
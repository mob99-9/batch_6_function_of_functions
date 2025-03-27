#Prog04. isupper() check if all characters of the string is on upper case. 
#Create a program that do the same functionality without using isupper() function.

#create a lists of upper case letters

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", 
            "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

#ask user to enter a string

user_string = input("Please enter a string: ")

#have a isupper variable

upper = False

#check each letter in user string if it is upper cased.

for letter in user_string:
    if letter in alphabet:
        upper = True
    elif letter == " ":
        None
    elif letter not in alphabet:
        upper = False

#print upper variable

print(upper)
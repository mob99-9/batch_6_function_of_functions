#Prog08. swapcase() reverse the casing of each of the character of the string. 
#Create a program that do the same functionality without using swapcase() function.
#Prog09. swapcase() reverse the casing of each of the character of the string. 
##Create a program that do the same functionality without using swapcase() function.

#ask user for a string 

user_string = input("Please enter a string: ")

#create another variable for the new string

swapcased_string = ""

#check every character in string and change casing

for char in user_string:
    if char.islower():
        swapcased_string += char.upper()
    elif char.isupper()== True:
        swapcased_string += char.lower()
    else:
        swapcased_string += char

#print the new string string

print(swapcased_string)
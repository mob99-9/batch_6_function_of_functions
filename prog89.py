#Prog08. swapcase() reverse the casing of each of the character of the string. 
#Create a program that do the same functionality without using swapcase() function.
#Prog09. swapcase() reverse the casing of each of the character of the string. 
##Create a program that do the same functionality without using swapcase() function.

#ask user for a string 

user_string = input("Please enter a string: ")

#check every character in string and change casing

for char in user_string:
    if char.islower()== True:
        letter_location = user_string.index(char)
        user_string = user_string.replace(char, user_string[letter_location].upper())
    elif char.isupper()== True:
        location_letter = user_string.index(char)
        user_string = user_string.replace(char, user_string[letter_location].lower())
    else:
        None

#print user string

print(user_string)
#Prog03. lower() converts all characters of the string into lower case. 
#Create a program that do the same functionality without using lower() function.

#create list for alphabets
letters = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j",
           "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "R", "r", "S", "s", "T", "t", 
           "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"] 

#ask user for a string
user_string = input("Please input a string in random casing: ")

#check each character if its upper case and replace it
for char in user_string:
    if char.islower() == True:
        None
    elif char == " ":
        None
    elif char.isupper() == True:
        letter = letters.index(char)
        user_string = user_string.replace(char, letters[letter + 1])
    else: 
        None

#print the string
print(user_string)
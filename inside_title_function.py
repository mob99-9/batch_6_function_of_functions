#Prog10. title() makes all first letter of each word in the string, capital letter. 
# And all other letter in small case. Create a program that do the same functionality without
#  using title() function.

#ask user for a string and create empty string

user_string = input("Please enter a string: ")

new_string = ""

#split the string by spaces

user_string = user_string.split(" ")

#capitalize every word in the string

for word in user_string:
    new_string += word.capitalize()
    new_string += " "

#print the new string

print(new_string)

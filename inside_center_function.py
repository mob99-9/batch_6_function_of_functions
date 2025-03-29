#Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center.
#Create a program that do the same functionality without using center() function.

#ask user for a string

user_string = input("Please enter a string: ")

#set center function for the user

padding = input("What padding would you like to use?: ")

lenght = input("How many characters would you like to input?: ")

#use algebra to get center function

center = padding * int(lenght)

#print user string with the center on both sides

print(center, user_string, center)
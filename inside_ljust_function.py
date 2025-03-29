#Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. 
#Create a program that do the same functionality without using ljust() function.

#ask user for a string

user_string = input("Please enter a string: ")

#set ljust function for the user

padding = input("What padding would you like to use?: ")

lenght = input("How many characters would you like to input?: ")

#use algebra to get ljust function

ljust = padding * int(lenght)

#print user string with the ljust variable

print(ljust, user_string)
#Prog05. endswith() check if the string end part matches the function parameter. 
#Create a program that do the same functionality without using endswith() function.

#ask user for a string

user_string = input("user_string = ")

#have a endswith variable 

endswith = input("user_string.endswith(): ")

#use rstrip to check if endswith is in user_string

try:
    user_string = user_string.rstrip(endswith)
    print(True)
except:
    print(False)
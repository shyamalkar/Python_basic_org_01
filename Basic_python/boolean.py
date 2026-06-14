# Boolean often call computer decision programming language.
# Boolean has only 2 value , one is True and another is False, also use for take decision
print(type(True))
print(type(False))

# Why Boolean use for ?
# We often use boolean for take Decision . 
#E.g., 
age = 20
print(age >= 18) # output should be True , because 20 is grather than 18 


#Comparison Operators
# Grather than 
print(5 > 3)    # True, because 5 is grather than 3 

#less than 
print(5 < 3)    # False, because 3 is not grather than 5 

# equal to
print(5 == 5)   # True,  5 and 5 both are same  , we often use in password matching.

# not equal to 
print(5 != 5)   # False, because 5 and 5 both are same, not equal is not logically matching.

# grather than and equal to
print(5 >= 5)   # True,  because 5 and 5 are equal ,

#less than or equal to 
print(5 <= 4)   # False, because 4 is not grather than or equal to 5


 
#Boolean Operator

print("True and True =", True and True)    # True, 
print("True and False=", True and False)   # False
print("False and False=", False and True)   # False
print("False and False =",False and False)  # False

# or function is different than and function. 
#If any one True then it's true if not then false 


print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

weekend = False
holiday = True

print(weekend or holiday)

#not, not use also for convert into oposite 
print(not True)   # False, because not true means it is not true so it show opposite, false.
print(not False)  # True, not false means it is true .

# Bool can Behavior like int . but we don't use it . and it never gone negative . maximum it can go 0.
# True is 1 number and False is 0 number 
print(True + True )  # Output should be 2
print(False  + True + True ) # Output should be 2

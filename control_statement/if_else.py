age = 20 # age is a variable 
has_id = True # Has id is a variable

if age >= 18: # checking condition
    if has_id: # nested condition 
        print("Entry allowed") 
    else:
        print("Not allowed")


# So the question is can i write code with a simplier way ? 
# The answer is true .
# Then why do we use nested if ?
# Because sometimes you need to check one condition first and only if true should you check another condition .

#For example 
age = 20
has_id = True
ticket = True

if age >= 18:
    if has_id:
        if ticket:
            print("Entry allowed")
        else:
            print("Buy a ticket first")
    else:
        print("Bring your ID")
else:
    print("You must be 18+")


# There are all the condition depended with each other , 
"""Is the person 18 or older ?
 If yes, do they have an ID ?
 If yes, Do they have a ticket ?"""

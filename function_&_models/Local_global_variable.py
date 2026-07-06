# What is local variable and what is global variable ?
# Local variable is nothing but where variable create inside of the function.

# you can't use outside of the function 

def test():
    x = 10
    print(x)

test()

# Global variable is nothing but where variable create outside of the function. 
# global variable is write outside of the function 
#e.g., 
name = "Shyamal"   # Global Variable

def greet():
    print(name)

greet()
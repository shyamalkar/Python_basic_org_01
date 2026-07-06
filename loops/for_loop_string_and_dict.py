# for loop 
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit) # it can print one value inside the list.

# for loop over a string 

name = "Python"

for c in name:
    print(c)

# for loop over dictionary 
student = {
    "name": "Shyamal",
    "age": 21,
    "city": "Kolkata"
}
# Only key 
for ky in student:
    print(ky)

# Only value 
for value in student.values(): 
    print(value)


# key and value both 
for key, value in student.items():
    print(key, value) 
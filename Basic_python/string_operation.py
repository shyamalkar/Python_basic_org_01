name = "Python"

# all capital letter uppercase .

name = "Python"
print(name.upper()) # OUTPUT should be :- PYTHON

# Lower()

text = "HELLO"
print(text.lower()) # OUTPUT SHOULD BE :- hello

#title()
text = "hello world . my name is shan"
print(text.title())  # output = Hello World , title() fun

# capitalize(). only first text write in capital word.
text = "python programming"
print(text.capitalize()) # output = Python programming

#strip() remove extra space last and first 
text = "   Python   " 
print(text.strip())  

#replace(), one place replace by another place.
text = "I like Java"
print(text.replace("Java", "Python")) # Python replace the Java word.

#find ()
text = "Python"
f = "Kila"
print('Find function',text.find("t")) # The output should be 2, because it tell us how many word after t presenting, and it always count start from 0 .
print('find function', f.find("K"))

#count()
text = "banana"

print(text.count("a"))

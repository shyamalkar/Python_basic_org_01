#Working with binary file 

f = open("binaryfile.bin",'wb') # wb for (write binary)
f.write(b"hello binary world")
f.close()

f = open("binaryfile.bin", "rb") #rb for (read binary)
data = f.read()
print(data)
<<<<<<< HEAD
=======
f.close()  
>>>>>>> b9afcd71d2388c25234601a0013b7370a85d57dd

f1=open("original.txt","w")
f1.write("Hello I am Rajnandini.\n")
f1.write("have a nice day.\n")
f1.close()


f1=open("original.txt","r")
data=f1.read()
print("Content of original.txt:\n")
print(data)
f1.close()




f2=open("copy.txt","w")
f2.write(data)
f2.close()


print("content is succesfully copyed form file")
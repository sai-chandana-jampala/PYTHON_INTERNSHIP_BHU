# file handling

#file opening - name of the file , mode
f = open("renamed.txt.py")
f.close()

# python read file
f = open("renamed.txt.py")
print(f.read())

# python read upto certain characters
f = open("renamed.txt.py")
print(f.read(10))

#python - read only one line
f = open("renamed.txt.py")
print(f.readline())


# looping through file
f = open("renamed.txt.py")
for x in f:
    print(x)

#python - close file
f = open("renamed.txt.py")
f.close()
# its a good practise to close the file



# python - write or append files
# append just attach at the end
# where as , write will just over write the file
f = open("renamed.txt.py","a")
f.write("i am intrested in web devlopment")
f.close()
f = open("renamed.txt.py","r")
print(f.read())
f.close()
# using the write  mode
f = open("renamed.txt.py","w")
f.write("i am intrested in web devlopment")
f.close()
f = open("renamed.txt.py","r")
print(f.read())
f.close()

# creating a new file
f = open("chandu.txt","x")
f.close()
 
# deleting a file
import os
os.remove("chandu.txt")

# check is the file exists
import os
if os.path.exists("chandu.txt"):
        os.remove("chandu.txt")
else:
        print("file doesnt exists")


# deleting a file
import os
os.rmdir("renamed.txt")# created a file with this name and it got removed 

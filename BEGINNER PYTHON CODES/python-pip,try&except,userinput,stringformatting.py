# pip
#the pip is the package manager for all all the packages or the modules
# the pip contains all the files that needed for the module
# you can just import and use it








# python - try , except
# try block - helps you to test the block of code
# except block - helps you to handle the errors
# else block - it just runs when the block of code is true
# finally block - it runs wether the block of code it true or not
# normally if an error occurs the program execution will stops
# to over come this exception we are gonna use the try and except block


# just usage of try and except block 
try :
    print(hello)
except:
    print("something is wrong")

# usage of else and finally  block
try :
    print("hello")
except:
    print("wrong")
else:
    print("hey! its a string")
finally:
    print("code execution completed")
    
# you can use two try  and except blocks 
# mostly the finally block is used to close the file
try :
    f = open("demo.txt")
    try:
        f.write =("hi!")
    except:
        print("huh?""check your file again")
    else:
        print("file got opened")
    finally:
        f.close()
except:
    print("something went wrong")

# rasie an exception(note: delete the comment sign while using)
#x = -1
#if x < 0:
#    raise Exception("only int is possible")

# you can also give what type of error to rise
#x = "hello"
#if not type(x) is int :
    #raise TypeError("only int are allowed ")







# python - user input
#python allows user input, this means the user can give the input


username = input("enter the username:")
print("my user name is"+" " + username)




# the string formatting is similar to using the format command that is discussed in above files






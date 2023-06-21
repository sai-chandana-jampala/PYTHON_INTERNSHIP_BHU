# data types
# this is about text  and numbers data type
print("\n" "assigning values to varaibles:")
x = 3
print(x)
x = 4.4
print(x)  # assigning int float , complex, string data types to a variable
x = "sai chandana jampala "
print(x)
x = 2 + 2j
print(x)








# printing the random number
print("\n""printing the random number btw 1 to 10 :")
import random
print("\n",random.randrange(1,10)) # printing a random number btw 1 to 10 








# type casting
print("\n""type casting:")
x = int(5.0)
print(x)        # note : you cannot change the data type of complex number
x= str (5.0)    # you can change the data type into int , float , string , complex
print(x)












#python string
print("\n""python slicing:")
x ="saichandana"
for X in x :    # using for loop to print the character in the string
    print (X)
y = "saichandana"
print(y[2:5])  # before character


print(y[ :5]) # slice from start

print(y[0: ]) # slice to end

print(y[-5:-2 ])# negative indexing









# python modifying
print ("\n"" python modifying the string :")
z = " hello, world"
print(z.upper()) # converting to upper case 
print(z. lower()) # converting to lower
print(z. strip()) #  removing the white space 
print(z.split()) # spliting the words btw ,
print(z. replace("e", "i")) # replacing the words










# string concatenation
print("\n" "string concatenation:")
a = " sai"
b = " chandana"
c = a + b
print(c)









# finding the length pf string
print("\n"" the length of the string :")
a= "saichandana"
print(len(a))













#to find wether a phase or character is present in the string
print("\n""to find wether givne phase is present in the string" )
a = " sai chandana"
print ( "sai" in  a)
# to find wether the given phase is not present in the string
print("\n""to find wetehr the given phase is not present in the string ")
a = " sai chandana"
print("chandu" not in a)















# you cant combine  numbers to string but you can do it by format method
print("\n using format method:")
a = " the number of cars are{} , one of the car cost is {} another car cost is {}"
print (a.format(2,1500,500))

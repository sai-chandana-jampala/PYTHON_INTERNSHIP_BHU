# creating a function
def my_function():
    # x = a + b
    pass

my_function()

# arguments should be equal to parameters
# passing arguments
def my_function(a,b):
     x = a + b
     print(x)
my_function(3,4)

# arbitary arguments : if you dont know how many arguments you gonna pass
# use the asetrisk mark
def my_function(*fruits):
     print("i like"+fruits[1])

my_function("mango", "banana")

# key word arguments: you can pass the arguments the parameters as key = value
def my_function(a,b):
     x = a + b
     print(x)
my_function(a=3,b= 4)

# arbitary key word arguments
# if you dont know how many arguments you gonna pass
def my_function(**kid):
  print("Her last name is " + kid["f"])

my_function(f = "sai", l = "chandana")

# default paramter value
def my_function(a=3, b = 4):
     x = a + b
     print(x)
my_function()

# passing the list as an argument
def my_function(fruits):
     print("i like"+" "+fruits[2])
fruits = ("mango", "banana", "apple")
my_function(fruits)

# return the value
def my_function(a,b):
     return a + b
print(my_function(a=3,b= 4))
print(my_function(a=4,b= 5))

# for some purpose you gonna make the function empty with out getting error we can write the pass statment
# python also accepts recursion , recursion is ntng but calling itself countinousley
# you need to have termination statment



# lambda functions
def my_function(n):
    return lambda a: a*n
mydoubler = my_function(2)
mytrippler = my_function(3)
print(mydoubler(11))
print(mytrippler(11))
# or
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

# array
#python doesnt supoort built in supoorted arrays
# we need to use list as the arrays
# every thing would be same as the list 








































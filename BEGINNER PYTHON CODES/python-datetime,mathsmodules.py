#---------------------------date&time-----------------------------------------#
# importing the date time 
import datetime
x = datetime.datetime.now()
print(x)# this will display year, month,date,hour,minute,second,microsecond

#  giving objects to date time module
import datetime
x = datetime.datetime(2001,3,21)
print(x)
# you shouldnt write now

#using strfttime()
import datetime
x = datetime.datetime(2001,3,21)
print(x.strftime("%b"))
# displaying the name of month




#---------------------mathsmodules--------------------------#
#python-maths,
# finding min and max
a = [1,2,3]
print(max(a))#finding max
print(min(a))#finding min

#returning the absolite +ve value
x = -2.25
print(abs(x))
 
#power of (x,y)
x =pow(3,4)
print(x)

# using maths module for difficult maths functions
# using sqrt
import math
x = math.sqrt(64)
print(x)


# method to rounding to the upwards nearest
x = math.ceil(1.24)
print(x)

# mathod to rounding to the downwards nearest
x = math.floor(1.24)
print(x)

# method to find the value of pie
import math
x = math.pi
print(x)

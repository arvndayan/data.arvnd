#Global Variable
# variables that are created outside of the function are know as global variables
# global varibales can be used by everyone, both inside or outside of the function


#example for global variable
X = "Aravind awesome" #this is global varibale which is used outside of the function

def myfunc():
    print("python makes " + X)

myfunc()

#example for local variable

x = "awesome" 

def myfunc():
    x = "great" # local variable which is used inside the function
    print("python is " + x)

myfunc()
print("python is " + x)
#Looping through a string:
# Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "banana":
    print(x)

#String Length
# To get the length of a string, use the len() function.

a = "Hello, World!"
print(len(a))

#check string:
#to check if a certain phrase or character is present in a string, we can use the keyword in

txt = "The best things in life are free!"
print("free" in txt)

# use it in an if statement:
#print only if "free" is present:

txt = "The best things in life are free! "
if "free" in txt:
    print("yes, 'free' is presen.")

#check if not 
#to check if a certain phrase or character is NOT present, we can use the keywood not in.

txt = "The best things in life are free!"
print("expensive" not in txt)

#use it in an if statement:

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
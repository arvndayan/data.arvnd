
#insert() this function can only insert one at a time
x = ["apple", "banana", "papaya"]
x.insert(0, 'dog')
x.insert(1, 'cat')
print(x)

# to insert multiple items at a time we can use slicing or concatination
x = ["apple", "banana", "papaya"]
y = ("cat", "dog", "snake")
x[1:2] = y
print(x)


#Python Collections(Arrays)
# List  : is a collection which is ordered and changeable. Allows duplicate members.
# Tuple : is a collection wich is ordered and unchangeable. Allows duplicate memnbers.
# Set   : is a collection  which is unordered, unchangeable and unindexed. No duplicate members.
# Dict  : is a collection which is ordered and changeable. No duplicate members.

# List items are indexed and you can refer them by using index
x = ["apple", "banana", "papaya"]
print(x[1]) #result will be banana

# insert() To insert a list item at a specified index, use the insert() method.
#syntax : list.insert(index, element)
x = ["apple", "banana", "papaya"]
x.insert(0, 'dog')
x.insert(1, 'cat')
print(x)

#append() it will add an item to end of the list
x = ["apple", "banana", "papaya"]
x.append("tomato")
print(x)

#extend() to append elements from another list to current list 
x = ["apple", "banana", "papaya"]
y = ["car", "bat", "van"]
x.extend(y)
print(x)

#remove() method removes the specificed items
x = ["apple", "banana", "papaya"]
x.remove("banana")
print(x)

#If there are more than one item with the specified value, the remove() method removes the first occurrence:
x = ["apple", "banana", "papaya", "banana"]
x.remove("banana")
print(x)

#pop() method removes the specified index.
x = ["apple", "banana", "papaya", "banana"]
x.pop(1)
print(x)

#If you do not specify the index, the pop() method removes the last item.
x = ["apple", "banana", "papaya", "banana"]
x.pop()
print(x)

# del keyword also removes the specified index:
x = ["apple", "banana", "papaya", "banana"]
del x[0]
print(x)

#The clear() method empties the list.The list still remains, but it has no content.
x = ["apple", "banana", "papaya", "banana"]
x.clear()
print(x)
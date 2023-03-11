# Ch 10 (lists) Topics
# What is a list
# Is it mutable? Yes
# Traversing lists
# Slicing
# Map, filter, reduce
# Deleting
# List and strings
# What gets stored and Aliasing
# lists and functions

# Ch 11 (Dictionaries) Topics
# Key, value pairs
# Using dictionaries
# Searching by values
# Dictionaries and lists
# global variables
# is it mutable? Kinda

# Ch 12 (Tuples) Topics
# what is a tuple?
# is it mutable? No, it's immutable
# Assignment
# Multiple returns from a single function
# Variable-length Argument
# Dictonaries and lists for tuples


# lists are like strings where you can reference parts of them by an index value

# How pyhthon stores and accesses data can be tricky

# Lists are considered "mutable" along with Dictonaries this trait allows the data
# to be changed however because it changes instead of being made into a new piece
# of data bugs commonly occur when multiple things are working on lists.
A_list = [1, 2, 3]
# print("This list is mutable A=", A_list)

# Integers along with floating point values and strings i.e. decimal point values, are
# immutable which means everytime we update the value a new value is stored
# in memory insead of changing it.
a_number = 2
#print("This number is immutable a=", a_number)

# We can see what the immutable and mutable definitions look like by using two
# values and changing one and see if the other was updated or not

# CHALLENGE: Try making you own examples of both mutable and immuable cases
b_number = a_number
print("Two immutable integers set equal to eachother (a=b) a=",
      a_number, "b=", b_number)

b_number = b_number + a_number
print("b = a + b causes new values to be created in memory and a remains unchanged a =",
      a_number, "b =", b_number)

# So how about when things mix?

B_list = A_list

print("how about when we set lits to equal eachother? Here A_list = Blist",
      A_list, "==", B_list)

B_list[1] = B_list[1] + A_list[1]

print("Now for the tricky parts, Notice what happens when I try to update B_list using A_list", A_list, "=?", B_list)
print("both values change")

B_list[1] = B_list[1] + 2
print("How about if we try to use only a integer and never reference A_list? For instance B_list's second value +2 ?",
      "we get A_list =", A_list, "==", "B_list=", B_list)

# If you want to copy lists, dictonaries or any iterable, make a new one
B_list = [B_list[0], B_list[1]+2, B_list[2]]
print("Basically if we want independent copys of immutables in our case we need to make a new list made")
print(A_list, "=?", B_list)

# The a += 1 operation is  away to say a value a = a + 1, will create a new data value when
# used on a mutable object.
B_list[1] += 2

print("Notice how when we use += on B_list item it does nothing to the A_list",
      A_list, "=?", B_list)

# We also need to be careful when trying to grab only 1 part of a mutable object because in Python
# because it will make it go from  mutable to immutable
c = B_list[0]
print("c set to B_list[0] is", c)
B_list[0] = 5
print("c after b has changed =", c)
c = B_list[0]
# CHALLENGE: make sure if i change B_list[0] c is unchanged
print("here we are setting c = B_list[0] c=", c, "B_list", B_list)
c = c+1
print(" Its not obvious if c is independent and a mutable integer or inherited the mutableness of B but notice what happens when i update it c + 1 c=", c, "B_list =", B_list)


# how to mess it up in a Loop
print("printing items to show whats going on in the loop, notce no where is there a counting variable")
for items in B_list:
  print(items)
  #CHALLENGE: why does this work when you put items == 1?
  if(items == 2):
    B_list[items] += 2

print("notice after this loop the A_list and B_list remain unchanged",
      A_list, "=?", B_list)
#CHALLENGE figure out why this loop isnt working as it looks like it should

# If we want the count for whats being looped we use a method
# CHALLENGE: write this loop to match the one with the x below
print("Becase it is an interator being looped its index is given by using a method")
for items in B_list:
  print(B_list.index(items))
# how change a mutable it in a Loop but "not great" way
x = 0
for items in B_list:
  x = x + 1
  print("x in loop = ", x)
  if(x == 1):
    B_list[x] += 2
print("notice the change to only B_list due to += operator A_list=",
      A_list, "B_list=", B_list)

# CHALLENGE write a loop that makes a smaller new list from a list you write

# now for a funciton


def function_time(alpha, delta):
  # notice i do not say anything about if the two varbales being passed
  the_result = alpha + delta
  return the_result


string_a = "hello"
string_b = "world"
num_a = 2
num_b = 4

#when you make a fucntion the return is what is getting pointed to by the varible
# output in this case. The data is "created" by return. the option to not use a
# return is there but can cause bugs
output = function_time(string_a, string_b)
print("two strings passed to the function", output)
output = function_time(num_a, num_b)
print("two integers passed to the function", output)
output = function_time(A_list, B_list)
print("two lists passed to the function", output)


# Dictonary examples to learn from

# creates a dictionary
# with numbers as key
# values as numbers
num_as_key = {0: [{5: 4, 2: 8},
                  {1: 7, 2: 9}],
              1: [{23: 523, 1000: 22},
                  {25: 33, 43: 32}]}

# creates a dictionary
# with stings as key
# values as numbers
string_as_key = {'first': [{5: 4, 2: 8},
                           {1: 7, 2: 9}],
                 'second': [{23: 523, 1000: 22},
                            {25: 33, 43: 32}]}

# creates a dictionary
# with numbers as key
# values as lists of numbers
list_of_numbers = {'10': [[50, 400, 20, 80],
                          [1, 70, 2, 9]],
                   '20': [[23, 5203, 11200, 22],
                          [25, 303, 43, 32]]}
#CHALLANGE make your own Dictonary and print the values out. Try chaning the keys
# and try changing or expanding the values

# printing  lists of data and keys in a few ways
# using items() method
print("accessing  lists of data and keys in a few ways")
print("accessing a dictionary with a number as the key")
# CHALLANGE .items() is a method for dictonaries. look up and try to use a different method.
for key, values in num_as_key.items():
    #CHALLANGE make a condition to set 1 of the Dictonaries to a new variable
    for i in values:
       print(key, " : ", i)


for key, values in num_as_key.items():
    for y in values:
        print(key, ":", y)


for key, values in num_as_key.items():
    for i in values:
        print(key)

for key, values in num_as_key.items():
    for i in values:
        print(i)  # notice the loop is going over values for each key

print("now accessing with a sting based key")

for key, values in string_as_key.items():
    for i in values:
        print(key, " : ", i)

print("*removed printing the key twice*")

for key, values in string_as_key.items():
    for i in values:
        print(i)

print("Now what if only use key instead of key, values?")
for key in string_as_key.items():
    print(key)

print("with second loop, notice both lists are printed at once, one key is printed")
for key in string_as_key.items():
    print(key)
    for values in key:
        print(values)

print("a Dictonary with lists as the value")

for key, values in list_of_numbers.items():
    for lists in values:
        print(lists)
        print(lists[0])
        if(lists[0] < 100):
          print("im low")

# tuples are a comma seperated combo of data,
# a empty tuple is (), a single value tuple is (value,) it needs the comma

a_tuple= (1,2,3)

# tuple as key
tuple_as_key = {(0, 1): "cat",
              (2, 3): "dogs"}

for key in tuple_as_key.items():
    print(key)
    for values in key:
        print(values)

# normally functions return 1 value but a tuple allows for multiple values to be returnd at once.
# remember mutable values changed in a function are seen by the caller and passed value, immutable values are returned.
def my_tuple_update(split_up):
     first,second = split_up.split(" ")
     return (first, second)

string = ("the Cat")

print(string)
new_tup = my_tuple_update(string)
print(new_tup)

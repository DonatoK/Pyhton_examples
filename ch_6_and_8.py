# Ch 6 (FUNCTIONS) topics
# Return values
# Incremental development
# Composition
# Boolean Functions
# More recursion
# Checking types

# Ch 8 (STRINGS) topics
# what is a string
# string length
# for loops
# slicing strings
# what is immutable
# searching strings
# looping and counting
# string methods
# in string
# string comparison


# What is a python function
# remember last weeks code
value =5
while value > 1 :
    print(value)
    value = value - 1
# other checks you could do with the while loop
# see chapter 5
# x != y
# x > y
# x < y
# x >= y
# X <= Y
# x == y

# conditiional execution
value =5
while value > 1 :
    if value == 4:
        print("magic number 4 hit")
    print(value)
    value = value - 1

#  can place code one, have it do work, and call it again
def print_vals():
    value = 5
    while value > 1:
        print(value)
        value = value - 1

# Using a function, notice you were using a function everytime you used print
print_vals()

def Better_print_vals(input_num):
    if (input_num == 3):
        print(" i do not like 3")
    else:
        while input_num > 1:
            print(input_num)
            input_num = input_num - 1

Better_print_vals(3)
Better_print_vals(4)
# can i use value?
print("can i use value?")
Better_print_vals(value)
#value = 7
#Better_print_vals(value)
# Have that same code return a value for later use

def return_print_vals(input_num):
    while input_num > 1:
        print(input_num)
        input_num = input_num - 1
    return input_num

hmm = return_print_vals(value)
print("what the function gave did", hmm)

# can be a true, false value (boolean) or any other value you choose

# recursion, functions that call themselves. Need some type of way to exit or it runs forever
# fun to write and think about but not needed for ARC, example taken from the book for learning

"""def factorial(n):
if n == 0:
return 1
else:
recurse = factorial(n-1)
result = n * recurse
return result """



# what are stings
my_string = "stuff"
# print(my_string[0])
# # how big is my string
# print(len(my_string))
# # negative wrap around
# print(my_string[-5])
# # a note on getting the last letter
# # print("print (my_string[len(my_string)]))", (my_string[len(my_string)]))
# # print(my_string[5])
# # hmmm
# # print("print (my_string[len(my_string) -1]))", (my_string[len(my_string) - 1]))

# how to change a string
#my_string[0] = "a"
my_string = "new_stuff"

# how to take a string chunk
print(my_string[0:3])
print(my_string[:3])
print(my_string[4:])
# what is a for loop
for letters in my_string:
    print(letters)
# place the for loop in a function and call it
def string_funct(in_str):
    for letters in in_str:
        print(letters)

string_funct(my_string)

#strings have methods you can run on them.
my_string = my_string.upper()
print(my_string)
# be careful with void methods
new_string = my_string.upper
print(new_string)

# more useful method is find
t_index = my_string.find('T')
print(t_index)
print(my_string[t_index])

# what if the letter is not there?

# Next lessons starts to go over how to control flow in our functions and more data types besides strings (lists, truples, and dictonaries)
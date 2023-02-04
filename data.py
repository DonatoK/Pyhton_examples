# How phthon stores and accesses data can be tricky

# Lists are considered "mutable" along with Dictonaries this trait allows the data
# to be changed however because it changes instead of being made into a new piece
# of data bugs commonly occur when multiple things are working on lists.
A_list = [1, 2, 3]
print("This list is mutable A=", A_list)

# Integers along with floating point values i.e. decimal point values, are
# immutable which means everytime we update the value a new value is stored
# in memory insead of changing it.
a_number = 2
print("This number is immutable a=", a_number)

# We can see what the immutable and mutable definitions look like by using two
# values and changing one and see if the other was updated or not

# CHALLENGE: Try making you own examples of both mutable and immuable cases
b_number = a_number
print("Two immutable integers set equal to eachother (a=b) a=",
      a_number, "b=", b_number)

b_number = b_number + a_number
print("b = a + b causes new values to be created in memory and a remains unchanged a =",
      a_number, "b =", b_number)


F_list = [7, 8, 9]
print(F_list)

f_number = 8
print(f_number)

f_number = b_number
print(f_number, b_number)

f_number = f_number - a_number
print("f_number =", f_number, "a_number =", a_number)

# So how about when things mix?

B_list = A_list

print("how about when we set lits to equal eachother? Here A_list = B_list",A_list, "==", B_list)

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


c = B_list[0]
print(c)
B_list[0] += 7
print(B_list)
c = B_list[0]
print(c)
print(c, B_list[0])
# how to mess it up in a Loop
print("printing items to show whats going on in the loop, notce no where is there a counting variable")
for items in B_list:
  print(items)
  #CHALLENGE: why does this work when you put items == 1?
  if(items == 2):
    B_list[items] += 2

items == 1
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
B_list = [7,0,8,9,10]

for items in F_list:
    print(B_list.index(items))

x = 6
# now for a funciton


def function_time(alpha, delta):
  # notice i do not say anything about if the two varbales being passed
  the_result = alpha + delta
  return the_result


string_a = "hello"
string_b = "world"
num_a = 2
num_b = 4

# when you make a fucntion the return is what is getting pointed to by the varible
# output in this case. The data is "created" by return. the option to not use a
# retun is there but can cuase bugs
output = function_time(string_a, string_b)
print("two strings passed to the function", output)
output = function_time(num_a, num_b)
print("two integers passed to the function", output)
output = function_time(A_list, B_list)
print("two lists passed to the function", output)

# here is a function that would be fun to expand
# it takes in 1st order or linear polynomials coefficient and constant, then
# returns the reuslt of a squaring operation e.g. (2x+1)^2 would feed in a
# 2 and a 1 while the result would be 4x^2 + 4x + 1
# CHALLANGE make this function to work on (3X^2 + 2X + 1)^2
# CHALLANGE address a negative constant or x_coeff


def square_poly(x_coeff, const):
  second_power = x_coeff * x_coeff
  first_power = x_coeff * const
  # We need to run the same operations using the constants
  first_power = first_power + (const*x_coeff)
  squar_const = const * const
  print(second_power, "X^2 +", first_power, "X +", const)


# CHALLANGE try different values
test = square_poly(2, 1)

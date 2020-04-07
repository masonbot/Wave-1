import math
# # Inputs

# #Note: cant multiply 2 strings toegther
# length = input("length of your property in metres:")
# width = input("width of your property in metres:")
# length = int(length)
# width = int(width)

# area = (length) * (width)
# area = str(area)

# print(area)

toRoot = input("please enter a number to find its root:")
toRoot = int(toRoot)
root = math.sqrt(toRoot)

print("the root is:" + str(root))

## BOOLEAN EXPRESSIONS AND OPERATORS
# 3 boolean operators: and, OR, !(not)
on = True
off = False

#and
andExample = on and off

# and will return true if both sides of and is = true
# and will return false if ones sides = false

# OR operator
orexample = on or off
#or will return true if one of the sides of the or  =true
#or will return false if both sides of the or =false

#not (!) operator:
notExample = not on 
 
# Order of boolean operators Not. And, then OR
#computes the results in that order
combinedExample = on or off and on

print(combinedExample)

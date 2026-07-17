# Day One - Exercise Level 3

import math

# Exercise 3a
print(type(9))                          # Integer
print(type(9.2))                        # Float
print(type(9j * 2))                     # Complex

print(type('Finn'))                     # String

truth_value = True
print(type(truth_value))                #Boolean

print(type([67, 21, 19]))               # List
print(type(('Star','Moon', 'Planet')))  # Tuple
print(type({7.26, 2.24, 6.8, 7.2}))     # Set
print(type({'first_name':'Jessamine'})) # Dictionary

# Exercise 3b: Find the Euclidean distance between (2,3) and (10,8)

a = (2, 3)
b = (10, 8)

euclidean_ab = math.dist(a, b)
print("The Euclidean distance between point a & point b is ", euclidean_ab, ".")



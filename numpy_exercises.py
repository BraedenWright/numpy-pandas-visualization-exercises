## Using Numpy

import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# Exercise 1

is_negative = a[a < 0]
len(is_negative)

## Answer: 4

# Exercise 2

is_positive = a[a > 0]
len(is_positive)

## Answer: 5

# Exercise 3

positively_even = a[(a > 0) & (a % 2 == 0)]
len(positively_even)

## Answer: 3

# Exercise 4

add_three = a + 3
len(add_three[add_three > 0])

## Answer: 10

# Exercise 5

a_squared = a ** 2
# mean
a_squared.mean()
# std dev
a_squared.std()

## Answer mean of 74 and std dev of 144.0243035046516

# Exercise 6

a.mean()
#current mean of 3

center = a - 3
center.mean()

## Answer ^^^

# Exercise 7

# z-score

numer = (a - a.mean())
numer

denom = a.std()
denom

z_score = numer / denom
z_score

## Answer ^^^ (wow, this seems too easy)




# Exercise 8

#### Setup 1
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

sum_of_a = a.sum()
sum_of_a

## Answer: 36

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = np.min(a)
min_of_a

## Answer: 1

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = np.max(a)
max_of_a

## Answer:  10

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = np.mean(a)
mean_of_a

## Answer:  5.5

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

product_of_a = np.prod(a)
product_of_a

## Answer:  3,628,800

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

squares_of_a = np.square(a)
squares_of_a

## Answer: [  1,   4,   9,  16,  25,  36,  49,  64,  81, 100]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

odds_in_a = a[a % 2 == 1]
odds_in_a

## Answer: [1, 3, 5, 7, 9]

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = a[a % 2 == 0]
evens_in_a

## Answer: [ 2,  4,  6,  8, 10]

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.

b = np.array([
    [3, 4, 5],
    [6, 7, 8]
    ])

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

## Answer:  33

sum_of_b = np.sum(b)
sum_of_b

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

min_of_b = np.min(b)
min_of_b

## Answer: 3

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = np.max(b)
max_of_b

## Answer: 8

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

mean_of_b = np.mean(b)
mean_of_b

## Answer: 5.5

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

product_of_b = np.prod(b)
product_of_b

## Answer: 20,160 

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

squares_of_b = np.square(b)
squares_of_b

## Answer: [[ 9, 16, 25],
#          [36, 49, 64]]

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

odds_in_b = b[b % 2 == 1]
odds_in_b

## Answer:  [3, 5, 7]

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

evens_in_b = b[b % 2 == 0]
evens_in_b

## Answer: [4, 6, 8]

# Exercise 9 - print out the shape of the array b.

np.shape(b)

## Answer: (2, 3)

# Exercise 10 - transpose the array b.

np.transpose(b)

         [[3, 6],
          [4, 7],
          [5, 8]]

## Answer: ^^^

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

b.reshape(1, 6)

## Answer: [3, 4, 5, 6, 7, 8]

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

b.reshape(6, 1)

           [[3],
            [4],
            [5],
            [6],
            [7],
            [8]]

## Answer:  ^^^^

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])


# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

## Answer:

# Exercise 2 - Determine the standard deviation of c.

## Answer:

# Exercise 3 - Determine the variance of c.

## Answer:

# Exercise 4 - Print out the shape of the array c

## Answer:

# Exercise 5 - Transpose c and print out transposed result.

## Answer:

# Exercise 6 - Get the dot product of the array c with c. 

## Answer:

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

## Answer:

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

## Answer:

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d

## Answer:

# Exercise 2 - Find the cosine of all the numbers in d

## Answer:

# Exercise 3 - Find the tangent of all the numbers in d

## Answer:

# Exercise 4 - Find all the negative numbers in d

## Answer:

# Exercise 5 - Find all the positive numbers in d

## Answer:

# Exercise 6 - Return an array of only the unique numbers in d.

## Answer:

# Exercise 7 - Determine how many unique numbers there are in d.

## Answer:

# Exercise 8 - Print out the shape of d.

## Answer:

# Exercise 9 - Transpose and then print out the shape of d.

## Answer:

# Exercise 10 - Reshape d into an array of 9 x 2

## Answer:
# Print out all your results below to check if your answers are correct


# Part 1
# Generate a list of numbers from 0 to 9 using list comprehension with a name "list1"
list1 = [x for x in range(0, 10)]
print(list1, "\n")
# Reverse the order of the list created in the part above (list1)
list1.reverse()
print(list1, "\n")
# change the 5th element of the list to be the letter "a"
list1[4] = 'a'
print(list1, "\n")
# Deduce a part of the list (slicing) from index 2 to index 7, STORE it as "list2" and then print it out
list2 = list1[2:8]
print(list2, "\n")

# Part 2
# Generate a list called "seven_multiples" using list comprehension of numbers from 0 to 999 which are multiples of 7
seven_multiples = [x for x in range(0, 1000) if x % 7 == 0]
print(seven_multiples, "\n")
# Print out the second last element of the list using negative indexes
print(seven_multiples[-2], "\n")

# Part 3
# Use a for loop to change all the values in the list "seven_multiples"
# for i in enumerate(seven_multiples):
#     seven_multiples[i] = 7

for i in range(len(seven_multiples)):
    seven_multiples[i] = 7
print(seven_multiples, "\n")
# created in the previous exercise to be number "7"

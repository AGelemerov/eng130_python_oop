# Report an issuefind_largest(numbers) should return the largest number from numbers.
# The array numbers always contains at least one number.
# Implement find_largest(numbers).

import random as r

len_of_list = r.randint(1, 10)  # make amount of numbers in list random (minimum 1)
numbers = []

for i in range(len_of_list):
    numbers.append(r.randint(1, 1000))  # add random numbers to the list


def find_largest(numbers_list):
    largest_num = 0
    for num in numbers_list:
        if largest_num < num:
            # compare current largest number with nuber being read
            # if current largest is smaller than one being read, new largest number is the one being read
            # e.g. largest_num = 7, number being read is 10, make the largest number = 10
            largest_num = num
    return largest_num


print(numbers)
print(find_largest(numbers))

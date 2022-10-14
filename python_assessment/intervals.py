# Report an issue Implement the find_smallest_interval(numbers) function which returns the smallest positive interval
# between two values of the numbers table. For example given the table the smallest interval is 1 (
# difference between 2 and 1) Constraints: numbers contains at least two numbers and a maximum of 100,000 entries.The
# solutions which favor execution time on large size arrays will get the most points.The difference between two
# elements will never exceed the size of an integer for your language
def find_smallest_interval(numbers):
    numbers.sort()
    interval = 100001

    for i in range(len(numbers) - 1):
        temp_interval = abs(numbers[i] - numbers[i + 1])
        if interval > temp_interval:
            interval = temp_interval

    return interval


print(find_smallest_interval([1, 6, 4, 8, 2]))

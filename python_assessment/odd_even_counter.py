# In this task, you will find a function called odd_even_counter that takes an argument of number. You will need to
# implement the below details to solve the problem: Implement a list - Consider that the list will need to be set
# i.e. not blank []: The list at index 0 will relate to even numbers and at a list index 1 odd numbers. You will need
# to iterate on any given number until it reaches 0. Within the loop, you will need to evaluate whether the number is
# even or odd and add it to the appropriate list index ensuring that it does not overwrite the number but adds to
# it. Remember to manage a counter in your loop. You will need to only return the array An example:
#
# If you run the test, which is being given the number 5 -> oddEvenCounter(5) it should print 6 and 9
#
# This is because the array returns [6,9] because of the even totals 2+4 = 6 and the odd totals 1+3+5 = 9
#
# Remember to use the test to ensure your method is correct!

# [x, y] - x = amount of even, y = amount of odd
def odd_even_counter(number):
    # 10 as example, take sum of all odd numbers below, then take sum of all even numbers
    odd_even_list = [0, 0]
    while number > 0:
        if number % 2 == 0:
            odd_even_list[0] += number
        elif number % 2 == 1:
            odd_even_list[1] += number

        number -= 1
    return odd_even_list


print(odd_even_counter(6))

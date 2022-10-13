# multiplies two numbers
def multiply(num1, num2):
    return num1 * num2


# divides two numbers
def divide(num1, num2):
    return num1 / num2


# executes the modulo operator on two numbers
def modulus(num1, num2):
    return num1 % num2


# converts centimeters to meters
def cm_to_m(cm):
    return cm / 100


# converts inches to centimeters
def inch_to_cm(inch):
    return inch * 2.25


# converts meters to feet
def m_to_feet(m):
    return m * 3.28


def movie_rating():
    # Options task
    age = int(input("Please enter you age: "))

    while True:
        if age > 117:
            print("Please re-enter your age, ages above 117 not allowed: ")
            break
        elif age >= 18:
            print("You are allowed to view movies for up to 18 and above")
            break
        elif age >= 16:
            print("You are allowed to view movies for up to 16 and below")
            break
        elif age >= 15:
            print("You are allowed to view movies for up to 15 and below")
            break
        elif age >= 12:
            print("You are allowed to view movies for up to 12 and below")
            break
        elif age >= 8:
            print("You are allowed to view movies for up to 8 and below")
            break
        else:
            age = int(input("please re-enter your age, no matches found: "))


def fizzbuzz():
    range_of_nums = int(input("Please enter range of numbers to test: "))
    fizz_num = int(input("Input fizz number: "))
    buzz_num = int(input("Input buzz number: "))

    for num in range(range_of_nums):
        if (num % fizz_num) == 0 and (num % buzz_num) == 0:
            print("FizzBuzz")
        elif (num % fizz_num) == 0:
            print("Fizz")
        elif (num % buzz_num) == 0:
            print("Buzz")
        else:
            print(num)


def restaurant_task():
    menu = {
        1: "Pizza",
        2: "Lasagne",
        3: "Linguine Carbonara",
        4: "Fettuccine Alfredo",
        5: "Risotto",
        6: "Ravioli"
    }
    amount_of_orders = 0
    cart = []

    while amount_of_orders < 3:
        for item in menu.items():
            print(str(item[0]) + ".", item[1])

        chosen_item = input("Please choose an item from the menu, 0 to end selection (number): ")
        if chosen_item == "0":
            break
        cart.append(chosen_item)
        amount_of_orders += 1

    print("\nYour order is as follows: ")
    for item in cart:
        print(item)


def how_old():
    # Calculate year of birth
    import datetime

    day = 0
    month = 0
    year = 0

    while True:
        day = input("Input day you were born (e.g. 12): ")
        if day.isdigit():
            while True:
                month = input("Input month you were born (e.g. 5): ")
                if month.isdigit():
                    while True:
                        year = input("Input year you were born (e.g. 1999): ")
                        if year.isdigit():
                            break
                        else:
                            print("Invalid entry")
                            continue  # not needed but to clarify
                    break
                else:
                    print("Invalid entry")
                    continue  # not needed but to clarify
            break
        else:
            print("Invalid entry")
            continue  # not needed but to clarify

    date_today = datetime.date
    print(date_today.today())

    day_today = int(str(date_today.today())[-2:])
    month_today = int(str(date_today.today())[5:7])
    year_today = int(str(date_today.today())[:4])

    month = int(month)
    day = int(day)
    year = int(year)

    # print(day_today)
    # print(month_today)
    # print(year_today)

    years_old = int(year_today) - year
    months_old = 0
    days_old = 0
    if month > month_today:
        months_old = month - month_today
        days_old = day - day_today + 31  # 31 as october is 31 days, 28 if feb and 30 if month is 30 days
        years_old -= 1
    elif month == month_today and day > day_today:
        days_old = day - day_today
        years_old -= 1
    else:
        print("error")
    print(f"Days old: {days_old}\nMonths old: {months_old}\nYears old: {years_old}")


print(multiply(5, 2))
print(divide(5, 2))
print(modulus(5, 2))
print(cm_to_m(5))
print(inch_to_cm(5))
print(m_to_feet(5))

print("movie_rating")
movie_rating()
print("fizzbuzz")
fizzbuzz()
print("restaurant")
restaurant_task()
print("how_old")
how_old()

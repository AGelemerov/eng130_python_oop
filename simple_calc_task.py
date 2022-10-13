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


print(multiply(5, 2))
print(divide(5, 2))
print(modulus(5, 2))
print(cm_to_m(5))
print(inch_to_cm(5))
print(m_to_feet(5))

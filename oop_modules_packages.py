# Lucky draw
# keyword called "import"

# print(random.randint(100, 1000))
# each time it is run a random number is generated

# number = 23.66

# compute any numbers - to round up -
# number .50 above to round up
# number .49 less round down

# print(number)
# print(math.ceil(number), "ceil")
# print(math.floor(number), "floor")
# print(math.trunc(number), "truncate")
#
# print(math.pow(number, 2))

# print(os.cpu_count())  # will result in number of CPU threads
# print(datetime.date.today())  # Will result in today's date being printed out
# print(sys.path)


# Functions
# Reusable, saves time, saves money, helps release software faster

def greeting():
    # greet user
    print("Hello Dear")


#     keyword called pass

# calling  a function

# greeting()


# greet the user with their name
def greeting_name(name):
    for i in range(10):
        print(name)
    print("Done with 10 prints")


# greeting_name("Luke")
# greeting_name("Abdellah")
# greeting_name("Abishek")
# greeting_name("Osman")
# greeting_name("Angel")
# greeting_name("Ben")
# greeting_name("Luke")


def add(num1, num2):
    print(num1 + num2)


add(2, 4)

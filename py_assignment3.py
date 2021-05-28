# 1
def func():
    print('Hello World')

# 2


def print_name(name):
    print('Hello my name is ' + name)


print_name('Avery')

# 3


def func3(x, y, z):
    if z == True:
        print(x)
    else:
        print(y)


func3('Hello', 'Goodbye', True)

# 4


def product(a, b):
    return a * b


print(product(3, 5))

# 5


def is_even(num):
    if (num % 2) == 0:
        return True
    else:
        return False

# 6


def is_greater(num1, num2):
    if num1 > num2:
        return True
    else:
        return False

# 7


def sum_func(*args):
    print(args)
    print(sum(args))


sum_func(1, 2, 3)

# 8


def even_list(*args):
    new_list = []
    for arg in args:
        if (arg % 2) == 0:
            new_list.append(arg)
    print(new_list)


even_list(1, 2, 3, 4, 5)

# 9


def upper_lower(str):
    res = []
    for index in range(len(str)):
        if (index % 2) == 0:
            res.append(str[index].upper())
        else:
            res.append(str[index].lower())
    return ''.join(res)


print(upper_lower('Hello World'))

# 10 question doesn't make sense

# 11


def compare_first(str1, str2):
    if str1[0].lower() == str2[0].lower():
        return True
    else:
        return False


print(compare_first('Avery', 'ana'))

# 12 question doesn't make sense

# 13


def capitalize(str):
    mylist = list(str)
    mylist[0] = mylist[0].upper()
    mylist[3] = mylist[3].upper()
    return ''.join(mylist)


print(capitalize('avery'))

# final problem, pt 2 assignment
test_lst = [
    [34587, 'Learning Python', 4, 40.95],
    [98762, 'Programming Python', 5, 56.80],
    [77226, 'Head First Python', 3, 32.95],
    [88112, 'Python 3', 3, 24.99]
]


def book_shop_accounting(lst):
    new_list = []
    for item in lst:
        new_list.append((item[0], (item[2] * item[3])))
    return(new_list)


print(book_shop_accounting(test_lst))
# looks like the next question is the same thing

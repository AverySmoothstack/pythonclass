# coding exercise 3
# 1
print('Hello World'[8])

# 2
thkstr = 'thinker'
ss = thkstr[2:5]
print(ss)

# 3 the output would be 'mmy'

# 4
print(set('Mississippi'))

# function determining a palindrom from a given string


def palindrom():
    potential = input('Please input the string you would like to check: ')

    if potential == potential[::-1]:
        print('Yes')
    else:
        print('No')


# Coding Excersize 4
# 1
mixed_list = [12, 'Avery', 1.21]
print(mixed_list)

# 2
nested_list = [1, 1, [1, 2]]
print(nested_list[2][1])  # Retrieving requested value

# 3
# the result of lst=['a','b','c'] lst[1] = b

# 4
wk_dictionary = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2,
                 'Thuresday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}

# 5 the output is 2


# 6
tpl_list = [1, [1, 2]]
# converted_list = [tuple(ele) for ele in tpl_list]

# factorial of given numbers


def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


print(fact(8))

# it looks like the remaining solutions are actually included in the assignment, tested them locally, not pushing similar code


# function determining different croud inputs based on the user data list
# different croud lists for testing

crowd_1 = ['Avery', 'Amber']
crowd_2 = ['Avery', 'Amber', 'Madison', 'Aubrey']
crowd_3 = ['Avery', 'Amber', 'Madison', 'Aubrey', 'Eve', 'Debora']
crowd_empty = []


def crowd_count(crowd_list):
    if len(crowd_list) > 5:
        print('There is a mob in the room.')
    elif (len(crowd_list) <= 5) and (len(crowd_list) >= 3):
        print('There is a crowd in the room')
    elif ((len(crowd_list) < 3) and (len(crowd_list) != 0)):
        print('The room is not crowded')
    else:
        print('The room is empty')


# insert sample list here
crowd_count(crowd_empty)
palindrom()

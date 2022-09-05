def increment_by_five(x):
    a = x + 5
    print('The answer is {}'.format(a))

def increment_by_five2(x):
    a = x + 5
    if a >= 18:
        adult = True
    else:
        adult = False
    return a, adult

def increment_by_five3(x):
    a = x + 5
    if x < 0:
        return "This function cannot work on negative numbers"
    return a

increment_by_five(11)
answer, is_adult = increment_by_five2(11)
print('The answer is {}'.format(answer))
print('True or false. the person is an adult: {}'.format(is_adult))
answer = increment_by_five3(-3)

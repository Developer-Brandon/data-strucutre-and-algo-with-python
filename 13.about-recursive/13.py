import random

def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return num

print('\n')
print('8!: ', factorial(4))


def list_factorial(list):
    if len(list) <= 1:
        return list[0]
    else:
        return list[0] + list_factorial(list[1:])

random_list = random.sample(range(100), 5)
print('\n')
print('Random list: ', random_list)
print('All sum about random list: ', list_factorial(random_list))


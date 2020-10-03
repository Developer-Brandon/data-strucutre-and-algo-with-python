import random

random_list = random.sample(range(100), 10)

def sequencial_search(list, data):
    for value in range(len(list)):
        if list[value] == data:
            return True
    return False

print('\n')
print('Random list: ', random_list)
print('\n')
test_number = 3
print('Test number: ', test_number)
print('After sequential search: ', sequencial_search(random_list, test_number))

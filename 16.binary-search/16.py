import random

def is_data_in_list(list, search_data):
    if len(list) == 1 and list[0] == search_data:
        return True
    if len(list) == 1 and list[0] != search_data:
        return False
    if len(list) == 0:
        return False

def binary_search(list, search_data):
    is_data_in_list(list, search_data)

    medium_pointer = len(list) // 2

    if search_data == list[medium_pointer]:
        return True
    else:
        if search_data < list[medium_pointer]:
            return binary_search(list[:medium_pointer], search_data)
        else:
            return binary_search(list[medium_pointer:], search_data)

random_list = random.sample(range(100), 50)
random_list.sort()
print('\n')
print('Random list: ', random_list)
print('\n')

test_number = 3
print('After binary search: ', binary_search(random_list, test_number))

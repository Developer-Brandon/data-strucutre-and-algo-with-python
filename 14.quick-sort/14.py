import random

def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        standardValue = list[0]
        left_list = [item for item in list if standardValue > item]
        right_list = [item for item in list if standardValue < item]
        return quick_sort(left_list) + [standardValue] + quick_sort(right_list)

random_list = random.sample(range(100), 50)
print('\nRandom list: ', random_list)
print('\nAfter quick sort: ', quick_sort(random_list))

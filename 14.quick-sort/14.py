import random

def quick_sort(list):
    if len(list) <= 1:
        return list
    pivot = list[0]
    left = [item for item in list[1:] if pivot > item]
    right = [item for item in list[1:] if pivot < item]
    return quick_sort(left) + [pivot] + quick_sort(right)

random_list = random.sample(range(100),10)
print('Random list: ', random_list)
print('After adjusting random list: ', quick_sort(random_list))

import random


def merge_align(list):
    if len(list) <= 1:
        return list
    else:
        middleIndex = int(len(list) / 2)
        left_list = merge_align(list[:middleIndex])
        right_list = merge_align(list[middleIndex:])
    return merge(left_list, right_list)


def merge(left_list, right_list):
    merged_list = list()
    left_pointer, right_pointer = 0, 0

    while len(left_list) > left_pointer and len(right_list) > right_pointer:
        if left_list[left_pointer] > right_list[right_pointer]:
            merged_list.append(right_list[right_pointer])
            right_pointer += 1
        else:
            merged_list.append(left_list[left_pointer])
            left_pointer += 1

    while len(left_list) > left_pointer:
        merged_list.append(left_list[left_pointer])
        left_pointer += 1

    while len(right_list) > right_pointer:
        merged_list.append(right_list[right_pointer])
        right_pointer += 1

    return merged_list


random_list = random.sample(range(100), 10)
print('\n')
print('Random list: ', random_list)
print('\n')
print('After merge sort: ', merge_align(random_list))
print('\n')

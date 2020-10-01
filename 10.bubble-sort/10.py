# import random
#
#
# def bubble_sort(data):
#     for outerIndex in range(len(data) - 1):
#         swap = False
#         for innerIndex in range(len(data) - outerIndex - 1):
#             if (data[innerIndex] > data[innerIndex + 1]):
#                 data[innerIndex], data[innerIndex + 1] = data[innerIndex + 1], data[innerIndex]
#                 swap = True
#         if swap == False:
#             break
#     return data
#
#
# random_list = random.sample(range(100), 80)
# print('\nbefore bubble sort: ', random_list ,'\n')
# print('after bubble sort: ', bubble_sort(random.sample(range(100), 50)))


import random

def bubble_sort(dataList):
    swipe = False
    for outerIndex in range(len(dataList) - 1):
        for innerIndex in range(len(dataList) - 1 - outerIndex) :
            if (dataList[innerIndex] > dataList[innerIndex + 1]):
                dataList[innerIndex], dataList[innerIndex + 1] = dataList[innerIndex + 1], dataList[innerIndex]
                swipe = True
        if swipe == False:
            break
    return dataList

randomList = random.sample(range(100), 40)
print('\n버블정렬 전: ', randomList)
print('\n버블정렬 후: ', bubble_sort(randomList))

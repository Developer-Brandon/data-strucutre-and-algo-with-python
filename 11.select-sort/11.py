import random

def selection_sort(data_list):
    for outerIndex in range(len(data_list) - 1):
        lowestIndex = outerIndex
        for innerIndex in range(outerIndex + 1, len(data_list)):
            if data_list[lowestIndex] > data_list[innerIndex]:
                lowestIndex = innerIndex
        data_list[outerIndex], data_list[lowestIndex] = data_list[lowestIndex], data_list[outerIndex]
    return data_list


randomList = random.sample(range(100), 40)

print('\n정렬 전: ', randomList)
print('\n정렬 후: ', selection_sort(randomList))

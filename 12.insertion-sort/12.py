import random

def insert_sort(dataList):
    for outerIndex in range(len(dataList)):
        for innerIndex in range(outerIndex, 0, -1):
            if dataList[innerIndex - 1] > dataList[innerIndex]:
                dataList[innerIndex - 1], dataList[innerIndex] = dataList[innerIndex], dataList[innerIndex - 1]
            else:
                break
    return dataList

data_list = random.sample(range(100), 40)

print('Before adjusting insertion sort: ', data_list)
print('After adjusting insertion sort: ', insert_sort(data_list))
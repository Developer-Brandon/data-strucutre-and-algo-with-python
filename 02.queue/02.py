'''
    1. 언어적 차원에서 지원하는 큐(Queue)로 구현
'''

import queue

print('\n\n')
data_queue = queue.Queue()
data_queue.put('brandon')
data_queue.put('cowboy_beebob')

print(data_queue)
# data_queue의 메모리 주소입니다
print(data_queue.qsize())
print(data_queue.get())
# brandon이 먼저 들어갔기 때문에, get을 하면 brandon이 먼저 빠집니다.
print(data_queue.qsize())
print('\n\n')

'''
    2. 언어적 차원에서 지원하는 우선순위 큐(Priority Queue) 구현
    - 튜플을 사용해보겠습니다
'''
br_queue = queue.PriorityQueue()
br_queue.put((10, "korea"))
br_queue.put((5, 1))
br_queue.put((15, "china"))

print(br_queue.qsize())
print(br_queue.get())
# 여기서 '오잉?' 하시는 분들 있을 수도 있는데요.
# 판단기준이 '숫자의 우선순위' 입니다. 그래서 (5,1)이 먼저 선출된 것입니다.
# 이 판단기준이 어떻게 이렇게 선정된건지는 모르겠지만 언어적 차원에서 이렇게 된것이니.. 아래 list로 구현할때에도 어쩔수 없이 이 기준으로 해야 할 듯합니다.
print("\n\n")

'''
    3. 리스트를 변수로 사용하여 큐(Queue) 구현
'''

data_list_queue = list()


def enqueue(data):
    data_list_queue.append(data)
    # 이건 list다 보니 append함수를 호출해야 합니다.


def dequeue():
    data = data_list_queue[0]
    del data_list_queue[0]
    return data


for index in range(10):
    enqueue(index)

print(len(data_list_queue))
dequeue()
print(len(data_list_queue))
print('\n\n')

'''
    4. 리스트를 변수로 사용하여 우선순위 큐(Queue) 구현
    - enqueue는 위의 enqueue를 가져다가 사용하고, dequeque의 경우 동작방식이 다르니 따로 정의해서 구현하겠습니다.
'''

data_priority_queue = list()

data_priority_queue.append((4, "semi"))
data_priority_queue.append((2, "somi"))
data_priority_queue.append((1, "sumi"))

index = data_priority_queue[0][0]


# 비교할 값이 아무거나 하나 있어야 하니 첫번째 값을 하나 뽑습니다

def priorityDequeue():
    global index
    for data in data_priority_queue:
        if (data[0] <= index):
            index = data[0]


priorityDequeue()
print(index)

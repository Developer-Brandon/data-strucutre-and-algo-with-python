'''
    1. 언어적 차원에서 지원하는 스택(Stack) 구현
    - 언어 자체에서 Stack이라는 자료구조를 제공하고 있지는 않는 걸로 알고있습니다. 혹시 아시는 분 있으시면 댓글 부탁드립니다
'''



'''
    2. 리스트를 변수로 하는 스택(Stack) 구현
'''

data_stack = list()

def push(data):
    data_stack.append(data)

def pop():
    data = data_stack[-1] # 리스트의 마지막 index
    del data_stack[-1]
    return data

def executePush():
    print('\n')
    for index in range(10):
        push(index)

def printPop():
    print(pop())
    print('\n')

#
executePush()
printPop()

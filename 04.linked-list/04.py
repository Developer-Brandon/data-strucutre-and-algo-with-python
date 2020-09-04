# 링크드 리스트 간단 구현

# 기본적인 Node를 만들기 위한 class 입니다.
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 링크드 리스트를 추가해주는 메소드입니다.
def add(data):
    node = head # 항상 head의 값을 가져와야 합니다.
    # 맨 마지막 node를 찾기위한 반복문입니다.
    while node.next: # 만약 노드가 있고, 노드가 다음을 가르키는 주소가 있다면 계속해서 아래 로직을 반복합니다
        node = node.next # 다음 노드를 가르키는 객체를 node에 덮어씌웁니다.
    node.next = Node(data)

# 링크드 리스트에 필요한 데이터를 init 해주는 메소드입니다.
def initData():
    node1 = Node(1)
    global head
    head = node1 # node1을 head 값으로 지정합니다.
    for index in range(2,10): # 1이라는 값은 이미 있으니까, 2~9까지 반복합니다. 총 1~9로 이루어진 링크드 리스트가 만들어질 예정입니다.
        add(index)

# 링크드 리스트에 필요한 데이터를 init 해주는 메소드입니다.
def printAll():
    node = head # 다시 head 값을 가져와서 node에 넣습니다
    while(node.next):
        print(node.data)
        node = node.next
    print(node.data)

##### 데이터 초기화
initData()

##### 출력
print('\n\n')
print('1.링크드 리스트 간단 구현하기')
printAll()

# 중간에 링크드 리스트 값 넣기
def insertMiddleNodeInList(data):
    node = head
    middleNode = Node(data) # 넘어온 값을 객체화하여 middelNode 변수에 삽입해줍니다.

    search = True
    while search: # node.data 에서 data 보다 작은값이 나와야, 그 뒤에 data를 삽입할 수 있으므로 아래와 같이 분기를 넣습니다
        if node.data < data:
            search = False
        else:
            node = node.next

    existingNextNodeObject = node.next # 맨 마지막 노드객체를 existingNextNodeObject 라는 변수에 넣습니다
    node.next = middleNode # 맨마지막의 노드 객체의 자리에, middleNode를 덮어씌웁니다.
    middleNode.next = existingNextNodeObject # 미들노드의 다음번째 주소값에 기존에 존재하는 nodeObject를 넣습니다


##### 출력
print('\n\n')
print('2.간단하게 구현된 링크드 리스트의 중간에 데이터 삽입하기')
insertMiddleNodeInList(1.5)
printAll()

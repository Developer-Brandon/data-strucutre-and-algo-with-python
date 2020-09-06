# 링크드 리스트 매니저와 함께 구현

# 기본적인 Node를 만들기 위한 class 입니다.
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# 노드 매니저 클래스
class NodeManager:
    def __init__(self, data):
        self.head = Node(data)

    # 맨 뒤에 노드를 더해주는 메소드 입니다.
    def add(self, data):
        node = self.head
        # node가 다음 주소값을 가르키는 next 값이 존재한다면 ...
        while node.next:  # 계속해서 node를 맨 끝 노드로 넘겨줍니다.
            node = node.next
        node.next = Node(data)  # 그리하여 맨 끝 노드에 노드객체를 생성해줍니다.

    # 노드를 삭제 시켜주는 메소드 입니다.
    # 노드를 삭제하는 과정은..
    # 삭제하고자 하는 노드를 찾고
    # 그 전 값의 next 값을 삭제하고자 하는 노드의 next 값과 연결시켜 줍니다
    def delete(self, data):
        if self.head == "":
            print('해당값을 가진 노드가 없습니다')
            return

        if self.head.data == data: # 만약 삭제하려는 데이터가 head의 데이터라면
            temp = self.head
            self.head = self.head.next # head의 next객체를, 현재 head에 덮어씌워 줍니다. next는 다음 노드의 객체를 가르키고 있으니까요.
            del temp # 그런 후에 지워줍니다
        else:
            node = self.head
            while node.next:
                if node.next.data == data: # 만약 node.next의 데이터 값이 사용자가 입력한 data값과 같다면
                    temp = node.next
                    node.next = node.next.next # node.next를 통째로 node.next.next값으로 교체 시켜줍니다
                    del temp
                    return
                else:
                    node = node.next

    # 모든 노드를 출력해주는 메소드 입니다.
    def printAllNode(self):
        print('\n\n')
        print('링크드 리스트 매니저와 함께 삭제 기능 구현하기')
        node = self.head
        # node.next가 존재하는한 계속해서 반복해줍니다.
        while node.next:
            print(node.data)
            node = node.next


##
def initialize_node_manager():
    global linked_list_manager
    linked_list_manager = NodeManager(0)


def init_data():
    for data in range(1,10):
        linked_list_manager.add(data)

initialize_node_manager()
init_data()
linked_list_manager.printAllNode()
linked_list_manager.delete(3)
linked_list_manager.printAllNode()

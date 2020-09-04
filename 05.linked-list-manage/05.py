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
    # 그 전 값의 next 값을 삭제하고자 하는 노드의 next값과 연결시켜 줍니다
    def delete(self, data):
        print('')


    # 모든 노드를 출력해주는 메소드 입니다.
    def printAllNode(self):
        node = self.head
        # node.next가 존재하는한 계속해서 반복해줍니다.
        while node.next:
            print(node.data)
            node = node.next

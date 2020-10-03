graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def bfs(graph, start_node):
    visited_node_list = list()
    node_list = list()

    node_list.append(start_node)

    while node_list:
        node = node_list.pop(0)
        if node not in visited_node_list:
            visited_node_list.append(node)
            print('visited_node_list: ', visited_node_list)
            node_list.extend(graph[node])
            print('node_list: ', node_list)
    return visited_node_list

print('\n')
print('Graph Data: ', graph)
print('\n')
print('Bfs: ', bfs(graph, 'A'))

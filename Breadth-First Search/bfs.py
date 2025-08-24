from collections import deque

class Node:
    def __init__(self, value):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({self.value})'

class Graph:
    def __init__(self, root):
        self._root = root

    def dfs(self):
        visited = []
        stack = [self._root]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                for neighbor in reversed(node.outbound):
                    stack.append(neighbor)
        return visited

    def bfs(self):
        visited = set()
        result = []
        queue = deque([self._root])
        visited.add(self._root)

        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in node.outbound:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return result

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)

g1 = Graph(a)

# print([str(node) for node in g1.dfs()])
print([str(node) for node in g1.bfs()])


a = Node('a')
b = Node('b')
c = Node('c')
a.point_to(b)
b.point_to(c)

g2 = Graph(a)

# print([str(node) for node in g2.dfs()])
print([str(node) for node in g2.bfs()])


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)
b.point_to(f)
c.point_to(e)

g3 = Graph(a)

# print([str(node) for node in g3.dfs()])
print([str(node) for node in g3.bfs()])


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')
k = Node('k')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)
a.point_to(e)
e.point_to(f)
e.point_to(g)
f.point_to(i)
f.point_to(h)
g.point_to(k)

g4 = Graph(a)

# print([str(node) for node in g4.dfs()])
print([str(node) for node in g4.bfs()])
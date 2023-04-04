# 하나의 MST 구한 후, 해당 MST에서 가장 긴 간선을 제거하면 두 개의 MST 만들어진다.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int, input().split())
parent = [i for i in range(v+1)]

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
last = 0 # MST에 포함되는 간선 중 가장 비용이 큰 간선

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent, a, b)
        result += cost
        last = cost  # sort 를 할 경우 어차피 맨 마지막이 제일 비싸니까   

print(result - last)
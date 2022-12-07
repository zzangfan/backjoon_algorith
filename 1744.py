n = int(input())
p_graph = []
n_graph = []
total = 0
for _ in range(n):
    value = int(input())
    if value >1:
        p_graph.append(value)
    elif value == 1:
        total += 1
    else:
        n_graph.append(value)

p_graph.sort(reverse=True)
n_graph.sort()


if len(p_graph)%2 == 0:
    for i in range(0,len(p_graph),2):
        total += p_graph[i] * p_graph[i+1]
else:
    for i in range(0,len(p_graph) - 1, 2):
       total += p_graph[i] * p_graph[i+1]
    total += p_graph[len(p_graph) -1 ]

if len(n_graph) % 2 == 0:
    for i in range(0, len(n_graph),2):
        total += n_graph[i] * n_graph[i+1]
else:
    for i in range(0,len(n_graph)-1,2):
        total += n_graph[i] * n_graph[i+1]
    total += n_graph[len(n_graph) -1]

print(total)
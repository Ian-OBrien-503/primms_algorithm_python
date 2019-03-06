
count = 0
graph = {}
file = open("cities.txt", "r")
for line in file:
    line = line.strip()
    line = line.split()
    key = line[0]
    dict = {line[1]: line[2]}
    if key in graph:
        graph[key].update(dict)
    else:
        graph[key] = {line[1]: line[2]}

print(graph)
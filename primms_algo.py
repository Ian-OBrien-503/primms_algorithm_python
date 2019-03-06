import math

graph = {}
dict = {}
closest_city = {}
visited_city = {}
mst = []


#build adjacency list using dict of dict
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


#basically just outputs the text file with every city listed and its distance to every other city
def output_distance_between_cities():
    for city1 in graph:
        for city2 in graph[city1]:
            print(city1, city2, (graph[city1])[city2])


def find_closest_city_from_any_city(closest_city):
    for city1 in graph:
        min_dist = math.inf
        for city2 in graph[city1]:
            dist = int(graph[city1][city2])
            if dist < min_dist:
                min_dist = dist
                closest = city2
        closest_city[city1] = {closest: min_dist}


#find the minimum spanning tree using primms algo
def primms_algo(graph, closest_city, dict):
    total_distance = 0
    root = "Albany"
    mst.append(root)
    next_city = closest_city[root]
    total_distance += (closest_city[root])[next_city]
    print(total_distance)
    print(next_city)
    print(visited_city)

find_closest_city_from_any_city(closest_city)
print(closest_city)
#primms_algo(graph, closest_city, dict)
#print(find_closest_city_from_any_city(closest_city))
#print(graph)
#print(output_distance_between_cities())

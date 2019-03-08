import math
import pprint

graph = {}
dict = {}
closest_city = {}
mst = []
unvisited = []
visited = []

def build_graph():
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
    file.close()


#basically just outputs the text file with every city listed and its distance to every other city
def output_distance_between_cities():
    for city1 in graph:
        for city2 in graph[city1]:
            print(city1, city2, (graph[city1])[city2])


#find the minimum spanning tree using primms algo
def primms_algo():

    #variables
    total_distance = 0
    for testing in graph:
        unvisited.append(testing)

    #pick arbitrary root
    root = "Albany"
    print("starting @ Albany")
    mst.append(root)
    unvisited.remove(root)
    visited.append(root)

#output_distance_between_cities()
build_graph()
pprint.pprint(graph)
#primms_algo()

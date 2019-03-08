import math
import pprint

#global variables/data structures
graph = {}
dict = {}
mst = []
unvisited = []
edge_list = {}

def build_unvisited():
    for keys in graph:
        unvisited.append(keys)


def build_graph():
    #build adjacency list using dict of dict
    file = open("cities.txt", "r")
    for line in file:
        line = line.strip()
        line = line.split()
        key = line[0]
        dict = {line[1]: int(line[2])}
        if key in graph:
            graph[key].update(dict)
        else:
            graph[key] = {line[1]: line[2]}
    file.close()


#this function finds the next closest city and edge not yet in the MST from a city in the MST
def find_next():
    min_dist = 9999
    count = 0
    for city in mst:
        x = city
        for key in graph[x]:
            if int(graph[x][key]) < min_dist and key in unvisited:
                min_dist = graph[x][key]
                temp = [x, key, graph[x][key]]
    return temp


#find the minimum spanning tree using primms algo
def prims_algo():

    #variables
    total_distance = 0

    #pick arbitrary root
    root = "Albany"
    print("starting @ Albany")
    mst.append(root)
    unvisited.remove(root)
    while unvisited:
        temp = find_next()
        unvisited.remove(temp[1])
        mst.append(temp[1])
        total_distance += temp[2]
        print("adding", temp, "to mst, new total distance:", total_distance)
        edge_list = {temp[0] : temp[1]}

    print("\n\ttotal_distance for minimum spanning tree:", total_distance)


#order here does matter for function calls
def main():
    #output_distance_between_cities()
    build_graph()
    build_unvisited()
    pprint.pprint(graph)
    prims_algo()


main()
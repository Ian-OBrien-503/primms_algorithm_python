import math

graph = {}
dict = {}
closest_city = {}
visited_city = {}
mst = []
unvisited = []

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

#builds dictonary of the closest city and its distance from any given city
def find_closest_city_from_any_city(closest_city):
    for city1 in graph:
        min_dist = math.inf
        for city2 in graph[city1]:
            dist = int(graph[city1][city2])
            if dist < min_dist:
                min_dist = dist
                closest = city2
        closest_city[city1] = {closest: min_dist}

#this function traverses existing mst to find the next vertex to add to the tree
def find_next(mst, total_distance):
    next = {}
    min_dist = 9999
    print(unvisited)
    for city in mst:
        if(city in unvisited):
            test = closest_city[city]
            for key in test:
                if test[key] < min_dist and key in unvisited:
                    min_dist = test[key]
                    next_city = key
                    next = {next_city: min_dist}
        else:
            continue
    for key in next:
        mst.append(key)
        unvisited.remove(key)
    return next


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

    #while we have visited all nodes find next node to visit and add it to tree
    while unvisited:
        test = find_next(mst, total_distance)
        for key in test:
            total_distance += test[key]
            print("visting", key, "new total distance is", total_distance)


output_distance_between_cities()
print("============\n")
find_closest_city_from_any_city(closest_city)
#print(closest_city)
primms_algo()

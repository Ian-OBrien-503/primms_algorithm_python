## Prim's Algorithm
implemented primms algorithm in python using adjacency list via a dictionary of dictionaries.

Rough definition of Prim's algorithm:  
1. pick an arbitrary starting vertex
2. add the vertex to the miniumum spanning tree & remove vertex from unvisited vertex list
3. find the next closest vertex from minimum spanning tree to vertex not yet in mimum spanning tree and is in unvisited list 
4. repeat steps 2 and 3 until we unvisited list is empty

## Build Instructions
make sure you have python intreperter installed:
 [installation instructions](https://docs.python-guide.org/starting/install3/linux/)

- clone current directory via: $ git clone https://github.com/Ian-OBrien-503/primms_algorithm_python.git
- run intrepreter/code with following: $ python primms_algo.py or $ python3 primms_algo.py

## About
I chose to develop this project using python because it seems to be the fastest language for prototyping algorithms, in my opinion. I ran into several problems trying to implement the algorithm from scratch without using any resources. I finally caved and began to look at a few resources online only to find that most of the examples used adjacency matrices rather than adjacency lists. This is a very similar approach but I chose not to use any of these sources.

I turned to "Introduction to the Design and Analysis of Algorithms" by Anany Levitin(3rd edition) section 9.1 for the pseudocode for prims algorithm.
I kept running into the issue where I would pick Albany as my starting city and then I would get Corvallis as the next closest city and added it to the minimum spanning tree. However; at this point my algorithm would then pick Albany again even though it was already in a tree, rinse and repeat, which resulted in an infinite loop.

I chose to use a dictionary of dictionaries for the adjacency list to represent the graph because it seemed like a reasonable way to represent the relationships for the distance from one city to any other city. I chose each city as a key for the outer dictionary, and then in the values for this dictionary was all adjacent cities and their distances which is essentially all edges from any city to another.

I have never used nested dictionaries before and I kept running into issues trying to reference a sub-key and other reference issues to get the right data that I was trying to get at. However; after some debugging and writing these data structures out on paper I was able to figure out and my results are below.



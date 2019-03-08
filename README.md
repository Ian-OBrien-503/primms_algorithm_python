## primms_algorithm_python  
implemented primms algorithm in python using adjacency list via a dictionary of dictionaries

## build instructions
make sure you have python intreperter installed:
 [installation instructions](https://docs.python-guide.org/starting/install3/linux/)


- make sure you have the cities.txt file in the same directiory as primms_algo.py
- run intrepreter/code with following: $ python primms_algo.py or $ python3 primms_algo.py

## about
I chose to develop this project using python because it seems to be the fastest language for prototyping algorithms, in my opinion.
I ran into several problems trying to implement the algorithm from scratch without using any resources.  I finally caved and began to look at a few
resources online only to find that most of the examples used adjacency matricies rather than adjacency lists. This is a very similar approach but
I chose not to use any of these sources.

I turned to "Introduction to the Design and Analysis of Algorithms" by Anany Levitin(3rd edition) section 9.1 for the psuedocode for primms algorithm.  
I kept running into the issue where I would pick Albany as my starting city and then I would get Corvallis as the next closest city and added it to the minumum 
spanning tree.  However; at this point my algortihm would then pick Albany again even though it was already in a tree, rinse and repeat, which resulted
in an infinite loop.  

I chose to use a dictionary of dictionaries for the adjacency list to represent the graph because it seemed like a reasonable way to represent the relationships for the distance
from one city to any other city.  I chose each city as a key for the outer dictionary, and then in the the values for this dictionary was all adjacent cities and their distances
which is essentially all edges from any city to another.  

I have never used nested dictionaries before and I kept running into issues trying to reference a sub-key and other reference issues to get the right data
that I was trying to get at.  However; after some debugging and writing these data structures out on paper I was able to figure out and my results are below.



from functools import cache 
from collections import defaultdict
import networkx as nx
import copy
with open('../data/23.dat') as f:
    lines = [(x.strip()) for x in f]

# Make a map of the lan
lan = defaultdict(list)
for line in lines:
    a ,b = line.split('-')
    lan[a].append(b)
    lan[b].append(a)

sets = []
def find_leafs(nodes, level):
    global sets
    if level == 3:
        if nodes[level]  ==  nodes[0]:
            if set(nodes[0:3]) not in sets:
                sets.append(set(nodes[0:3]))
        return
    for n in lan[nodes[level]]:
        if level < 2 and n == nodes[0] : continue # skip back links 
        nodes.append(n)
        find_leafs(nodes,level +1)
        nodes.pop()
    return

def part1():
    for name in lan.keys():
        if name[0] == 't':
            nodes = [name]
            find_leafs(nodes,0)
    print(len(sets))

#part1()



# node = 'co'
# #b = lan[node].append(node)
# b = set(lan[node])
# b.add(node)
# for n in lan[node]:
#     c = set(lan[n])
#     c.add(n)
#     print(c)
#     print(b)

#     b = b.intersection(c)

# This must be an exampel of finding all maximal cliques in an undirected graph    
# Bron–Kerbosch algorithm is an enumeration algorithm for this
# https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm

sets = []
def BronKerbosch1(R, P, X):
    global sets
    if len(P) == 0 and len(X) == 0 :
        if R not in sets:
            sets.append(R)
#        print(R)
    for v in P:
        P2 = copy.copy(P)
        N = set(lan[v])
        BronKerbosch1(R.union(set([v])), P2.intersection(N), X.intersection(N))
        P2.remove(v)
        X.add(v)

p = set(lan.keys())
r = set()
x = set()
#BronKerbosch1(r,p,x)
# THIS is too slow it seems,


# Looking at web some solutions, a recursive ting should work here also

# An nice library also exists,
# and https://networkx.org which can do it directly.

G = nx.Graph()
for line in lines:
    a ,b = line.split('-')
    G.add_edge(a,b)

','.join(sorted(max(nx.find_cliques(G), key=len)))


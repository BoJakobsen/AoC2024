import math
with open("../data/16.dat") as f:
    ma = [list((x.strip())) for x in f]

nl = len(ma)
nc = len(ma[0])

dist = {}
orien= {}
prev = {}
Q = {}

# find start point
for l in range(nl):
    for c in range(nc):
        if ma[l][c] == 'S':
            pos0 = (l,c)
            dist[(l,c)] = 0
            prev[(l,c)] = float('nan')
            Q[(l,c)] = 0
            orien[(l,c)]= (0,1)
        if ma[l][c] == 'E':
            end0 = (l,c)
            prev[(l,c)] = float('nan')
            dist[(l,c)] = float('inf')
            Q[(l,c)] = float("inf")
            orien[(l,c)]= float('nan')
        if ma[l][c] == ".":
            dist[(l,c)] = float('inf')
            prev[(l,c)] = float('nan')
            Q[(l,c)]=float("inf")
            orien[(l,c)]= float('nan')            

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for l in ma:
    print(*l)

while len(Q) > 0:
    u = min(Q, key = Q.get)
    Q.pop(u)
    if u == end0: break
    for dir in dirs:
        v = tupadd(u,dir)
        if v in Q: # still a valid direction
            if orien[u] == dir:
                alt = dist[u] + 1
            else:
                alt = dist[u] + 1 + 1000
            if alt < dist[v]:
                dist[v] = alt
                Q[v] = alt
                prev[v] = u
                orien[v] = dir
        
S= []
D= []
u = end0
while u == u: # very strange way to test for nan
    S.append(u)
    D.append(orien[u])
    u = prev[u]

res = 0
lastD=D[0]
for kk in range(1,len(D)):
    if D[kk] != lastD:
        res += 1000
    lastD=D[kk]
res += len(S)-1
print(res)

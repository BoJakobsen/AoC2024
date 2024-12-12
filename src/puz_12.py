#Snippets is loaded before running this

#lines = baseloader('../data/12_test.dat')
lines = baseloader('../data/12.dat')


dat = defaultdict(list)
for Nll, ll in enumerate(lines):
    for Ncc, cc in enumerate(ll):
        dat[cc].append((Nll,Ncc))

# get all nab points, within bound
def get_nab(coord):
    dirs=[(1,0), (0,1), (-1,0), (0,-1)]
    nabs=[]
    for d in dirs:
        if checkbound(lines, tupadd(d,coord)):
            nabs.append(tupadd(d,coord))
    return nabs

# get all nab points, ignoring bound
def get_nab2(coord):
    dirs=[(1,0), (0,1), (-1,0), (0,-1)]
    nabs=[]
    for d in dirs:
        nabs.append(tupadd(d,coord))
    return nabs


def is_nab(coord,coord0):
    return coord in get_nab(coord0)


# Find the distinct connected regions
groups = defaultdict(list)
for kind in dat.keys():
    poss = copy.copy(dat[kind])
    while len(poss)>0:
        grp = [poss[0]]  # add first poss to the grp
        poss.remove(grp[0])  # remove from list
        added = True
        while added:
            added = False 
            for pos in poss:  # check if we can add a number
                nab = get_nab(pos)
                if set(nab).intersection(set(grp)):  # is nab a nabou
                    grp.append(pos)
                    poss.remove(pos)
                    added = True
                    break
        groups[kind].append(grp)
 
# Problem 1 can now easily be calculated
res = 0
for regs in groups.values():
    for reg in regs:
        ares = len(reg)
        per = 0
        for point in reg:
            per += 4-len(set(get_nab2(point)).intersection(set(reg)))
        res += ares * per
print(res)

# Helper fuction
def minmax(reg):
    minl = len(lines)
    maxl = 0
    minc = len(lines[0])
    maxc = 0
    for p in reg:
        if p[0] < minl :
            minl = p[0]
        if p[0] > maxl :
            maxl = p[0]
        if p[1] < minc :
            minc = p[1]
        if p[1] > maxc :
            maxc = p[1]
    return minl,maxl,minc,maxc
            
        
    


# Problem 2

res = 0
for key , regs in groups.items():
    for reg in regs:
        bound = minmax(reg) # line char
        sides = 0
        # count horizontal
        for l in range(bound[0]-2,bound[1]+3):
            ingrp_down = False
            ingrp_up = False
            for c in range(bound[2]-1,bound[3]+2):
                if not ingrp_down and (l+1,c) in reg and (l,c) not in reg: 
                    ingrp_down = True
        #            print("start")
        #            print(l,c)
                    sides += 1
                if ingrp_down and ((l+1,c) not in reg or (l,c)  in reg): 
                    ingrp_down = False
                if not ingrp_up and (l-1,c) in reg and (l,c) not in reg: 
                    ingrp_up = True
        #            print("start")
        #            print(l,c)
                    sides += 1
                if ingrp_up and ((l-1,c) not in reg or (l,c)  in reg): 
                    ingrp_up = False

        # count vertical
        for c in range(bound[2]-2,bound[3]+3):
            ingrp_left = False
            ingrp_right = False
            for l in range(bound[0]-1,bound[1]+2):
                if not ingrp_right and (l,c+1) in reg and (l,c) not in reg: 
                    ingrp_right = True
        #            print("start")
        #            print(l,c)
                    sides += 1
                if ingrp_right and ((l,c+1) not in reg or (l,c)  in reg): 
                    ingrp_right = False
                if not ingrp_left and (l,c-1) in reg and (l,c) not in reg: 
                    ingrp_left = True
        #            print("start")
        #            print(l,c)
                    sides += 1
                if ingrp_left and ((l,c-1) not in reg or (l,c)  in reg): # end of grp
                    ingrp_left = False
        res += sides * len(reg)
print(res)

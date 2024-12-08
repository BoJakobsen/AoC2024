# Some usefully stuff for working with AoC problems
# Potentially nice to  just run before slowing

# Libs often used
import numpy as np
import itertools
import re


# basic loader
def baseloader(filename):
    with open(filename) as f:
        lines = [(x.strip()) for x in f]
    return lines


# Nice for working with tuples representing coordinates
def tupadd(a, b):
    res = tuple(map(lambda i, j: i + j, a, b))
    return res


# map is given as list of strings (og lists)
# coordinate as tuple
def checkbound(lines, coord):
    res = coord[0] >= 0 and coord[0] < len(lines) and coord[1] >= 0 and coord[1] < len(lines[0])
    return res


# Mapping a map to a dict with coordinates of the points
# basechar is the one "not to map" (empty points in map)
def maptodict(lines, basechar):
    pos = {}
    for ll in range(len(lines)):
        for cc in range(len(lines[ll])):
            char = lines[ll][cc]
            if char not in basechar:
                if char in pos:
                    pos[char].add(((ll, cc)))
                else:
                    pos[char] = set()
                    pos[char].add((ll, cc))
    return pos


# Links to other AoC resources

# Nice list of python snippets from AoC
# https://www.reddit.com/r/adventofcode/comments/1gsl4fm/share_your_favorite_tricks_and_snippets/


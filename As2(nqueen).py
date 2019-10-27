# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 21:56:09 2019

@author: Freakky7781_VRikk
"""
import copy
from nltk import flatten

b = ' '
final = [[1,2,3],[4,5,6],[7,8,b]]

def pprint(matrix):
    for i in matrix:
        print("  [{}  {}  {}]".format(i[0], i[1], i[2]))
    print()

def gettilepos(matrix):
    for i in matrix:
        if b in i:
            return [matrix.index(i), i.index(b)]

def getneighbours(matrix, pos):
    x, y = pos
    coordinates = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
    for i in list(coordinates):
        if -1 in i or 3 in i:
            coordinates.remove(i)
    return coordinates

def compare(matrix, possible_matrix_list):
    cost = []
    for possible_matrix in possible_matrix_list:
        matrix_cost = 0
        possible_matrix = flatten(possible_matrix)
        final_matrix = flatten(matrix)
        for i, j in zip(final_matrix, possible_matrix):
            if i == b:
                pass
            elif i != j:
                matrix_cost += 1
        cost.append(matrix_cost)
    return cost

current = [[1,2,3],[b,4,6],[7,5,8]]
min_cost, counter = 999, 0
pprint(current)
while min_cost != 0:
    pos = gettilepos(current)
    neighbours = getneighbours(current, pos)
    outcomes = []
    for n in neighbours:
        temp = copy.deepcopy(current)
        x, y = n
        tx, ty = pos
        temp[x][y] = b
        temp[tx][ty] = current[x][y]
        outcomes.append(temp)
    cost = compare(final, outcomes)
    min_cost = min(cost)
    current = outcomes[cost.index(min_cost)]
    pprint(current)
    counter += 1
print("Total steps : ", counter)
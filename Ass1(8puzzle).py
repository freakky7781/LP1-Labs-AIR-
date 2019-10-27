# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 06:56:05 2019

@author: Freakky7781_VRikk
"""
from nltk import flatten
import copy
b='_'

final= [[1,2,3],[4,5,6],[7,8,b]]
def getupos(matrix):
    for i in matrix:
        if b in i:
            return [matrix.index(i),i.index(b)]
                
def compare(matrix,possible_matrix):
    cost=[]
    for possible in possible_matrix:
        mat_cost=0
        possible=flatten(possible)
        matrix=flatten(matrix)
        for i,j in zip(matrix,possible):
            if i==b:
                pass
            elif(i!=j):
                mat_cost+=1
        cost.append(mat_cost)
    return cost
def getneighbour(matrix,pos):
    x,y=pos
    coord=[[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
    for i in list(coord):
        if -1 in i or 3 in i:
            coord.remove(i)
    return coord
def printmatrix(matrix):
    for i in matrix:
        for j in i:
            print(j,end=" ")
        print()
current=[[1,2,3],[b,4,6],[7,5,8]]
min_cost,steps=999,0
printmatrix(current)
while min_cost!=0:
    upos=getupos(current)
    outcomes=[]
    neighbour=getneighbour(current,upos)
    for i in neighbour:
        temp=copy.deepcopy(current)
        x,y=i
        uposx,uposy=upos
        temp[uposx][uposy]=temp[x][y]
        temp[x][y]=b
        outcomes.append(temp)
    
    cost=compare(final,outcomes)
    min_cost=min(cost)
    current=outcomes[cost.index(min_cost)]
    printmatrix(current)
    steps+=1
    print(min_cost)

print("total steps requied were",steps)
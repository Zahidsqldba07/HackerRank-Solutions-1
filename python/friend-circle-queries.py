#!/bin/python3

import math
import os
import random
import re
import sys

class DisjointSet:
    _disjoint_set = list()

    def __init__(self, queries):
        uniqElements = set()
        for query in queries:
            uniqElements = uniqElements.union(set(query))
            # for elem in query:
            #     if elem not in uniqElements:
            #         uniqElements.add(elem)
        for elem in uniqElements:
            self._disjoint_set.append([elem])
        # self._disjoint_set = [i for i in range(10**9)]
        print(self._disjoint_set)

    def _find_index(self, elem):
        for item in self._disjoint_set:
            if elem in item:
                return self._disjoint_set.index(item)
        return None

    def union(self, elem1, elem2):
        index1 = self._find_index(elem1)
        index2 = self._find_index(elem2)
        if (index1 != index2 and index1 is not None and index2 is not None):
            self._disjoint_set[index2] = self._disjoint_set[index2] + self._disjoint_set[index1]
            del self._disjoint_set[index1]

    def get(self):  
        print(self._disjoint_set)
        return self._disjoint_set

# Complete the maxCircle function below.
def maxCircle2(queries):
    calculatedMax = []

    try:
        disjointSet = DisjointSet(queries)
        for query in queries:
            disjointSet.union(query[0], query[1])
            maxLen = 0
            for disjointSetElement in disjointSet.get():
                maxLen = len(disjointSetElement) if len(disjointSetElement) > maxLen else maxLen
            calculatedMax.append(maxLen)
    except RuntimeError as ex:
        print(str(ex))

    # friends = []
    # for query in queries:
    #     if len(friends) == 0:
    #         friends.append(set(query))
    #     else:
    #         for person in query:
    #             for i, friend in enumerate(friends):
    #                 if person in friend:
    #                     friends[i] = friend.union(set(query))

    #                     for j, friendInOtherPair in enumerate(friends):
    #                         if person in friendInOtherPair:
    #                             friends[i] = friends[i].union(set(friendInOtherPair))
    #                             friendInOtherPair.clear()

    #                     break
    #             else:
    #                 friends.append(set(query))
    #             print(str(friends))
    #     maxLen = 0
    #     for friend in friends:
    #         maxLen = len(friend) if len(friend) > maxLen else maxLen
    #     calculatedMax.append(maxLen)

    return calculatedMax

def init_cmp(mp,x,y):
    if x not in mp:
        mp[x]=x
    if y not in mp:
        mp[y]=y

def init_cc(cc,x,y):
    if x not in cc:
        cc[x]=1
    if y not in cc:
        cc[y]=1

def get_parent(mp,x):
    while mp[x]!=x:
        x=mp[x]
    return x

# Complete the maxCircle function below.
def maxCircle(queries):
    mp = {}
    cc = {}
    max_gp = 0
    res = []
    for q in queries:
        init_cmp(mp,q[0],q[1])
        init_cc(cc,q[0],q[1])
        p1 = get_parent(mp,q[0])
        p2 = get_parent(mp,q[1])
        if p1!=p2:
            if cc[p1]>cc[p2]:
                mp[p2]=p1
                cc[p1]=cc[p1]+cc[p2]
            else:
                mp[p1]=p2
                cc[p2]=cc[p1]+cc[p2]
            max_gp = max(max_gp,max(cc[p1],cc[p2]))
        res.append(max_gp)
    return res 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

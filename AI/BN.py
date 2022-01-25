# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes

GRUPO 7:
86466 - Madalena Pedreira
86496 - Pedro Custodio
"""

import numpy as np
import itertools

class Node():
    def __init__(self, prob, parents):
        if len(parents) == 0:
            self.prob = prob[0]
        else:
            self.prob = prob # [[.001,.29],[.94,.95]]
        self.parents = parents # [0,1]
    
    def computeProb(self, evid): #(0,1,1,1,1)
        res = self.prob
        for p in self.parents:
            res = res[evid[p]]
        return [1-res,res]

    
class BN():
    def __init__(self, gra, prob):
        self.gra = gra  
        self.prob = prob #[p1,p2,p3,p4,p5]

    def computePostProb(self, evid): #evid : -1 (quero calcular)| [] (desconhecido)
        count = 0
        for e in evid:   
            if e == []:
                count +=1

        lst = list(itertools.product([0,1], repeat = count))
        
        pt = 0
        ev = [] 
        pos = 0
        neg = 0
   
        for i in lst: #calcula positivas
            pt = 0
            ev = []
            for e in evid:
                if e == -1:
                    ev.append(1)
                elif e == []:
                    ev.append(i[pt])
                    pt += 1
                else:
                    ev.append(e)
            pos += self.computeJointProb(tuple(ev))

        for i in lst: #calcula negativas
            pt = 0
            ev = []
            for e in evid:
                if e == -1:
                    ev.append(0)
                elif e == []:
                    ev.append(i[pt])
                    pt += 1
                else:
                    ev.append(e)
            neg += self.computeJointProb(tuple(ev))
        
        return pos/(pos+neg)
    
        
    def computeJointProb(self, evid):
        res = 1
        for n in self.prob:
            res *= n.computeProb(evid)[evid[self.prob.index(n)]]
        return res

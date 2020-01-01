# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 13:34:26 2019

@author: ishita
"""
import numpy as np

class NeuralNetwork :
    def __init__(self):
        self.inputlayer = 2;
        self.hiddentlayer1 = 8;#bias,dis obstacle,height obstacle,bias,gap,bird,speed,width obstacle
      #  self.hiddentlayer2 = 4;
        self.outputlayer = 2;
        self.W1 = np.random.rand(self.inputlayer,self.hiddentlayer1);
        self.W2 = np.random.rand(self.hiddentlayer1,self.outputlayer);
        
    def Z(self,input):
        z1 = np.dot(input,self.W1);
        g1 = np.tanh(z1);
        z2 = np.dot(g1,self.W2);
        g2 = np.tanh(z2);
        return g2;
    
    def sigoid(self,z):
        return 1 / (1 + np.exp(-z));


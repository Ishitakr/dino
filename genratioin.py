# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 15:18:24 2019

@author: ishita
"""

import random
import copy
from neuralnetwork import NeuralNetwork

class Generation:
    def __init__(self):
        self.population = 50;
        self.genomes = [];
        self.bestfit = 10;
        self.mutation = 0.1;
        self.keep_best = 10;
    
    def initiate_genomes(self):
        genomes = [];
        for i in range(self.population):
            genomes.append(NeuralNetwork);
        return genomes
   
    def set_genome(self,genomes):
        self.genomes = genomes;
    
    def keep_best_genome(self):
        self.genomes.sort(key = lambda x:x.fitness,reverse = True);
        self.best = self.genomes[: self.bestfit];
        self.copy = copy.deepcopy(self.best[:]);
        
    def decide_weights(self,weights):
        if random.uniform(0,1) < self.mutation:
            return weights * (random.uniform(0,1) * 5) - (random.uniform(0,1) - 0.5);
        else:
            return 0;
        
    def assign_weights(self,genomes):
        new_genome = copy.deepcopy(genomes);
        new_genome.W1 += self.decide_weights(new_genome.W1);
        new_genome.W2 += self.decide_weights(new_genome.W2);
        return new_genome
    
    def cross_over(self, genome1, genome2):
        new_genome = copy.deepcopy(genome1)
        other_genome = copy.deepcopy(genome2)
    
        cut_location = int(len(new_genome.W1) * random.uniform(0, 1))
        for i in range(cut_location):
          new_genome.W1[i], other_genome.W1[i] = other_genome.W1[i], new_genome.W1[i]
    
        cut_location = int(len(new_genome.W2) * random.uniform(0, 1))
        for i in range(cut_location):
          new_genome.W2[i], other_genome.W2[i] = other_genome.W2[i], new_genome.W2[i]
    
        cut_location = int(len(new_genome.W3) * random.uniform(0, 1))
        
        return new_genome
    
    def mutations(self):
        while len(self.genomes) < self.keep_best * 4:
          genome1 = random.choice(self.best_genomes)
          genome2 = random.choice(self.best_genomes)
          self.genomes.append(self.mutate(self.cross_over(genome1, genome2)))
    
        while len(self.genomes) < self.population:
          genome = random.choice(self.best_genomes)
          self.genomes.append(self.mutate(genome))
    
        random.shuffle(self.genomes)
    
        return self.genomes

        
        
    
    
            
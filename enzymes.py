#!/usr/bin/env python

#color setting
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

#import public module
import sys
import math
import re
import csv
import os
import shutil
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import *

#import functions
from functions import Reactions
from functions import Showdata
from functions import Simulation
from functions import Compose
from functions import Decompose

class YciV:#RNA/ssDNA exonuclease 5' -> 3'specific
    def __init__(self):
        pass

    def propensity(self, state, k):
        return

    def execute(self, location, mseq, state):
        return

class YdaV:#Rac prophage; predicted DNA replication protein
    def __init__(self):
        pass

    def propensity(self, state, k):
        return

    def execute(self, location, mseq, state):
        return

class zinc_binding_phosphatase:#zinc-binding phosphatase
    def __init__(self):
        pass

    def propensity(self, state, k):
        return

    def execute(self, location, mseq, state):
        return

class CrfC:#Clamp-binding sister replication fork colocalization protein
    def __init__(self):
        pass

    def propensity(self, state, k):
        return

    def execute(self, location, mseq, state):
        return

class RarA:#recombination factor
    def __init__(self):
        pass

    def propensity(self, state, k):
        return

    def execute(self, location, mseq, state):
        return

class Hda:#regulator of DnaA that prevents premature reinitiation of DNA replication
    def __init__(self):
        pass

    def propensity(self, state, k):
        return

    def execute(self, location, mseq, state):
        return

class DnaA_initiator_associating_factor:#DnaA initiator-associating factor for replication initiation
    def __init__(self):
        pass

    def propensity(self, state, k):
        return

    def execute(self, location, mseq, state):
        return

class DNA_polymerase_III_holoenzyme:
    def __init__(self):
        pass

    def propensity(self, state, k):
        return

    def execute(self, location, mseq, state):
        return

class Tus:#DNA-binding protein; inhibition of replication at Ter sites
    def __init__(self):
        pass

    def propensity(self, state, k):
        return

    def execute(self, location, mseq, state):
        return

class DnaC:#chromosome replication; initiation and chain elongation
    def __init__(self):
        pass

    def propensity(self, state, k):
        return

    def execute(self, location, mseq, state):
        return

class Dam:#DNA adenine methyltransferase
    def __init__(self):
        pass

    def propensity(self, state, k):
        return

    def execute(self, location, mseq, state):
        return

class primosome:
    def __init__(self,k):
        self.k = k

    def propensity(self, state):
        self.p = self.k
        self.p = self.p * state[Reactions().Getindex('primosome',state)][1]
        return self.p

    def execute(self, location, mseq, state):
        if location >= 1 : mseq[location-1][Reactions().Getindex('primosome',state)] = 0
        mseq[location][Reactions().Getindex('primosome',state)] = 1
        mseq[location][Reactions().Getindex('ds',state)] = 1
        return location, mseq, state
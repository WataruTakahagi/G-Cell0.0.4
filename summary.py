#!/usr/bin/env python

#color setting
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

#import public module
import csv
import os

name = raw_input(YELLOW+'Input dir name : '+ENDC)
if os.path.exists(name):
    os.chdir(os.getcwd()+'/'+name)
    os.system('open *.png')
else:print GREEN+name+RED+' NOT EXITSTS!!'+ENDC
if os.path.exists('mutationseq.txt'):
    f = open('mutationseq.txt','r').read()
    print BLUE+"{0:-^66}".format('MUTATION')+ENDC
    MUTATION, target = f.count('M'), f
    print RED+'MUTATION '+ENDC+ '= '+`float(MUTATION/float(len(target)))*100`+' ('+`MUTATION`+'/'+`len(target)`+')'+GREEN+' (%)'+ENDC
    print BLUE+"{0:->66}".format('-')+ENDC
"""
if os.path.exists('substances.csv'):
    f = open('substances.csv','r')
    f = csv.reader(f)
    print BLUE+"{0:-^46}".format('SUMMARY')+ENDC
    for line in f:
        if line[1] == 0:print RED+'NG '+ENDC+': '+RED+"{:<5}".format(line[0])+ENDC+"{:>33}".format(' = ')+BLUE+line[1]+ENDC
        else:print GREEN+'OK '+ENDC+': '+GREEN+"{:<5}".format(line[0])+ENDC+"{:>33}".format(' = ')+BLUE+line[1]+ENDC
    print BLUE+"{0:->46}".format('-')+ENDC
"""
if os.path.exists('summary.csv'):
    f = open('summary.csv','r')
    f = csv.reader(f)
    print BLUE+"{0:-^66}".format('SUMMARY')+ENDC
    for line in f:
        print GREEN+"{:<60}".format(line[0])+ENDC+"{:>1}".format(' = ')+BLUE+line[1]+ENDC
    print BLUE+"{0:->66}".format('-')+ENDC
if os.path.exists('profile.py'):
    os.system('python profile.py')

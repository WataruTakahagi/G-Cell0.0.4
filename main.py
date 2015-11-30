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
import glob

#import whole-ecoli replication module
from functions import *
from proteins import *

#setup
time, SubList, events = Reactions().setup()
target = Reactions().Target('mutationseq.txt')

#Substance generate
Reactions().Monomer('YciV',600,SubList,target)#RNA/ssDNA exonuclease 5'->3'specific(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=G6634-MONOMER)
Reactions().Monomer('YdaV',600,SubList,target)#Rac prophage; predicted DNA replication protein(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=G6684-MONOMER)
Reactions().Monomer('YcdX',600,SubList,target)#zinc-binding phosphatase(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=G6540-MONOMER)
Reactions().Monomer('CrfC',600,SubList,target)#Clamp-binding sister replication fork colocalization protein(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG11210-MONOMER)
Reactions().Monomer('RarA',600,SubList,target)#recombination factor(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG12690-MONOMER)
Reactions().Monomer('Hda',600,SubList,target)#regulator of DnaA that prevents premature reinitiation of DNA replication(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=G7313-MONOMER)
Reactions().Monomer('DiaA',600,SubList,target)#DnaA initiator-associating factor for replication initiation(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=YRAO-MONOMER)
Reactions().Monomer('HolB',600,SubList,target)#DNA polymerase III, delta prime subunit(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG11500-MONOMER)
Reactions().Monomer('HolA',600,SubList,target)#DNA polymerase III, delta subunit(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG11412-MONOMER)
Reactions().Monomer('Tus',600,SubList,target)#DNA-binding protein; inhibition of replication at Ter sites(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG11038-MONOMER)
Reactions().Monomer('DnaC',600,SubList,target)#chromosome replication; initiation and chain elongation(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10237-MONOMER)
Reactions().Monomer('Dam',600,SubList,target)#DNA adenine methyltransferase(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10204-MONOMER)
Reactions().Monomer('DnaG',600,SubList,target)#DNA primase(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10239-MONOMER)
Reactions().Monomer('DnaN',600,SubList,target)#DNA polymerase III, beta subunit(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10242-MONOMER)
Reactions().Monomer('DnaT',600,SubList,target)#primosomal protein DnaT(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10244-MONOMER)
Reactions().Monomer('Rep',600,SubList,target)#Rep helicase, a single-stranded DNA dependent ATPase(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10837-MONOMER)
Reactions().Monomer('PriB',600,SubList,target)#primosomal replication protein N(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10764-MONOMER)
Reactions().Monomer('DnaQ',600,SubList,target)#DNA polymerase III, epsilon subunit(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10243-MONOMER)
Reactions().Monomer('DnaA',600,SubList,target)#chromosomal replication initiator protein DnaA; DNA-binding transcriptional dual regulator(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=PD03831)
Reactions().Monomer('MukE',600,SubList,target)#protein involved in chromosome partitioning(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG11252-MONOMER)
Reactions().Monomer('MukB',600,SubList,target)#cell division protein involved in chromosome partitioning(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10618-MONOMER)
Reactions().Monomer('MukF',600,SubList,target)#MukF dimer(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG12165-MONOMER)
Reactions().Monomer('NrdD',600,SubList,target)#ribonucleoside-triphosphate reductase(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=RIBONUCLEOSIDE-TRIP-REDUCT-MONOMER)
Reactions().Monomer('RecQ',600,SubList,target)#ATP-dependent DNA helicase(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10833-MONOMER)
Reactions().Monomer('DinB',600,SubList,target)#DNA polymerase IV (Y-family DNA polymerase; translesion DNA synthesis)(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=G6115-MONOMER)
Reactions().Monomer('NrdB',600,SubList,target)#ribonucleoside diphosphate reductase 1, beta subunit dimer(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=NRDB-MONOMER)
Reactions().Monomer('NrdE',600,SubList,target)#ribonucleoside-diphosphate reductase 2, alpha subunit dimer(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=NRDE-MONOMER)
Reactions().Monomer('NrdF',600,SubList,target)#ribonucleoside-diphosphate reductase 2, beta subunit dimer(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=NRDF-MONOMER)
Reactions().Monomer('HolC',600,SubList,target)#DNA polymerase III, chi subunit(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG11413-MONOMER)
Reactions().Monomer('HolD',600,SubList,target)#DNA polymerase III, psi subunit(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG11414-MONOMER)
Reactions().Monomer('LigB',600,SubList,target)#DNA ligase(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG11334-MONOMER)
Reactions().Monomer('PriA',600,SubList,target)#primosome factor N'(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10763-MONOMER)
Reactions().Monomer('LigA',600,SubList,target)#DNA ligase(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10534-MONOMER)
Reactions().Monomer('SbcC',600,SubList,target)#ATP-dependent dsDNA exonuclease(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10927-MONOMER)
Reactions().Monomer('DnaE',600,SubList,target)#DNA polymerase III, alpha subunit(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10927-MONOMER)
Reactions().Monomer('Ssb',600,SubList,target)#ssDNA-binding protein(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10976-MONOMER)
Reactions().Monomer('SbcD',600,SubList,target)#ATP-dependent dsDNA exonuclease(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG11094-MONOMER)
Reactions().Monomer('DnaB',600,SubList,target)#replicative DNA helicase(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10236-MONOMER)
Reactions().Monomer('HolE',600,SubList,target)#DNA polymerase III, theta subunit(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG11505-MONOMER)
Reactions().Monomer('RecF',600,SubList,target)#ssDNA and dsDNA binding, ATP binding(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10828-MONOMER)
Reactions().Monomer('LexA',600,SubList,target)#LexA DNA-binding transcriptional repressor(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=PD00205)
Reactions().Monomer('DnaK',600,SubList,target)#chaperone protein DnaK(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10241-MONOMER)
Reactions().Monomer('DnaJ',600,SubList,target)#chaperone protein DnaJ(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10240-MONOMER)
Reactions().Monomer('MutT',600,SubList,target)#8-oxo-dGTP diphosphatase(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10626-MONOMER)
Reactions().Monomer('DnaX',600,SubList,target)#DNA polymerase III, tau subunit dimer(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10245-MONOMER)
Reactions().Monomer('GspB',600,SubList,target)#calcium-binding protein required for initiation of chromosome replication(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG11263-MONOMER)
Reactions().Monomer('UvrD',600,SubList,target)#ssDNA translocase and dsDNA helicase - DNA helicase II(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG11064-MONOMER)
Reactions().Monomer('PolA',600,SubList,target)#DNA polymerase I, 5'-->3'polymerase, 5'-->3'and3'-->5'exonuclease(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10746-MONOMER)
Reactions().Monomer('NrdA',600,SubList,target)#ribonucleoside diphosphate reductase 1, alpha atom fun subunit dimer(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=NRDA-MONOMER)
Reactions().Monomer('PriC',600,SubList,target)#primosomal replication protein N''(http://ecocyc.org/ECOLI/NEW-IMAGE?type=ENZYME&object=EG10765-MONOMER)
Reactions().Complex('primosome',0,SubList)
Reactions().Complex('replicative_DNA_helicase',0,SubList)
Reactions().Complex('primosomal_protein_DnaT',0,SubList)
Reactions().Complex('primosomal_replication_protein_N',0,SubList)
Reactions().Complex('primosome_factor_N_ap',0,SubList)
Reactions().Complex('primosomal_replication_protein_N_ap2',0,SubList)
Reactions().Complex('DNA_primase',0,SubList)
Reactions().Complex('DNA_polymerase_III_holoenzyme',0,SubList)
Reactions().Complex('DNA_polymerase_III_core_enzyme',0,SubList)
Reactions().Complex('DNA_polymerase_III_preinitiation_complex',0,SubList)
Reactions().Complex('DNA_polymerase_III_beta_subunit',0,SubList)
Reactions().Complex('DNA_polymerase_III_tau_subunit_dimer',0,SubList)
Reactions().Complex('DNA_polymerase_III_psi_chi_subunit',0,SubList)

#Sequence data
seq, mod = Reactions().Readseq(target,SubList)
Reactions().Increase(0,'DnaB',mod,SubList)
Reactions().Increase(0,'DnaB',mod,SubList)
Reactions().Decrease(0,'DnaA',mod,SubList)

"""
#run process
logt, logd, t, tend = Showdata().logger(time, SubList, 0, 0.01)

#primosome
Reactions().Events(Compose('replicative_DNA_helicase',['DnaB'],[6],1.0e-9),events)
Reactions().Events(Compose('primosomal_protein_DnaT',['DnaT'],[3],1.0e-2),events)
Reactions().Events(Compose('primosomal_replication_protein_N',['PriB'],[2],5.0e-1),events)
Reactions().Events(Compose('primosome',['replicative_DNA_helicase','primosomal_protein_DnaT','primosomal_replication_protein_N','PriA','PriC','DnaG'],[1,1,1,1,1,1],1.0e-8),events)
Reactions().Events(Decompose('replicative_DNA_helicase',['DnaB'],[6],10),events)
Reactions().Events(Decompose('primosomal_protein_DnaT',['DnaT'],[3],1),events)
Reactions().Events(Decompose('primosomal_replication_protein_N',['PriB'],[2],1),events)
Reactions().Events(Decompose('primosome',['replicative_DNA_helicase','primosomal_protein_DnaT','primosomal_replication_protein_N','PriA','PriC','DnaG'],[1,1,1,1,1,1],10),events)
#Reactions().Events(primosome(0,mod,0.00),events)#delete location info.

#DNA_polymerase_III_holoenzyme
Reactions().Events(Compose('DNA_polymerase_III_core_enzyme',['DnaE','DnaQ','HolE'],[1,1,1],1.0e-2),events)
Reactions().Events(Compose('DNA_polymerase_III_preinitiation_complex',['DnaX','HolB','HolA'],[3,1,1],1.0e-9),events)
Reactions().Events(Compose('DNA_polymerase_III_beta_subunit',['DnaN'],[2],5.0e-1),events)
Reactions().Events(Compose('DNA_polymerase_III_tau_subunit_dimer',['DnaX'],[2],5.0e-1),events)
Reactions().Events(Compose('DNA_polymerase_III_psi_chi_subunit',['HolC','HolD'],[1,1],5.0e-1),events)
Reactions().Events(Compose('DNA_polymerase_III_holoenzyme',['DNA_polymerase_III_core_enzyme','DNA_polymerase_III_preinitiation_complex','DNA_polymerase_III_beta_subunit','DNA_polymerase_III_tau_subunit_dimer','DNA_polymerase_III_psi_chi_subunit'],[3,1,2,1,4],1.0e-15),events)
#Reactions().Events(DNA_polymerase_III_holoenzyme(0,mod,0.00),events)

#simulation
Simulation().Run(t, tend, SubList, events, logt, logd, mod)

#showdata, make .png
Showdata().png(['DnaB','replicative_DNA_helicase'], logt, logd, SubList,'default')
Showdata().png(['DnaT','primosomal_protein_DnaT'], logt, logd, SubList,'default')
Showdata().png(['PriB','primosomal_replication_protein_N'], logt, logd, SubList,'default')
Showdata().png(['replicative_DNA_helicase','primosomal_protein_DnaT','primosomal_replication_protein_N','PriA','PriC','DnaG','primosome'], logt, logd, SubList,'default')

Showdata().png(['DnaE','DnaQ','HolE','DNA_polymerase_III_core_enzyme'], logt, logd, SubList,'default')
Showdata().png(['DnaX','HolB','HolA','DNA_polymerase_III_preinitiation_complex'], logt, logd, SubList,'default')
Showdata().png(['DnaN','DNA_polymerase_III_beta_subunit'], logt, logd, SubList,'default')
Showdata().png(['DnaX','DNA_polymerase_III_tau_subunit_dimer'], logt, logd, SubList,'default')
Showdata().png(['HolC','HolD','DNA_polymerase_III_psi_chi_subunit'], logt, logd, SubList,'default')
Showdata().png(['DNA_polymerase_III_core_enzyme','DNA_polymerase_III_preinitiation_complex','DNA_polymerase_III_beta_subunit','DNA_polymerase_III_tau_subunit_dimer','DNA_polymerase_III_psi_chi_subunit','DNA_polymerase_III_holoenzyme'], logt, logd, SubList,'default')

#Finalize
Simulation().Save(mod,SubList)
Simulation().Makedata('default')
"""

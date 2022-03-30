#!/usr/bin/env python


import sys
import os
import numpy as np
import pandas as pd
from argparse import ArgumentParser

def build_argparser():
    p = ArgumentParser(description=__doc__)
    p.add_argument("structure", type=str,
                   help="PDB-file containing structure.")
    p.add_argument("--ca", dest="ca", action="store_true",
            help="Return B factor for alpha carbons only")
    p.add_argument("--sidechain", dest='sc', action="store_true", 
                  help="Return B factor for sidechain atoms only")
    p.add_argument("--pdb", help="Name of the input PDB.")
    return p

  
def get_bfactor(structure, pdb, ca = None, sidechain = None):
    if ca and sidechain:
        print('Both alpha carbon and sidechain selected. Please choose one')
        return
    bfactors = []
    select = structure.extract('record', 'ATOM', '==')
    select = select.extract('e', 'H', '!=')
    if not ca == None:
       select = select.extract('name', 'CA', '==')
    if not sidechain == None:
        select = select.extract('name', (['N', 'CA', 'C', 'O']), '!=')
    for c in np.unique(select.chain):
        for r in np.unique(select.extract('chain', c, '==').resi:
            b_factor = np.average(select.extract(f'resi {r} and chain {c}').b) / np.average(select.extract(f'resi {r} and chain {c}').q)
            bfactors.append(tuple((pdb, np.array2string(r), np.array2string(select.extract(f'resi {r} and chain {c}').resn[0]), np.array2string(np.unique(c), b_factor)))
     B_factor = pd.DataFrame(bfactors, columns =['PDB', 'resi', 'resn', 'chain', 'b_factor'])
     return B_factor   
     

def main():
    p = build_argparser()
    args = p.parse_args()
    B_factor = get_bfactor(args.structure, args.pdb, args.ca, args.sc)
    B_factor.to_csv(args.pdb + '_B_factors.csv', index=False)   
                  
                            
if __name__ == '__main__':
    main()

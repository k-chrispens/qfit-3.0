ROTAMERS = {
# Alanine
'ALA': {
    'atoms': ['N', 'CA', 'C', 'O',
              'CB',
    ],
    'hydrogens': 'H1 HA HB1 HB2 HB3 H2 H3'.split(),
    'bonds': [
        ['N', 'CA'], ['CA', 'C'], ['C', 'O'],
        ['CA', 'CB'],
    ],
    'nchi': 0,
    'chi': {
    },
    'chi-rotate': {
    },
    'rotamers': [
    ],
},

# Arginine
'ARG': {
    'atoms': ['N', 'CA', 'C', 'O',
              'CB', 'CG', 'CD', 'NE', 'CZ', 'NH1', 'NH2'
             ],
    'hydrogens': 'H HA HB2 HB3 HG2 HG3 HD2 HD3 HE HH11 HH12 HH21 HH22'.split(),
    'bonds': [
        ['N', 'CA'], ['CA', 'C'], ['C', 'O'],
        ['CA', 'CB'], ['CB', 'CG'], ['CG', 'CD'], ['CD', 'NE'], ['NE', 'CZ'],
        ['CZ', 'NH1'], ['CZ', 'NH2'],
    ],
    'nchi': 4,
    'chi': {
        1: ['N', 'CA', 'CB', 'CG'],
        2: ['CA', 'CB', 'CG', 'CD'],
        3: ['CB', 'CG', 'CD', 'NE'],
        4: ['CG', 'CD', 'NE', 'CZ'],
    },
    'chi-rotate': {
        1: ['CG', 'CD', 'NE', 'CZ', 'NH1', 'NH2'],
        2: ['CD', 'NE', 'CZ', 'NH1', 'NH2'],
        3: ['NE', 'CZ', 'NH1', 'NH2'],
        4: ['CZ', 'NH1', 'NH2'],
    },
    'rotamers': [
        [  62,  180,  65,   85],
        [  62,  180,  65, -175],
        [  62,  180, 180,   85],
        [  62,  180, 180,  180],
        [  62,  180, 180,  -85],
        [  62,  180, -65,  175],
        [  62,  180, -65,  -85],
        [-177,   65,  65,   85],
        [-177,   65,  65, -175],
        [-177,   65, 180,   85],
        [-177,   65, 180,  180],
        [-177,  180,  65,   85],
        [-177,  180,  65, -175],
        [-177,  180,  65, -105],
        [-177,  180, 180,   85],
        [-177,  180, 180,  180],
        [-177,  180, 180,  -85],
        [-177,  180, -65,  105],
        [-177,  180, -65,  175],
        [-177,  180, -65,  -85],
        [ -67,  180,  65,   85],
        [ -67,  180,  65, -175],
        [ -67,  180, 180,   85],
        [ -67,  180, 180,  180],
        [ -67,  180, 180,  -85],
        [ -67,  180, -65,  105],
        [ -67,  180, -65,  175],
        [ -67, -167, -65,  -85],
        [ -62,  179,  67, -113],
        [ -62,  -68, 180,   85],
        [ -62,  -68, 180,  180],
        [ -62,  -68, 180,  -85],
        [ -62,  -68, -65,  175],
        [ -62,  -68, -65,  -85],
    ]
},
# Asparagine
'ASN': {
    'atoms': ['N', 'CA', 'C', 'O',
              'CB', 'CG', 'OD1', 'ND2',
             ],
    'hydrogens': 'H HA HB2 HB3 HD21 HD22'.split(),
    'bonds': [
        ['N', 'CA'], ['CA', 'C'], ['C', 'O'],
        ['CA', 'CB'], ['CB', 'CG'], ['CG', 'OD1'], ['CG', 'ND2'],
    ],
    'nchi': 2,
    'chi': {
        1: ['N', 'CA', 'CB', 'CG'],
        2: ['CA', 'CB', 'CG', 'OD1'],
    },
    'chi-rotate': {
        1: ['CG', 'OD1', 'ND2'],
        2: ['OD1', 'ND2'],
    },
    'rotamers': [
        [  62, -10],
        [  62,  30],
        [-174, -20],
        [-177,  30],
        [ -65, -20],
        [ -65, -75],
        [ -65, 120],
    ],
},
# Aspartate
'ASP': {
    'atoms': ['N', 'CA', 'C', 'O',
              'CB', 'CG', 'OD1', 'OD2',
             ],
    'hydrogens': 'H HA HB2 HB3 HD2'.split(),
    'bonds': [
        ['N', 'CA'], ['CA', 'C'], ['C', 'O'],
        ['CA', 'CB'], ['CB', 'CG'], ['CG', 'OD1'], ['CG', 'OD2'],
    ],
    'nchi': 2,
    'chi': {
        1: ['N', 'CA', 'CB', 'CG'],
        2: ['CA', 'CB', 'CG', 'OD1'],
    },
    'chi-rotate': {
        1: ['CG', 'OD1', 'OD2'],
        2: ['OD1', 'OD2'],
    },
    'rotamers': [
        [  62, -10],
        [  62,  30],
        [-177,   0],
        [-177,  65],
        [ -70, -15],
    ],
},
# Cysteine
'CYS': {
    'atoms': ['N', 'CA', 'C', 'O',
              'CB', 'SG',
             ],
    'hydrogens': 'H HA HB2 HB3 HG'.split(),
    'bonds': [
        ['N', 'CA'], ['CA', 'C'], ['C', 'O'],
        ['CA', 'CB'], ['CB', 'SG'],
    ],
    'nchi': 1,
    'chi': {
        1: ['N', 'CA', 'CB', 'SG'],
    },
    'chi-rotate': {
        1: ['SG'],
    },
    'rotamers': [
        [  62],
        [-177],
        [ -65],
    ],
},
'GLN': {
    'atoms': ['N', 'CA', 'C', 'O',
              'CB', 'CG', 'CD', 'OE1', 'NE2',
             ],
    'hydrogens': 'H HA HB2 HB3 HG2 HG3 HE21 HE22'.split(),
    'bonds': [
        ['N', 'CA'], ['CA', 'C'], ['C', 'O'],
        ['CA', 'CB'], ['CB', 'CG'], ['CG', 'CD'], ['CD', 'OE1'], ['CD', 'NE2']
    ],
    'nchi': 3,
    'chi': {
        1: ['N', 'CA', 'CB', 'CG'],
        2: ['CA', 'CB', 'CG', 'CD'],
        3: ['CB', 'CG', 'CD', 'OE1'],
    },
    'chi-rotate': {
        1: ['CG', 'CD', 'OE1', 'NE2'],
        2: ['CD', 'OE1', 'NE2'],
        3: ['OE1', 'NE2'],
    },
    'rotamers': [
        [  62, 180,   20],
        [  70, -75,    0],
        [-177,  65, -100],
        [-177,  65,   60],
        [-177, 180,    0],
        [ -65,  85,    0],
        [ -67, 180,  -25],
        [ -65, -65,  -40],
        [ -65, -65,  100],
    ],
},
'GLU': {
    'atoms': ['N', 'CA', 'C', 'O',
              'CB', 'CG', 'CD', 'OE1', 'OE2',
             ],
    'hydrogens': 'H HA HB2 HB3 HG2 HG3 HE2'.split(),
    'bonds': [
        ['N', 'CA'], ['CA', 'C'], ['C', 'O'],
        ['CA', 'CB'], ['CB', 'CG'], ['CG', 'CD'], ['CD', 'OE1'], ['CD', 'OE2']
    ],
    'nchi': 3,
    'chi': {
        1: ['N', 'CA', 'CB', 'CG'],
        2: ['CA', 'CB', 'CG', 'CD'],
        3: ['CB', 'CG', 'CD', 'OE1'],
    },
    'chi-rotate': {
        1: ['CG', 'CD', 'OE1', 'OE2'],
        2: ['CD', 'OE1', 'OE2'],
        3: ['OE1', 'OE2'],
    },
    'rotamers': [
        [  62, 180, -20],
        [  70, -80,   0],
        [-177,  65,  10],
        [-177, 180,   0],
        [-177, -80, -25],
        [ -65,  85,   0],
        [ -67, 180, -10],
        [ -65, -65, -40],
    ],
},
# Glycine
'GLY': {
    'atoms': ['N', 'CA', 'C', 'O',
    ],
    'hydrogens': 'H HA2 HA3'.split(),
    'bonds': [
        ['N', 'CA'], ['CA', 'C'], ['C', 'O'],
    ],
    'nchi': 0,
    'chi': {
    },
    'chi-rotate': {
    },
    'rotamers': [
    ],
},
'HIS': {
    'atoms': ['N', 'CA', 'C', 'O',
              'CB', 'CG', 'ND1', 'CD2', 'CE1', 'NE2',
             ],
    'hydrogens': 'H HA HB2 HB3 HD1 HD2 HE1 HE2'.split(),
    'bonds': [
        ['N', 'CA'], ['CA', 'C'], ['C', 'O'],
        ['CA', 'CB'], ['CB', 'CG'], ['CG', 'ND1'], ['ND1', 'CE1'],
        ['CE1', 'NE2'], ['CD2', 'NE2'], ['CD2', 'CG'],
    ],
    'nchi': 2,
    'chi': {
        1: ['N', 'CA', 'CB', 'CG'],
        2: ['CA', 'CB', 'CG', 'ND1'],
    },
    'chi-rotate': {
        1: ['CG', 'ND1', 'CD2', 'CE1', 'NE2'],
        2: ['ND1', 'CD2', 'CE1', 'NE2'],
    },
    'rotamers': [
        [  62,  -75],
        [  62,   80],
        [-177, -165],
        [-177,  -80],
        [-177,   60],
        [ -65,  -70],
        [ -65,  165],
        [ -65,   80],
    ],
},
'ILE': {
    'atoms': ['N', 'CA', 'C', 'O',
              'CB', 'CG1', 'CG2', 'CD1',
             ],
    'hydrogens': 'H HA HB HG12 HG13 HG21 HG22 HG23 HD11 HD12 HD13'.split(),
    'bonds': [
        ['N', 'CA'], ['CA', 'C'], ['C', 'O'],
        ['CA', 'CB'], ['CB', 'CG1'], ['CB', 'CG2'], ['CG1', 'CD1'],
    ],
    'nchi': 2,
    'chi': {
        1: ['N', 'CA', 'CB', 'CG1'],
        2: ['CA', 'CB', 'CG1', 'CD1'],
    },
    'chi-rotate': {
        1: ['CG1', 'CG2', 'CD1'],
        2: ['CD1'],
    },
    'rotamers': [
        [  62, 100],
        [  62, 170],
        [-177,  66],
        [-177, 165],
        [ -65, 100],
        [ -65, 170],
        [ -57, -60],
    ],
},
'LEU': {
    'atoms': ['N', 'CA', 'C', 'O',
              'CB', 'CG', 'CD1', 'CD2',
             ],
    'hydrogens': 'H HA HB2 HB3 HG HD11 HD12 HD13 HD21 HD22 HD23'.split(),
    'bonds': [
        ['N', 'CA'], ['CA', 'C'], ['C', 'O'],
        ['CA', 'CB'], ['CB', 'CG'], ['CG', 'CD1'], ['CG', 'CD2'],
    ],
    'nchi': 2,
    'chi': {
        1: ['N', 'CA', 'CB', 'CG'],
        2: ['CA', 'CB', 'CG', 'CD1'],
    },
    'chi-rotate': {
        1: ['CG', 'CD1', 'CD2'],
        2: ['CD1', 'CD2'],
    },
    'rotamers': [
        [  62,  80],
        [-177,  65],
        [-172, 145],
        [ -85,  65],
        [ -65, 175],
    ],
},
'LYS': {
    'atoms': ['N', 'CA', 'C', 'O',
              'CB', 'CG', 'CD', 'CE', 'NZ',
             ],
    'hydrogens': 'H HA HB2 HB3 HG2 HG3 HD2 HD3 HE2 HE3 HZ1 HZ2 HZ3'.split(),
    'bonds': [
        ['N', 'CA'], ['CA', 'C'], ['C', 'O'],
        ['CA', 'CB'], ['CB', 'CG'], ['CG', 'CD'], ['CD', 'CE'], ['CE', 'NZ']
    ],
    'nchi': 4,
    'chi': {
        1: ['N', 'CA', 'CB', 'CG'],
        2: ['CA', 'CB', 'CG', 'CD'],
        3: ['CB', 'CG', 'CD', 'CE'],
        4: ['CG', 'CD', 'CE', 'NZ'],
    },
    'chi-rotate': {
        1: ['CG', 'CD', 'CE', 'NZ'],
        2: ['CD', 'CE', 'NZ'],
        3: ['CE', 'NZ'],
        4: ['NZ'],
    },
    'rotamers': [
        [  62, 180,  68, 180],
        [  62, 180, 180,  65],
        [  62, 180, 180, 180],
        [  62, 180, 180, -65],
        [  62, 180, -68, 180],
        [-177,  68, 180,  65],
        [-177,  68, 180, 180],
        [-177,  68, 180, -65],
        [-177, 180,  68,  65],
        [-177, 180,  68, 180],
        [-177, 180, 180,  65],
        [-177, 180, 180, 180],
        [-177, 180, 180, -65],
        [-177, 180, -68, 180],
        [-177, 180, -68, -65],
        [ -90,  68, 180, 180],
        [ -67, 180,  68,  65],
        [ -67, 180,  68, 180],
        [ -67, 180, 180,  65],
        [ -67, 180, 180, 180],
        [ -67, 180, 180, -65],
        [ -67, 180, -68, 180],
        [ -67, 180, -68, -65],
        [ -62, -68, 180,  65],
        [ -62, -68, 180, 180],
        [ -62, -68, 180, -65],
        [ -62, -68, -68, 180],
    ],
},
'MET': {
    'atoms': ['N', 'CA', 'C', 'O',
              'CB', 'CG', 'SD', 'CE',
             ],
    'hydrogens': 'H HA HB2 HB3 HG2 HG3 HE1 HE2 HE3'.split(),
    'bonds': [
        ['N', 'CA'], ['CA', 'C'], ['C', 'O'],
        ['CA', 'CB'], ['CB', 'CG'], ['CG', 'SD'], ['SD', 'CE'],
    ],
    'nchi': 3,
    'chi': {
        1: ['N', 'CA', 'CB', 'CG'],
        2: ['CA', 'CB', 'CG', 'SD'],
        3: ['CB', 'CG', 'SD', 'CE'],
    },
    'chi-rotate': {
        1: ['CG', 'SD', 'CE'],
        2: ['SD', 'CE'],
        3: ['CE'],
    },
    'rotamers': [
        [  62, 180,  75],
        [  62, 180, -75],
        [-177,  65,  75],
        [-177,  65, 180],
        [-177, 180,  75],
        [-177, 180, 180],
        [-177, 180, -75],
        [ -67, 180,  75],
        [ -67, 180, 180],
        [ -67, 180, -75],
        [ -65, -65, 103],
        [ -65, -65, 180],
        [ -65, -65, -70],
    ],
},
'PHE': {
    'atoms': ['N', 'CA', 'C', 'O',
              'CB', 'CG', 'CD1', 'CD2', 'CE1', 'CE2', 'CZ',
             ],
    'hydrogens': 'H HA HB2 HB3 HD1 HD2 HE1 HE2 HZ'.split(),
    'bonds': [
        ['N', 'CA'], ['CA', 'C'], ['C', 'O'],
        ['CA', 'CB'], ['CB', 'CG'], ['CG', 'CD1'], ['CG', 'CD2'],
        ['CD1', 'CE1'], ['CD2', 'CE2'], ['CE1', 'CZ'], ['CE2', 'CZ'],
    ],
    'nchi': 2,
    'chi': {
        1: ['N', 'CA', 'CB', 'CG'],
        2: ['CA', 'CB', 'CG', 'CD1'],
    },
    'chi-rotate': {
        1: ['CG', 'CD1', 'CD2', 'CE1', 'CE2', 'CZ'],
        2: ['CD1', 'CD2', 'CE1', 'CE2', 'CZ'],
    },
    'rotamers': [
        [  62,  90],
        [-177,  80],
        [ -65, -85],
        [ -65, -30],
    ],
},
# Proline
'PRO': {
    'atoms': ['N', 'CA', 'C', 'O',
              'CB', 'CG', 'CD',
             ],
    'hydrogens': 'H HA HB2 HB3 HG2 HG3 HD2 HD3'.split(),
    'bonds': [
        ['N', 'CA'], ['CA', 'C'], ['C', 'O'],
        ['CA', 'CB'], ['CB', 'CG'], ['CG', 'CD'], ['CD', 'N'],
    ],
    'nchi': 1,
    'chi': {
        1: ['N', 'CA', 'CB', 'CG'],
    },
    'chi-rotate': {
        1: ['CG'],
    },
    'rotamers': [
        [ 30],
        [-30],
    ],
},
# Serine
'SER': {
    'atoms': ['N', 'CA', 'C', 'O',
              'CB', 'OG',
             ],
    'hydrogens': 'H HA HB2 HB3 HG'.split(),
    'bonds': [
        ['N', 'CA'], ['CA', 'C'], ['C', 'O'],
        ['CA', 'CB'], ['CB', 'OG'],
    ],
    'nchi': 1,
    'chi': {
        1: ['N', 'CA', 'CB', 'OG'],
    },
    'chi-rotate': {
        1: ['OG'],
    },
    'rotamers': [
        [  62],
        [-177],
        [ -65],
    ],
},
# Threonine
'THR': {
    'atoms': ['N', 'CA', 'C', 'O',
              'CB', 'OG1', 'CG2',
             ],
    'hydrogens': 'H HA HB HG1 HG21 HG22 HG23'.split(),
    'bonds': [
        ['N', 'CA'], ['CA', 'C'], ['C', 'O'],
        ['CA', 'CB'], ['CB', 'OG1'], ['CB', 'CG2'],
    ],
    'nchi': 1,
    'chi': {
        1: ['N', 'CA', 'CB', 'OG1'],
    },
    'chi-rotate': {
        1: ['OG1', 'CG2'],
    },
    'rotamers': [
        [  62],
        [-175],
        [ -65],
    ],
},
# Tryptophan
'TRP': {
    'atoms': ['N', 'CA', 'C', 'O',
              'CB', 'CG', 'CD1', 'CD2', 'NE1', 'CE2', 'CE3', 'CZ2', 'CZ3', 'CH2',
             ],
    'hydrogens': 'H HA HB2 HB3 HD1 HE1 HE3 HZ2 HZ3 HH2'.split(),
    'bonds': [
        ['N', 'CA'], ['CA', 'C'], ['C', 'O'],
        ['CA', 'CB'], ['CB', 'CG'], ['CG', 'CD1'], ['CG', 'CD2'],
        ['CD1', 'NE1'], ['NE1', 'CE2'], ['CD2', 'CE2'], ['CD2', 'CE3'],
        ['CE2', 'CZ2'], ['CE3', 'CZ3'], ['CZ2', 'CH2'], ['CZ3', 'CH2'],
    ],
    'nchi': 2,
    'chi': {
        1: ['N', 'CA', 'CB', 'CG'],
        2: ['CA', 'CB', 'CG', 'CD1'],
    },
    'chi-rotate': {
        1: ['CG', 'CD1', 'CD2', 'NE1', 'CE2', 'CE3', 'CZ2', 'CZ3', 'CH2'],
        2: ['CD1', 'CD2', 'NE1', 'CE2', 'CE3', 'CZ2', 'CZ3', 'CH2'],
    },
    'rotamers': [
        [  62,  -90],
        [  62,   90],
        [-177, -105],
        [-177,   90],
        [ -65,  -90],
        [ -65,   -5],
        [ -65,   95],
    ],
},
# Tyrosine
'TYR': {
    'atoms': ['N', 'CA', 'C', 'O',
              'CB', 'CG', 'CD1', 'CD2', 'CE1', 'CE2', 'CZ', 'OH',
             ],
    'hydrogens': 'H HA HB2 HB3 HD1 HD2 HE1 HE2 HH'.split(),
    'bonds': [
        ['N', 'CA'], ['CA', 'C'], ['C', 'O'],
        ['CA', 'CB'], ['CB', 'CG'], ['CG', 'CD1'], ['CD1', 'CE1'],
        ['CG', 'CD2'], ['CD2', 'CE2'], ['CE1', 'CZ'], ['CE2', 'CZ'],
        ['CZ', 'OH'],
    ],
    'nchi': 2,
    'chi': {
        1: ['N', 'CA', 'CB', 'CG'],
        2: ['CA', 'CB', 'CG', 'CD1'],
    },
    'chi-rotate': {
        1: ['CG', 'CD1', 'CD2', 'CE1', 'CE2', 'CZ', 'OH'],
        2: ['CD1', 'CD2', 'CE1', 'CE2', 'CZ', 'OH'],
    },
    'rotamers': [
        [  62,  90],
        [-177,  80],
        [ -65, -85],
        [ -65, -30],
    ],
},
# Valine
'VAL': {
    'atoms': ['N', 'CA', 'C', 'O',
              'CB', 'CG1', 'CG2',
             ],
    'hydrogens': 'H HA HB HG11 HG12 HG13 HG21 HG22 HG23'.split(),
    'bonds': [
        ['N', 'CA'], ['CA', 'C'], ['C', 'O'],
        ['CA', 'CB'], ['CB', 'CG1'], ['CB', 'CG2'],
    ],
    'nchi': 1,
    'chi': {
        1: ['N', 'CA', 'CB', 'CG1'],
    },
    'chi-rotate': {
        1: ['CG1', 'CG2'],
    },
    'rotamers': [
        [ 63],
        [175],
        [-60],
    ],
},
# Selenomethionine
'MSE': {
    'atoms': ['N', 'CA', 'C', 'O',
              'CB', 'CG', 'SE', 'CE',
             ],
    'hydrogens': 'H HA HB2 HB3 HG2 HG3 HE1 HE2 HE3'.split(),
    'bonds': [
        ['N', 'CA'], ['CA', 'C'], ['C', 'O'],
        ['CA', 'CB'], ['CB', 'CG'], ['CG', 'SE'], ['SE', 'CE'],
    ],
    'nchi': 3,
    'chi': {
        1: ['N', 'CA', 'CB', 'CG'],
        2: ['CA', 'CB', 'CG', 'SE'],
        3: ['CB', 'CG', 'SE', 'CE'],
    },
    'chi-rotate': {
        1: ['CG', 'SE', 'CE'],
        2: ['SE', 'CE'],
        3: ['CE'],
    },
    # A blatant copy of MET
    'rotamers': [
        [  62, 180,  75],
        [  62, 180, -75],
        [-177,  65,  75],
        [-177,  65, 180],
        [-177, 180,  75],
        [-177, 180, 180],
        [-177, 180, -75],
        [ -67, 180,  75],
        [ -67, 180, 180],
        [ -67, 180, -75],
        [ -65, -65, 103],
        [ -65, -65, 180],
        [ -65, -65, -70],
    ],
},
}

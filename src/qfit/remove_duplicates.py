"""Delete duplicate atom entries"""

import numpy as np
import argparse
import logging
import os
import sys
import time
from string import ascii_uppercase
from . import Structure
from .structure import residue_type
from .structure.residue import _RotamerResidue
from .structure.rotamers import ROTAMERS


def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("structure", type=str, help="PDB-file containing structure.")

    # Output options
    p.add_argument(
        "-d",
        "--directory",
        type=os.path.abspath,
        default=".",
        metavar="<dir>",
        help="Directory to store results.",
    )
    p.add_argument("-v", "--verbose", action="store_true", help="Be verbose.")
    args = p.parse_args()

    return args


def find_unique_atoms(structure):
    """Find unique atoms in a structure.

    Atoms that belong to amino acids are assumed to be unique.

    Args:
        structure (qfit.Structure): structure to scan for unique atoms.

    Returns:
        np.ndarray[bool]: a (structure.natoms,) mask, with unique atoms
            marked True.
    """

    # First, assume all atoms are identical
    identical_ij = np.ones((structure.natoms, structure.natoms), dtype=bool)
    # The main diagonal does not contain 'duplicated' atoms
    identical_ij &= np.invert(np.identity(structure.natoms, dtype=bool))

    # Identify duplicated atoms by comparing selected properties.
    for attr in ("resi", "resn", "altloc", "icode", "chain", "name"):
        attrvec = structure.data[attr]
        ident_prop = attrvec[:, np.newaxis] == attrvec[np.newaxis, :]
        identical_ij &= ident_prop

    # We only care about the upper triangle
    #   (duplication will only mark atoms with higher index for removal)
    identical_ij = np.triu(identical_ij)

    # Logical-or rows together
    identical_i = np.any(identical_ij, axis=0)

    # Name atoms which are not unique
    print(
        f"Atoms {tuple(*np.nonzero(identical_i))} had earlier, identical atoms.\n"
        f"They are being removed."
    )

    # We are not concerned if amino acids have duplicate atoms
    is_amino_acid = np.frompyfunc(ROTAMERS.__contains__, 1, 1)
    amino_acids_i = is_amino_acid(structure.resn).astype(bool)
    identical_i &= np.invert(amino_acids_i)

    # Unique atoms are not identical
    return np.invert(identical_i)


def main():
    args = parse_args()
    try:
        os.makedirs(args.directory)
    except OSError:
        pass

    structure = Structure.fromfile(args.structure).reorder()

    # Find unique atoms
    mask = find_unique_atoms(structure)

    # Remove duplicated atoms
    data = {}
    for attr in structure.data:
        data[attr] = structure.data[attr][mask]
    new_structure = Structure(data)

    # Print the new structure to file
    new_structure.tofile(args.structure + ".fixed")

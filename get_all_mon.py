from ase.io import read,write
import glob
from ccdc import io
import os

if __name__ == "__main__":
    files=glob.glob("*.cif")
    for file in files:
        mol_reader = io.MoleculeReader(file)
        reader = mol_reader[0]
        moleculenum = len(reader.components)
        for i in range(0,moleculenum):
            mol = reader.components[i]
            writer = io.MoleculeWriter("temp.cif")
            writer.write(mol)
            monomer = read("temp.cif")
            write(f"monomer{i}.xyz",monomer)
            os.remove("temp.cif")
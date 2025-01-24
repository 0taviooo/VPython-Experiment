
from include.atom_module import atom
from include.bond_module import bond
from include.angle_module import angle
from include.molecules_dict_module import molecules
from include.utilities import make_atom, make_bond
from math import cos, sin, radians
from vpython import vec

# Definição da classe de molécula
class Molecule:
    """
    Represents a chemical molecule, encapsulating its type, spatial coordinates, and the relationships between its constituent atoms.

    Attributes:
        type (str): The type of the molecule (e.g., water, methane).
        xyz (list[int]): A list of three integers representing the x, y, and z coordinates of the molecule's central atom.
        molecule_atoms (list): A list of atom types that compose the molecule.
        molecule_bonds (list): A list of bond types that connect the atoms in the molecule.
        angle (float): The angle between bonds in degrees, if applicable.
        bond_length (list): A list containing lengths of bonds between atoms.
        atoms (list): A dynamically populated list to hold atom objects created for this molecule.
        bonds (list): A dynamically populated list to hold bond objects created for this molecule.

    Methods:
        make_molecule(): Constructs the 3D representation of the molecule by placing atoms and bonds based on their specified properties and spatial relationships.
    """
    def __init__(self, type, xyz):
        self.type = type
        self.xyz = xyz
        self.molecule_atoms = molecules[type]['atoms']
        self.molecule_bonds = molecules[type]['bonds']
        self.angle = angle.get(type, 0)
        self.bond_length = bond[type]
        self.atoms = []
        self.bonds = []
    
    def make_molecule(self):
        """
        Constructs the molecular structure by creating atoms and bonds based on predefined properties such as bond lengths and angles.

        The method performs the following steps:
            1. Retrieves the initial position from `xyz` coordinates.
            2. Calculates gaps based on atomic radii to ensure proper spacing between atoms.
            3. Iteratively creates atoms and bonds according to their specified arrangement:
               - For the first atom, it places it at the origin defined by `xyz`.
               - For subsequent atoms, it calculates their positions based on bond lengths and angles relative to previously placed atoms.
            4. Adjusts for angles when placing third atoms to maintain geometric accuracy.

        This method ultimately populates `self.atoms` with atom objects and `self.bonds` with bond objects representing the physical structure of the molecule in 3D space.
        """
        x, y, z = self.xyz
        gap = atom[self.molecule_atoms[0]]['radius']
                
        for index, atom_type in enumerate(self.molecule_atoms):
            atom_radius = atom[atom_type]['radius']
                            
            if index == 0:
                self.atoms.append(make_atom(atom_type, x, y, z))
                
            elif index == 1:
                self.bonds.append(make_bond(self.bond_length[0], self.molecule_bonds[0], x + gap, y, z, direction=vec(1, 0, 0)))
                self.atoms.append(make_atom(atom_type, x + gap + self.bond_length[0] + atom_radius, y, z))
            elif index == 2:
                if self.angle:
                    
                    bond_angle = self.angle if self.angle <= 90 else 180 - self.angle
                                        
                    self.bonds.append(make_bond(self.bond_length[1] + gap, self.molecule_bonds[1], x, y, z))
                    for b in self.bonds[-1]:
                        b.rotate(axis=vec(0, 0, 1), angle=radians(self.angle))
                    self.atoms.append(make_atom(
                                                self.molecule_atoms[2],
                                                x - (((self.bond_length[1] + gap + atom_radius) * cos(radians(bond_angle)))),
                                                y + (((self.bond_length[1] + atom_radius) * sin(radians(bond_angle))) + min(atom_radius, gap) - bond['variation']),
                                                z
                                        )
                                    )
                else:
                    self.bonds.append(make_bond(self.bond_length[1], self.molecule_bonds[1], x - gap, y, z, direction=vec(-1, 0, 0)))
                    self.atoms.append(make_atom(atom_type, x - gap - self.bond_length[1] - atom_radius, y, z))


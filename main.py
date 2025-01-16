Web VPython 3.2

# from vpython import *

class new_colors:
    dark_red = vec(0.4, 0, 0)
    dark_green = vec(0, 0.3, 0)
    dark_orange = vec(0.6, 0.3, 0)
    beige = vec(1, 0.9, 0.8)
    grey = vec(0.4, 0.4, 0.4)
    pink = vec(1, 0.6, 1)

atom = {
    'H': {'radius': 0.53, 'color': color.white},
    
    'C': {'radius': 0.67, 'color': color.black},
    
    'N': {'radius': 0.56, 'color': color.blue},
    
    'O': {'radius': 0.48, 'color': color.red},
    
    'F': {'radius': 0.42, 'color': color.green},
    'Cl': {'radius': 0.79, 'color': color.green},
    
    'Br': {'radius': 0.94, 'color': new_colors.dark_red},
    
    'I': {'radius': 1.15, 'color': color.purple},
    
    'He': {'radius': 0.31, 'color': color.cyan},
    'Ne': {'radius': 0.38, 'color': color.cyan},
    'Ar': {'radius': 0.71, 'color': color.cyan},
    'Kr': {'radius': 0.87, 'color': color.cyan},
    'Xe': {'radius': 1.08, 'color': color.cyan},
    'Rn': {'radius': 1.20, 'color': color.cyan},
    
    'P': {'radius': 0.98, 'color': color.orange},
    
    'S': {'radius': 0.87, 'color': color.yellow},
    
    'B': {'radius': 0.87, 'color': new_colors.beige},
    
    'Li': {'radius': 1.67, 'color': color.magenta},
    'Na': {'radius': 1.90, 'color': color.magenta},
    'K': {'radius': 2.43, 'color': color.magenta},
    'Rb': {'radius': 2.95, 'color': color.magenta},
    'Cs': {'radius': 2.98, 'color': color.magenta},
    
    
    'Be': {'radius': 1.12, 'color': new_colors.dark_green},
    'Mg': {'radius': 1.45, 'color': new_colors.dark_green},
    'Ca': {'radius': 1.94, 'color': new_colors.dark_green},
    'Sr': {'radius': 2.19, 'color': new_colors.dark_green},
    'Ba': {'radius': 2.53, 'color': new_colors.dark_green},
    
    'Ti': {'radius': 1.76, 'color': new_colors.grey},
    
    'Fe': {'radius': 1.56, 'color': new_colors.dark_orange},
    
    'Si': {'radius': 1.11, 'color': new_colors.pink},
}

bond = {
    'radius': 0.05,
    'variation': 0.1,
    
    'H2': [0.74],
    'Li2': [2.67],
    'Be2': [2.46],
    'B2': [1.59],
    'C2': [1.24],
    'N2': [1.09],
    'O2': [1.20],
    'F2': [1.41],
    'Ne2': [3.10],
    'Na2': [3.07],
    'Mg2': [3.89],
    'P2': [1.83],
    'S2': [1.88],
    'Cl2': [1.98],
    'Ar2': [3.75],
    'K2': [3.90],
    'Br2': [2.28],
    'I2': [2.66],
    
    'HCl': [1.38],
    'SiO': [1.52],
    'CO': [1.12],
    'CS': [1.54],
    'SiS': [1.94],
    
    'CO2': [1.16, 1.16],
    'H2O': [1.0, 1.0],
    'HCN': [1.09, 1.16],
    'NO2': [1.19, 1.19],
    'O3': [1.28, 1.28],
    'SO2': [1.43, 1.43],
    'OF2': [1.40, 1.40],
    'HCO': [1.12, 1.74],
    'HCS': [1.09, 1.56],
    'HSiO': [1.53, 1.53],
    'HSiS': [1.51, 1.97],
    'HOC': [0.98, 1.27],
    'HSC': [1.38, 1.66],
    'HOSi': [0.96, 1.66],
    'HSSi': [1.35, 2.14],
}

angle = {
    'H2O': 104.48,
    'NO2': 134.3,
    'O3': 116.8,
    'SO2': 119,
    'OF2': 103,
    'HCO': 124,
    'HCS': 131.4,
    'HSiO': 118,
    'HSiS': 116.1,
    'HOC': 114.5,
    'HSC': 103.8,
    'HOSi': 120.2,
    'HSSi': 101.9,
}

molecules = {
    'H2': {
        'atoms': ['H', 'H'],
        'bonds': ['simple'],
    },
    'Li2': {
        'atoms': ['Li', 'Li'],
        'bonds': ['simple'],
    },
    'Be2': {
        'atoms': ['Be', 'Be'],
        'bonds': ['simple'],
    },
    'B2': {
        'atoms': ['B', 'B'],
        'bonds': ['simple'],
    },
    'C2': {
        'atoms': ['C', 'C'],
        'bonds': ['simple'],
    },
    'N2': {
        'atoms': ['N', 'N'],
        'bonds': ['triple'],
    },
    'O2': {
        'atoms': ['O', 'O'],
        'bonds': ['double'],
    },
    'F2': {
        'atoms': ['F', 'F'],
        'bonds': ['simple'],
    },
    'Ne2': {
        'atoms': ['Ne', 'Ne'],
        'bonds': ['simple'],
    },
    'Na2': {
        'atoms': ['Na', 'Na'],
        'bonds': ['simple'],
    },
    'Mg2': {
        'atoms': ['Mg', 'Mg'],
        'bonds': ['simple'],
    },
    'P2': {
        'atoms': ['P', 'P'],
        'bonds': ['simple'],
    },
    'S2': {
        'atoms': ['S', 'S'],
        'bonds': ['simple'],
    },
    'Cl2': {
        'atoms': ['Cl', 'Cl'],
        'bonds': ['simple'],
    },
    'Ar2': {
        'atoms': ['Ar', 'Ar'],
        'bonds': ['simple'],
    },
    'Br2': {
        'atoms': ['Br', 'Br'],
        'bonds': ['simple'],
    },
    'I2': {
        'atoms': ['I', 'I'],
        'bonds': ['simple'],
    },
    'K2': {
        'atoms': ['K', 'K'],
        'bonds': ['simple'],
    },
    
    'HCl': {
        'atoms': ['H', 'Cl'],
        'bonds': ['simple'],
    },
    'CO': {
        'atoms': ['C', 'O'],
        'bonds': ['triple'],
    },
    'CS': {
        'atoms': ['C', 'S'],
        'bonds': ['triple'],
    },
    'SiO': {
        'atoms': ['Si', 'O'],
        'bonds': ['triple'],
    },
    'SiS': {
        'atoms': ['Si', 'S'],
        'bonds': ['triple'],
    },
    'CO2': {
        'atoms': ['C', 'O', 'O'],
        'bonds': ['double', 'double'],
    },
    'H2O': {
        'atoms': ['O', 'H', 'H'],
        'bonds': ['simple', 'simple'],
    },
    'HCN': {
        'atoms': ['H', 'C', 'N'],
        'bonds': ['simple', 'triple'],
    },
    'NO2': {
        'atoms': ['N', 'O', 'O'],
        'bonds': ['simple', 'double'],
    },
    'O3': {
        'atoms': ['O', 'O', 'O'],
        'bonds': ['simple', 'double'],
    },
    'SO2': {
        'atoms': ['S', 'O', 'O'],
        'bonds': ['double', 'double'],
    },
    'OF2': {
        'atoms': ['O', 'F', 'F'],
        'bonds': ['simple', 'simple'],
    },
    'HCO': {
        'atoms': ['H', 'C', 'O'],
        'bonds': ['simple', 'double'],
    },
    'HCS': {
        'atoms': ['H', 'C', 'S'],
        'bonds': ['simple', 'double'],
    },
    'HSiO': {
        'atoms': ['H', 'Si', 'O'],
        'bonds': ['double', 'double'],
    },
    'HSiS': {
        'atoms': ['H', 'Si', 'S'],
        'bonds': ['simple', 'double'],
    },
    'HOC': {
        'atoms': ['H', 'O', 'C'],
        'bonds': ['simple', 'double'],
    },
    'HSC': {
        'atoms': ['H', 'O', 'C'],
        'bonds': ['simple', 'double'],
    },
    'HOSi': {
        'atoms': ['H', 'O', 'Si'],
        'bonds': ['double', 'double'],
    },
    'HSSi': {
        'atoms': ['H', 'S', 'Si'],
        'bonds': ['simple', 'double'],
    },
}

def make_atom(type, x, y, z):
    a = sphere(pos=vec(x, y, z), color=atom[type]['color'], radius=atom[type]['radius'])
    return a

def make_bond(bond_length, bond_type, x, y, z, direction=vec(1, 0, 0)):
    bonds = []
    if bond_type == 'simple':
        sigma1 = cylinder(pos=vec(x, y, z), axis=direction * bond_length, radius=bond['radius'], color=color.white)
        bonds.append(sigma1)
    elif bond_type == 'double':
        sigma1 = cylinder(pos=vec(x, y+bond['variation'], z), axis=direction * bond_length, radius=bond['radius'], color=color.white)
        pi1 = cylinder(pos=vec(x, y-bond['variation'], z), axis=direction * bond_length, radius=bond['radius'], color=color.white)
        bonds.append(sigma1)
        bonds.append(pi1)
    elif bond_type == 'triple':
        pi1 = cylinder(pos=vec(x, y+bond['variation'], z), axis=direction * bond_length, radius=bond['radius'], color=color.white)
        sigma1 = cylinder(pos=vec(x, y, z), axis=direction * bond_length, radius=bond['radius'], color=color.white)
        pi2 = cylinder(pos=vec(x, y-bond['variation'], z), axis=direction * bond_length, radius=bond['radius'], color=color.white)
        bonds.append(pi1)
        bonds.append(sigma1)
        bonds.append(pi2)
    return bonds

class Molecule:
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
        x, y, z = self.xyz
                
        for index, atom_type in enumerate(self.molecule_atoms):
            atom_radius = atom[atom_type]['radius']
                            
            if index == 0:
                self.atoms.append(make_atom(atom_type, x, y, z))
                
            elif index == 1:
                gap = atom[self.molecule_atoms[0]]['radius']
                self.bonds.append(make_bond(self.bond_length[0], self.molecule_bonds[0], x + gap, y, z, direction=vec(1, 0, 0)))
                self.atoms.append(make_atom(atom_type, x + gap + self.bond_length[0] + atom_radius, y, z))
            elif index == 2:
                gap = atom[self.molecule_atoms[0]]['radius']
                # Problema começa aqui:
                if self.angle:
                    
                    bond_angle = self.angle if self.angle <= 90 else 180 - self.angle
                                        
                    self.bonds.append(make_bond(self.bond_length[1] + gap, self.molecule_bonds[1], x, y, z))
                    for b in self.bonds[-1]:
                        b.rotate(axis=vec(0, 0, 1), angle=radians(self.angle))
                    self.atoms.append(make_atom(self.molecule_atoms[2], x - ((self.bond_length[1] * cos(bond_angle)) + gap + (atom_radius * cos(bond_angle))), y + ((self.bond_length[1] * sin(bond_angle)) + gap + atom_radius), z))
                # Problema termina aqui.
                else:
                    self.bonds.append(make_bond(self.bond_length[1], self.molecule_bonds[1], x - gap, y, z, direction=vec(-1, 0, 0)))
                    self.atoms.append(make_atom(atom_type, x - gap - self.bond_length[1] - atom_radius, y, z))

# Linha 1
h2 = Molecule('H2', [0, 0, 0])
h2.make_molecule()

n2 = Molecule('N2', [12, 0, 0])
n2.make_molecule()

o2 = Molecule('O2', [24, 0, 0])
o2.make_molecule()

f2 = Molecule('F2', [36, 0, 0])
f2.make_molecule()

cl2 = Molecule('Cl2', [48, 0, 0])
cl2.make_molecule()

# Linha 2
br2 = Molecule('Br2', [0, 4, 0])
br2.make_molecule()

i2 = Molecule('I2', [12, 4, 0])
i2.make_molecule()

hcl = Molecule('HCl', [24, 4, 0])
hcl.make_molecule()

co2 = Molecule('CO2', [36, 4, 0])
co2.make_molecule()

h2o = Molecule('H2O', [48, 4, 0])
h2o.make_molecule()

#Linha 3
hcn = Molecule('HCN', [0, 8, 0])
hcn.make_molecule()

no2 = Molecule('NO2', [12, 8, 0])
no2.make_molecule()

o3 = Molecule('O3', [24, 8, 0])
o3.make_molecule()

so2 = Molecule('SO2', [36, 8, 0])
so2.make_molecule()

of2 = Molecule('OF2', [48, 8, 0])
of2.make_molecule()

#Linha 4
sio = Molecule('SiO', [0, 12, 0])
sio.make_molecule()

co = Molecule('CO', [12, 12, 0])
co.make_molecule()

cs = Molecule('CS', [24, 12, 0])
cs.make_molecule()

sio = Molecule('SiO', [36, 12, 0])
sio.make_molecule()

sis = Molecule('SiS', [48, 12, 0])
sis.make_molecule()

#Linha 5
hco = Molecule('HCO', [0, 16, 0])
hco.make_molecule()

hcs = Molecule('HCS', [12, 16, 0])
hcs.make_molecule()

hsio = Molecule('HSiO', [24, 16, 0])
hsio.make_molecule()

hsis = Molecule('HSiS', [36, 16, 0])
hsis.make_molecule()

hoc = Molecule('HOC', [48, 16, 0])
hoc.make_molecule()

#Linha 6
hsc = Molecule('HSC', [0, 20, 0])
hsc.make_molecule()

hosi = Molecule('HOSi', [12, 20, 0])
hosi.make_molecule()

hssi = Molecule('HSSi', [24, 20, 0])
hssi.make_molecule()

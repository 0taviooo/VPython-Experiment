Web VPython 3.2

dark_red = vec(0.4, 0, 0)
dark_green = vec(0, 0.3, 0)
dark_orange = vec(0.6, 0.3, 0)
beige = vec(1, 0.9, 0.8)
grey = vec(0.4, 0.4, 0.4)

atom = {
    'H': {'radius': 0.53, 'color': color.white},
    
    'C': {'radius': 0.67, 'color': color.black},
    
    'N': {'radius': 0.56, 'color': color.blue},
    
    'O': {'radius': 0.48, 'color': color.red},
    
    'F': {'radius': 0.42, 'color': color.green},
    'Cl': {'radius': 0.79, 'color': color.green},
    
    'Br': {'radius': 0.94, 'color': dark_red},
    
    'I': {'radius': 1.15, 'color': color.purple},
    
    'He': {'radius': 0.31, 'color': color.cyan},
    'Ne': {'radius': 0.38, 'color': color.cyan},
    'Ar': {'radius': 0.71, 'color': color.cyan},
    'Kr': {'radius': 0.87, 'color': color.cyan},
    'Xe': {'radius': 1.08, 'color': color.cyan},
    'Rn': {'radius': 1.20, 'color': color.cyan},
    
    'P': {'radius': 0.98, 'color': color.orange},
    
    'S': {'radius': 0.87, 'color': color.yellow},
    
    'B': {'radius': 0.87, 'color': beige},
    
    'Li': {'radius': 1.67, 'color': color.magenta},
    'Na': {'radius': 1.90, 'color': color.magenta},
    'K': {'radius': 2.43, 'color': color.magenta},
    'Rb': {'radius': 2.95, 'color': color.magenta},
    'Cs': {'radius': 2.98, 'color': color.magenta},
    
    
    'Be': {'radius': 1.12, 'color': dark_green},
    'Mg': {'radius': 1.45, 'color': dark_green},
    'Ca': {'radius': 1.94, 'color': dark_green},
    'Sr': {'radius': 2.19, 'color': dark_green},
    'Ba': {'radius': 2.53, 'color': dark_green},
    
    'Ti': {'radius': 1.76, 'color': grey},
    
    'Fe': {'radius': 1.56, 'color': dark_orange},
}

bond = {
    'radius': 0.05,
    'variation': 0.1,
    
    'H2': 0.74,
    'Li2': 2.67,
    'Be2': 2.46,
    'B2': 1.59,
    'C2': 1.24,
    'N2': 1.09,
    'O2': 1.20,
    'F2': 1.41,
    'Ne2': 3.10,
    'Na2': 3.07,
    'Mg2': 3.89,
    'P2': 1.83,
    'S2': 1.88,
    'Cl2': 1.98,
    'Ar2': 3.75,
    'K2': 3.90,
    'Br2': 2.28,
    'I2': 2.66,
    
    'HCl': 1.38,
    'CO2': 1.16,
    'H2O': 1.0,
}

angle = {
    'H2O': 104.48,
}

molecules = {
    'H2': ['H', 'H'],
    'Li2': ['Li', 'Li'],
    'Be2': ['Be', 'Be'],
    'B2': ['B', 'B'],
    'C2': ['C', 'C'],
    'N2': ['N', 'N'],
    'O2': ['O', 'O'],
    'F2': ['F', 'F'],
    'Ne2': ['Ne', 'Ne'],
    'Na2': ['Na', 'Na'],
    'Mg2': ['Mg', 'Mg'],
    'P2': ['P', 'P'],
    'S2': ['S', 'S'],
    'Cl2': ['Cl', 'Cl'],
    'Ar2': ['Ar', 'Ar'],
    'Br2': ['Br', 'Br'],
    'I2': ['I', 'I'],
    'K2': ['K', 'K'],
    
    'HCl': ['H', 'Cl'],
    'CO2': ['C', 'O', 'O'],
    'H2O': ['O', 'H', 'H'],
}

def make_atom(type, x, y, z):
    a = sphere(pos=vec(x, y, z), color=atom[type]['color'], radius=atom[type]['radius'])
    return a

def make_bond(bond_length, bond_type, x, y, z, direction=vec(1, 0, 0)):
    if bond_type == 'simple':
        sigma1 = cylinder(pos=vec(x, y, z), axis=direction * bond_length, radius=bond['radius'], color=color.white)
    elif bond_type == 'double':
        sigma1 = cylinder(pos=vec(x, y+bond['variation'], z), axis=direction * bond_length, radius=bond['radius'], color=color.white)
        pi2 = cylinder(pos=vec(x, y-bond['variation'], z), axis=direction * bond_length, radius=bond['radius'], color=color.white)
    elif bond_type == 'triple':
        pi1 = cylinder(pos=vec(x, y+bond['variation'], z), axis=direction * bond_length, radius=bond['radius'], color=color.white)
        sigma1 = cylinder(pos=vec(x, y, z), axis=direction * bond_length, radius=bond['radius'], color=color.white)
        pi2 = cylinder(pos=vec(x, y-bond['variation'], z), axis=direction * bond_length, radius=bond['radius'], color=color.white)
    return

class Molecule:
    def __init__(self, type, bond_type, xyz):
        self.type = type
        self.bond_type = bond_type
        self.xyz = xyz
        self.angle = angle.get(type, 0)
        self.atoms = molecules[type]
        self.bond_length = bond[type]

    def make_molecule(self):
        x, y, z = self.xyz
        atom_radius = atom[self.atoms[0]]['radius']
                
        for index, atom_type in enumerate(self.atoms):
            atom_radius = atom[atom_type]['radius']
                            
            if index == 0:
                make_atom(atom_type, x, y, z)
                
            elif index == 1:
                gap = atom[self.atoms[0]]['radius']
                make_bond(self.bond_length, self.bond_type, x + gap, y, z, direction=vec(1, 0, 0))
                make_atom(atom_type, x + gap + self.bond_length + atom_radius, y, z)
            elif index == 2:
                gap = atom[self.atoms[0]]['radius']
                if self.angle:
                    
                    bond_angle = self.angle / 2
                    
                    direction2 = vec(cos(radians(bond_angle)), sin(radians(bond_angle)), 0)
                    
                    make_bond(self.bond_length, self.bond_type, x + gap / 2, y + gap / 2, z, direction=direction2)
                    make_atom(self.atoms[2], x + self.bond_length * direction2.x + atom_radius, y + self.bond_length * direction2.y + atom_radius, z)
                else:
                    make_bond(self.bond_length, self.bond_type, x - gap, y, z, direction=vec(-1, 0, 0))
                    make_atom(atom_type, x - gap - self.bond_length - atom_radius, y, z)


h2 = Molecule('H2', 'simple', [0, 0, 0])
h2.make_molecule()

n2 = Molecule('N2', 'triple', [10, 0, 0])
n2.make_molecule()

o2 = Molecule('O2', 'double', [20, 0, 0])
o2.make_molecule()

f2 = Molecule('F2', 'simple', [30, 0, 0])
f2.make_molecule()

cl2 = Molecule('Cl2', 'simple', [40, 0, 0])
cl2.make_molecule()

br2 = Molecule('Br2', 'simple', [0, 4, 0])
br2.make_molecule()

i2 = Molecule('I2', 'simple', [10, 4, 0])
i2.make_molecule()

hcl = Molecule('HCl', 'simple', [20, 4, 0])
hcl.make_molecule()

co2 = Molecule('CO2', 'double', [30, 4, 0])
co2.make_molecule()

h2o = Molecule('H2O', 'simple', [40, 4, 0])
h2o.make_molecule()

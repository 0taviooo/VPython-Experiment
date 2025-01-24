
from include.molecules_class_module import Molecule

# Definição as moléculas disponíveis
h2 = Molecule('H2', [0, 0, 0])
h2.make_molecule()

n2 = Molecule('N2', [0, 0, 0])
n2.make_molecule()

o2 = Molecule('O2', [0, 0, 0])
o2.make_molecule()

f2 = Molecule('F2', [0, 0, 0])
f2.make_molecule()

cl2 = Molecule('Cl2', [0, 0, 0])
cl2.make_molecule()

br2 = Molecule('Br2', [0, 0, 0])
br2.make_molecule()

i2 = Molecule('I2', [0, 0, 0])
i2.make_molecule()

hcl = Molecule('HCl', [0, 0, 0])
hcl.make_molecule()

co2 = Molecule('CO2', [0, 0, 0])
co2.make_molecule()

h2o = Molecule('H2O', [0, 0, 0])
h2o.make_molecule()

hcn = Molecule('HCN', [0, 0, 0])
hcn.make_molecule()

no2 = Molecule('NO2', [0, 0, 0])
no2.make_molecule()

o3 = Molecule('O3', [0, 0, 0])
o3.make_molecule()

so2 = Molecule('SO2', [0, 0, 0])
so2.make_molecule()

of2 = Molecule('OF2', [0, 0, 0])
of2.make_molecule()

co = Molecule('CO', [0, 0, 0])
co.make_molecule()

cs = Molecule('CS', [0, 0, 0])
cs.make_molecule()

sio = Molecule('SiO', [0, 0, 0])
sio.make_molecule()

sis = Molecule('SiS', [0, 0, 0])
sis.make_molecule()

hco = Molecule('HCO', [0, 0, 0])
hco.make_molecule()

hcs = Molecule('HCS', [0, 0, 0])
hcs.make_molecule()

hsio = Molecule('HSiO', [0, 0, 0])
hsio.make_molecule()

hsis = Molecule('HSiS', [0, 0, 0])
hsis.make_molecule()

hoc = Molecule('HOC', [0, 0, 0])
hoc.make_molecule()

hsc = Molecule('HSC', [0, 0, 0])
hsc.make_molecule()

hosi = Molecule('HOSi', [0, 0, 0])
hosi.make_molecule()

hssi = Molecule('HSSi', [0, 0, 0])
hssi.make_molecule()

# Definição uma lista com todas as moléculas declaradas
molecules_list: list[Molecule] = [
    h2,
    n2,
    o2,
    f2,
    cl2,
    br2,
    i2,
    hcl,
    sio,
    co,
    cs,
    sis,
    co2,
    h2o,
    hcn,
    no2,
    o3,
    so2,
    of2,
    hco,
    hcs,
    hsio,
    hsis,
    hoc,
    hsc,
    hosi,
    hssi,
]

# Função para selecionar a molécula a ser visível
def select_molecule(type: str, ml: list[Molecule] = molecules_list) -> None:
    """
    Selects and highlights a molecule in the 3D simulation.

    This function adjusts the visibility of atoms and bonds in a molecular model 
    to highlight a selected molecule. The selected molecule's components are fully 
    visible, while all other molecules are hidden by setting their opacity to zero.

    Parameters:
        type (str): The type of the molecule to select (e.g., 'H2', 'CO2').
        ml (list[Molecule]): A list of Molecule objects available in the simulation.

    Behavior:
        - The selected molecule's atoms and bonds will have their opacity set to 1 (visible).
        - All other molecules' atoms and bonds will have their opacity set to 0 (hidden).

    Returns:
        None: This function modifies the visual representation directly in the 3D scene.
    """
    
    for molecule in ml: 
        if molecule.type == type:
            for atom in molecule.atoms:
                atom.opacity = 1
            for bond_set in molecule.bonds:
                for bond in bond_set:
                    bond.opacity = 1
        else:
            for atom in molecule.atoms:
                atom.opacity = 0
            for bond_set in molecule.bonds:
                for bond in bond_set:
                    bond.opacity = 0

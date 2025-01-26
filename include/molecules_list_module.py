
from include.molecules_class_module import Molecule
from include.molecules_dict_module import molecules

# Definição as moléculas disponíveis
molecules_list: list[Molecule] = []

for m in molecules.keys():
    molecules_list.append(Molecule(m, [0, 0, 0]))
    molecules_list[-1].make_molecule()

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

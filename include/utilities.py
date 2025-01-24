
from vpython import sphere, vector, vec, cylinder, color
from include.bond_module import bond
from include.atom_module import atom

# Definição da função para a criação dos átomos
def make_atom(type: str, x: float, y: float, z: float) -> sphere:
    """
    Creates a 3D representation of an atom using a sphere.

    This function generates a visual sphere that represents an atom in a molecular model. 
    The atom's appearance is determined by its type, which defines its color and radius.

    Parameters:
        type (str): The type of the atom (e.g., 'H' for hydrogen, 'O' for oxygen).
        x (float): The x-coordinate for the atom's position in 3D space.
        y (float): The y-coordinate for the atom's position in 3D space.
        z (float): The z-coordinate for the atom's position in 3D space.

    Returns:
        sphere: A VPython sphere object representing the atom at the specified coordinates.
    """
    
    a = sphere(pos=vec(x, y, z), color=atom[type]['color'], radius=atom[type]['radius'])
    return a

# Definição da função para a criação de ligações atômicas
def make_bond(bond_length: float, bond_type: str, x: float, y: float, z: float, direction: vector=vec(1, 0, 0)) -> list[cylinder]:
    """
    Constructs a visual representation of a chemical bond between atoms.

    This function creates one or more cylinders that represent bonds between atoms based on the specified bond type (simple, double, or triple). Each bond is positioned according to given coordinates and extends in a specified direction.

    Parameters:
        bond_length (float): The length of the bond to be created.
        bond_type (str): The type of bond ('simple', 'double', or 'triple').
        x (float): The x-coordinate for positioning the bond.
        y (float): The y-coordinate for positioning the bond.
        z (float): The z-coordinate for positioning the bond.
        direction (vector): A VPython vector indicating the direction of the bond. Defaults to the positive x-axis.

    Returns:
        list: A list of VPython cylinder objects representing the bonds created.
    
    Bond Types:
        - 'simple': Creates a single cylindrical bond.
        - 'double': Creates two parallel cylindrical bonds offset vertically.
        - 'triple': Creates three cylindrical bonds with one central and two offset vertically.

    Each bond is represented as a cylinder with specified radius and color. The cylinders are positioned based on their type to accurately depict the molecular structure.
    """
    
    bonds: list[cylinder] = []
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

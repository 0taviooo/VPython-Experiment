from vpython import color
from include.new_colors_module import new_colors

# Definição de um dicionário com os átomos e seus respectivos raios e cores
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
from vpython import color
from include.new_colors_module import new_colors
from typing import Any

# Definição de um dicionário com os átomos e seus respectivos raios e cores
atom: dict[str, Any] = {
    'H': {
		'name': 'Hidrogênio',
		'radius': 0.53,
		'color': color.white,
	},
    
    'C': {
		'name': 'Carbono',
		'radius': 0.67,
		'color': color.black,
	},
    
    'N': {
		'name': 'Nitrogênio',
		'radius': 0.56,
		'color': color.blue,
	},
    
    'O': {
		'name': 'Oxigênio',
		'radius': 0.48,
		'color': color.red,
	},
    
    'F': {
		'name': 'Flúor',
		'radius': 0.42,
		'color': color.green,
	},
    'Cl': {
		'name': 'Cloro',
		'radius': 0.79,
		'color': color.green,
	},
    
    'Br': {
		'name': 'Brômio',
		'radius': 0.94,
		'color': new_colors.dark_red,
	},
    
    'I': {
		'name': 'Iodo',
		'radius': 1.15,
		'color': color.purple,
	},
    
    'He': {
		'name': 'Hélio',
		'radius': 0.31,
		'color': color.cyan,
	},
    'Ne': {
		'name': 'Neônio',
		'radius': 0.38,
		'color': color.cyan,
	},
    'Ar': {
		'name': 'Argônio',
		'radius': 0.71,
		'color': color.cyan,
	},
    'Kr': {
		'name': 'Criptônio',
		'radius': 0.87,
		'color': color.cyan,
	},
    'Xe': {
		'name': 'Xenônio',
		'radius': 1.08,
		'color': color.cyan,
	},
    'Rn': {
		'name': 'Radônio',
		'radius': 1.20,
		'color': color.cyan,
	},
    
    'P': {
		'name': 'Fósforo',
		'radius': 0.98,
		'color': color.orange,
	},
    
    'S': {
		'name': 'Enxofre',
		'radius': 0.87,
		'color': color.yellow,
	},
    
    'B': {
		'name': 'Boro',
		'radius': 0.87,
		'color': new_colors.beige,
	},
    
    'Li': {
		'name': 'Lítio',
		'radius': 1.67,
		'color': color.magenta,
	},
    'Na': {
		'name': 'Sódio',
		'radius': 1.90,
		'color': color.magenta,
	},
    'K': {
		'name': 'Potássio',
		'radius': 2.43,
		'color': color.magenta,
	},
    'Rb': {
		'name': 'Rubídio',
		'radius': 2.95,
		'color': color.magenta,
	},
    'Cs': {
		'name': 'Césio',
		'radius': 2.98,
		'color': color.magenta,
	},
    
    
    'Be': {
		'name': 'Berílio',
		'radius': 1.12,
		'color': new_colors.dark_green,
	},
    'Mg': {
		'name': 'Magnésio',
		'radius': 1.45,
		'color': new_colors.dark_green,
	},
    'Ca': {
		'name': 'Cálcio',
		'radius': 1.94,
		'color': new_colors.dark_green,
	},
    'Sr': {
		'name': 'Estrôncio',
		'radius': 2.19,
		'color': new_colors.dark_green,
	},
    'Ba': {
		'name': 'Bário',
		'radius': 2.53,
		'color': new_colors.dark_green,
	},
    
    'Ti': {
		'name': 'Titânio',
		'radius': 1.76,
		'color': new_colors.grey,
	},
    
    'Fe': {
		'name': 'Ferro',
		'radius': 1.56,
		'color': new_colors.dark_orange,
	},
    
    'Si': {
		'name': 'Silício',
		'radius': 1.11,
		'color': new_colors.pink,
	},
    'Au': {
		'name': 'Ouro',
		'radius': 1.74,
		'color': new_colors.pink,
	},
}
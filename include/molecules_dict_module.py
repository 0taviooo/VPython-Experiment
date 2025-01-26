
# Definição de um dicionário com as moléculas e seus respectivos átomos e ligações
molecules: dict[str, dict[str, list[str]]] = {
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
        'atoms': ['H', 'S', 'C'],
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

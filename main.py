
from include.molecules_list_module import molecules_list, select_molecule
from vpython import *

# Configuração inicial da cena
scene.width = 1300
scene.height = 400
scene.title = "\nSimulação: moléculas em 3D \n\n"

# Desativação dos controles do usuário sobre a câmera
scene.userzoom = False
scene.userspin = False
scene.userpan = False

# Selecionamento a primeira molécula a ser exibida como H2
select_molecule('H2')

# Definição o slider para o usuário variar a velocidade de rotação da molécula
scene.caption = "\nVarie a velocidade de rotação: \n\n"

def setspeed(s: slider) -> None:
    wt_spd.text = '{:1.2f}'.format(s.value)
    
sl_spd = slider(min=0, max=4, value=1.5, length=400, bind=setspeed, right=15)
wt_spd = wtext(text='{:1.2f}'.format(sl_spd.value))
scene.append_to_caption(' radianos p/s\n\n')

# Definição o slider para o usuário variar a distância de visualização da molécula
scene.append_to_caption("\nVarie a distância de visualização: \n\n")

def setzoom(s: slider) -> None:
    wt_z.text = '{:1.2f}'.format(s.value)
    
sl_z = slider(min=5, max=15, value=10, length=400, bind=setzoom, right=15)
wt_z = wtext(text='{:1.2f}'.format(sl_z.value))
scene.append_to_caption(' micrômetros de distância\n\n')

# Definição a função do menu de escolhas para o usuário selecionar a molécula que desejar
def M(m:menu) -> None:
    val: str = m.selected
    select_molecule(val)

molecules_choices = [choice.type for choice in molecules_list]
menu(choices=molecules_choices, index=0, bind=M)

# Função principal de execução
if __name__ == '__main__':
    # Definição a quantidade de quadros por segundo da tela
    dt: int = 60
    # Definição o ângulo a ser alterado para a câmera girar
    angle: float = 0
    while True:
        rate(dt)
        scene.camera.pos = vec(sl_z.value * cos(radians(angle)), 0, sl_z.value * sin(radians(angle)))
        scene.camera.axis = -scene.camera.pos
        angle += sl_spd.value
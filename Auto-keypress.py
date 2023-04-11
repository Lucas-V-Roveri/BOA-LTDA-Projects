from pynput.keyboard import Key, Controller
import time


def troca (tempo):
    teclado = Controller()

    teclado.press(Key.ctrl)
    teclado.press(Key.tab)
    teclado.release(Key.ctrl)
    teclado.release(Key.tab)
    time.sleep(tempo)



print(":::::::::::::::::::::::::::::::::::::::::::::::::")
print("::Auto-keypress::Criado:por:Lucas:Vilela:Roveri::")
print(":::::::::::::V2.0::::::::::::::08/03/2023::::::::")
print(":::::::::::::::::::::::::::::::::::::::::::::::::")

print("\n::Iniciando o programa::\n")
tempo = input("\nInsira o intervalo de tempo que deseja mudar de tela: ")
tempo = int(tempo)
resp = input("\nDeseja realizar o processo por tempo indifinido? Y/N: ")
resp = resp.upper()
vezes = 0
maximo = 0
if resp == "Y":
    vezes = 1
    while vezes > maximo:
        troca(tempo)
else:
    maximo = input("\nInsira a quantidade de vezes que deseja mudar de tela: ")
    maximo = int(maximo)
    while vezes <= maximo:
        troca(tempo)
        vezes+=1
    print("\n.:Processo finalizado:.")




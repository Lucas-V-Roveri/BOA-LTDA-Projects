import time
import os
import pynput
from pynput.keyboard import Key, Controller
import subprocess
import threading
import warnings
import paramiko

keyboard = Controller()

def adduser():
    host = pdv
    port = 22
    username = "root"
    password = "48265"
    print("\n.:Conectando-se ao Host:.")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(host, port, username, password)
    print(".:Criando ")
    username_new = "pdv"
    password_new = "159753!#EQlj"
    command_create_user = "sudo useradd -m -p $(openssl passwd -1 {}) {}".format(password_new, username_new)
    stdin, stdout, stderr = ssh.exec_command(command_create_user)

    print(stdout.read().decode())

    ssh.close()


def open_vnc_viewer():

    subprocess.call(["putty", "-ssh", pdv])

def visudo():
    time.sleep(3)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
    keyboard.type('root')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
    keyboard.type('48265')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
    keyboard.type('sudo su')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.type('visudo')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    contador = 0
    time.sleep(1)
    while contador < 19:
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        contador+=1
    with keyboard.pressed(Key.ctrl.value):
        keyboard.press('k')
        keyboard.release('k')
    time.sleep(1)
    keyboard.type('root ALL=(ALL:ALL)EXEC: ALL')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.type('pdv ALL=(ALL:ALL)NOPASSWD:EXEC: ALL')
    time.sleep(1)

    with keyboard.pressed(Key.ctrl.value):
        keyboard.press('s')
        keyboard.release('s')
        keyboard.press('x')
        keyboard.release('x')
    time.sleep(3)

    with keyboard.pressed(Key.alt.value):
        keyboard.press(Key.f4)
        keyboard.release(Key.f4)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)




#####################

n_loja = "Pdvs.txt"

loja = open(n_loja)

for pdv in loja:

    pdv = str(pdv)
    pdv = pdv.strip()
    print(".:Alterando Visudo no Host", pdv, ":.")
    t2 = threading.Thread(target=open_vnc_viewer)
    t1 = threading.Thread(target=visudo)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    adduser()



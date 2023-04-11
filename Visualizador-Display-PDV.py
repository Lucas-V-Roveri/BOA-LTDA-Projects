import threading
import paramiko
import subprocess
import os
import datetime

print(":::::::::::::::::::::::::::::::::::::::")
print(":::::Visualizador:::de:::Display:::::::")
print("::::Criado:por::Lucas:Vilela:Roveri::::")
print(":::::T.I-BOA::::::::::::::V.1.0::::::::")
print(":::::::::::::::::::::::::::::::::::::::\n")

host = input("=>Insira o IP do PDV que deseja conectar: ")
user = input("=>Insira o usuário do PDV: ")
pwd = input("=>Insira a senha do PDV: ")

today = datetime.date.today()
day = today.strftime("%d")

def tail():

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(":::::Conectando-se ao Host:::::")
    ssh_client.connect(hostname=host, username=user, password=pwd)
    print(":::Coletando Logs do Teclado:::")
    stdin, stdout, stderr = ssh_client.exec_command("tail -F /vmix/vmix/dataisp/logs/display."+day)
    for line in stdout:
        print(line.strip('\n'))
    print("\n:::::::::::::::::::::::::::::::::::::::")


def open_vnc_viewer():
    program_files = os.environ.get('ProgramFiles')
    if program_files:
        vnc_viewer_path = os.path.join(program_files, 'RealVNC', 'VNC Viewer', 'vncviewer.exe')
        if os.path.isfile(vnc_viewer_path):
            vnc_path = vnc_viewer_path
    print(":::Abrindo o VNC::::")
    subprocess.call([vnc_path, host])


resp = input("==>Deseja abrir o VNC? Y/N: ")
resp = resp.upper()
if resp == "Y":
    try:
        t1 = threading.Thread(target=tail)
        t2 = threading.Thread(target=open_vnc_viewer)

        t1.start()
        t2.start()

        t1.join()
        t2.join()
    except:
        print("#####################################")
        print("#Aplicação#VNC#Viewer#Não#encontrada#")
        print("#Iniciando#a#coleta#de#logs#do#Tail##")
        print("#####################################")
        tail()
else:
    tail()















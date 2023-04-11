import subprocess
import os
import time

import paramiko
n_loja = "Pdvs.txt"



client = paramiko.SSHClient()


client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

hosts = open(n_loja)
for ip in hosts:
    try:

        ip = ip.strip()
        hostname = ip
        username = 'root'
        password = '1'
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, username=username, password=password)
        user = 'root'
        new_password = '48265'
        command = f'echo "{user}:{new_password}" | chpasswd'
        stdin, stdout, stderr = client.exec_command(command)
        print("<::",hostname, " <==> Senha alterada::>")
        time.sleep(1)
        client.close()
    except:
        print(">::", ip, " <==> Senha correta::<")
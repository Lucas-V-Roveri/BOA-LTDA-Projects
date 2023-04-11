import paramiko
import os
import time


n_loja = "Pdvs.txt"
loja = open(n_loja)

def ftp():
    try:
     ssh = paramiko.SSHClient()
     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
     ssh.connect(hostname=pdv, username='root', password='48265')
     print("\n.:Conectando-se ao host como root:.")
     print(".:Iniciando Transferencia:.\n")
     sftp_client = ssh.open_sftp()
     sftp_client.put(localpath=r'C:\Users\estagio.ti2.BOA\Documents\teste\pasta\varboa.rar', remotepath=r'/home/varboa.rar')
     time.sleep(2)
     print("\n.:Transferencia completa:.\n")
     print("\n.:Iniciando descompactação do arquivo:.\n")
     stdin, stdout, stderr = ssh.exec_command('cd /home && sudo unrar varboa.rar')
     time.sleep(3)
     print(".:Descompactação completa:.")
     sftp_client.close()

     time.sleep(3)
     ssh.close()
    except:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=pdv, username='root', password='1')
        print("\n.:Conectando-se ao host como root:.")
        print("\n::Testando Senha Alternativa::")
        print(".:Iniciando Transferencia:.\n")
        sftp_client = ssh.open_sftp()
        sftp_client.put(localpath=r'C:\Users\estagio.ti2.BOA\Documents\teste\pasta\varboa.rar', remotepath=r'/home/varboa.rar')
        time.sleep(2)
        print("\n.:Transferencia completa:.\n")
        print("\n.:Iniciando descompactação do arquivo:.\n")
        stdin, stdout, stderr = ssh.exec_command('cd /home && sudo unrar varboa.rar')
        time.sleep(3)
        print(".:Descompactação completa:.")
        sftp_client.close()

        time.sleep(3)
        ssh.close()


def ssh():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("\n.:Conectando-se ao host com o usuário pdv:.")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=pdv, username='pdv', password='159753!#EQlj')
    stdin, stdout, stderr = ssh.exec_command('sudo su')
    time.sleep(2)
    print("\n==> Aplicando baseline do serviço SSH")
    stdin, stdout, stderr = ssh.exec_command('cd /home/varboa/ && sudo bash unix_corrections.sh --tech SSH -b "SSH - Default" --target-path /etc/ssh/sshd_config -i "6129,6118,6127,6108,6101" -y no')
    output = stdout.read()
    err = stderr.read()
    print(output)
    print(err)
    time.sleep(1)
    print("\n==> Aplicando baseline geral")
    stdin, stdout, stderr = ssh.exec_command('cd /home/varboa/ && sudo bash unix_corrections.sh --tech Linux -b "Linux_PDV - Default" -y no')
    output = stdout.read()
    err = stderr.read()
    print(output)
    print(err)
    print("\n.:Encerrando a conexão:.")
    time.sleep(5)
    ssh.close()




for pdv in loja:
    try:
     pdv = str(pdv)
     pdv = pdv.strip()
     print("\n.:| ", pdv, " |:.\n")
     ftp()
     ssh()

    except:
     print("\nUm erro foi encontrado durante o processo do seguinte host ==> ", pdv)
     pass

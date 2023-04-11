#! /usr/bin/python3
import linecache
from paramiko import SSHClient
import paramiko
import time
import glob
import os

print(":::::::::::::::::::::::::::::::::::::::::::::::")
print("::T.I-BOA::::Gerenciador:de:versao:::PDV:::::::")
print("::::Script:::Criado::Por:::>Lucas::Vilela<:::::")
print("::::::::V1.0:::::Data:::03/03/2023:::::::::::::")
print(":::::::::::::::::::::::::::::::::::::::::::::::\n\n")

def main_menu():
	resp = True
	while resp:
		print ("\nO que deseja fazer:\n1. Atualizar versão do PDV \n2. Backup da versão atual\n3. Rollback da versão do PDV\n4. Rebootar o PDV\n5. Configurar os IPs \n6. Encerrar")
		resp = input ("\nInsira a opçao desejada: ")
		if resp == "1":
			att_pdv()
		elif resp == "2":
			backup()
		elif resp == "3":
			rollback()
		elif resp == "4":
			reboot()
		elif resp == "5":
			r = input("Deseja configurar os Ips? Y/N: ")
			r.upper()
			if r == "Y":
				ips()
			else:
				print("\nPara configurar as lojas manualmente faça o seguinte procedimento:\n\n1.Crie um txt com o seguinte formato: \nLnumero.txt \nExemplo: L01.txt\n\n2.Adicione os ips em linhas separadas \nExemplo:\n10.199.4.20\n10.199.4.21\n\n")
				input("Pressione ENTER para continuar\n")
		elif resp == "6":
			print ("\nEncerrando o programa")
			quit()
		else:
			print ("Opção invalida")

def att_pdv():
	print("\n::::::::::::::::::::::::::")
	print(":::ATUALIZAR-VERSÃO-PDV:::")
	print("::::::::::::::::::::::::::\n\n")

	arquivo = input("\nInsira o nome do arquivo para a atualização: ")
	arquivo = "arquivos\\"+arquivo
	numero_loja = input("\nInsira o conjunto de IPs que deseja atualizar: ")
	user = input("\nInsira o usuário da máquina: ")
	pwd = input("\nInsira a senha da máquina: ")
	r = input("\nDeseja tentar uma senha alternativa? Y/N: ")
	r.upper()
	if r == "Y":
		pwd2 = input("Insira a senha alternativa: ")
	numero_loja = 'config\\ip-lojas\\'+numero_loja
	loja = open(numero_loja)
	contador = 1
	for ips in loja:
		try:
			print(":::::::::::::::::::::::::::::::::::::::")
			host = linecache.getline(numero_loja, contador)
			print("\n",host)
			host = host.strip()

			ssh = SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(hostname=host, username=user, password=pwd)
			print("\n.:Conectando-se ao host:.")

			ftp_client = ssh.open_sftp()
			ftp_client.put(arquivo, r"/vmix/vmix/pdv/teste.txt")
			ftp_client.close()
			print("\n.:Transferindo os arquivos:.")

			stdin, stdout, stderr = ssh.exec_command("chmod 777 /vmix/vmix/pdv/*")
			print("\n.:Aplicando Permissoes:.")
			print("\n:::::::::::::::::::::::::::::::::::::::")

			time.sleep(2)
			ssh.close()
			contador +=1
		except:
			try:
				if pwd2 == "":
					print("\nSenha alternativa não configurada\n")
				else:
					host = linecache.getline(numero_loja, contador)
					print(host)
					host = host.strip()
					ssh = SSHClient()
					ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
					ssh.connect(hostname=host, username=user, password=pwd2)
					print(".:Tentando conectar-se ao host com senha alternativa:.")

					ftp_client = ssh.open_sftp()
					ftp_client.put(arquivo, r"/vmix/vmix/pdv/teste.txt")
					ftp_client.close()
					print("\n.:Transferindo arquivos:.")
					stdin, stdout, stderr = ssh.exec_command("chmod 777 /vmix/vmix/pdv/*")
					print("\n.:Aplicando permissoes:.")
					time.sleep(2)
					ssh.close()
					contador += 1
					print("\n:::::::::::::::::::::::::::::::::::::::")

			except:
				print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
				print(":Um erro foi encontrado durante a conexão com o host: ", host,":")
				print(":::Por favor, verifique as informações inseridas e tente novamente::")
				print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
				contador += 1
	print("\n::::::::::::::Processo finalizado::::::::::::::::")
	input(".:Pressione ENTER para voltar ao menu principal:.\n")
	main_menu()

def backup():
	print("\n:::::::::::::::::::::::::")
	print("::::BACKUP-VERSÃO-PDV::::")
	print(":::::::::::::::::::::::::\n\n")

	r = input("\nDeseja realizar o backup da versao atual? Y/N: ")
	r = r.upper()
	if r == "N":
		print ("\nRetornando ao menu principal\n")
	else:
		numero_loja = input("\nInsira o conjunto de IPs em que deseja realizar o backup: ")
		numero_loja = 'config\\ip-lojas\\'+numero_loja
		loja = open(numero_loja)

		user = input("\nInsira o usuário da máquina: ")
		pwd = input("\nInsira a senha da máquina: ")
		r = input("\nDeseja tentar uma senha alternativa? Y/N: ")
		r.upper()
		print("\n")
		if r == "Y":
			pwd2 = input("Insira a senha alternativa: ")
		contador = 1
		for ips in loja:
			try:
				host = linecache.getline(numero_loja, contador)
				print(host)
				host = host.strip()
				ssh = SSHClient()
				ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				ssh.connect(hostname=host, username=user, password=pwd)

				stdin, stdout, stderr = ssh.exec_command("cp /vmix/vmix/pdv/teste.txt /vmix/vmix/pdv/teste.txt.backup && chmod 777 /vmix/vmix/pdv/*")
				time.sleep(2)
				ssh.close()
				contador += 1
			except:
					try:
						host = linecache.getline(numero_loja, contador)
						print(host)
						host = host.strip()
						ssh = SSHClient()
						ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
						ssh.connect(hostname=host, username=user, password=pwd2)

						stdin, stdout, stderr = ssh.exec_command("cp /vmix/vmix/pdv/versao.nfce /vmix/vmix/pdv/versao.nfce.backup && chmod 777 /vmix/vmix/pdv/*")
						time.sleep(2)
						ssh.close()
						contador += 1
					except:
						print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
						print(":Um erro foi encontrado durante a conexão com o host: ", host, ":")
						print(":::Por favor, verifique as informações inseridas e tente novamente::")
						print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
						contador += 1
		print("\n::::::::::::::Processo finalizado::::::::::::::::")
		input(".:Pressione ENTER para voltar ao menu principal:.\n")
		main_menu()


def rollback():
	print("\n::::::::::::::::::::::::::")
	print(":::ROLLBACK-VERSÃO-PDV:::")
	print("::::::::::::::::::::::::::\n\n")

	numero_loja = input("\nInsira o conjutno de IPs em que deseja realizar o rollback: ")
	numero_loja = 'config\\ip-lojas\\' + numero_loja
	loja = open(numero_loja)
	contador = 1

	user = input("\nInsira o usuário da máquina: ")
	pwd = input("\nInsira a senha da máquina: ")
	r = input("\nDeseja tentar uma senha alternativa? Y/N: ")
	r.upper()
	print("\n")
	if r == "Y":
		pwd2 = input("Insira a senha alternativa: ")
	for ips in loja:
		try:
			host = linecache.getline(numero_loja, contador)
			print(host)
			host = host.strip()
			ssh = SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(hostname=host, username=user, password=pwd)

			stdin, stdout, stderr = ssh.exec_command("mv /vmix/vmix/pdv/teste.txt /vmix/vmix/pdv/teste.txt.rollback && cp /vmix/vmix/pdv/teste.txt.backup /vmix/vmix/pdv/teste.txt && chmod 777 /vmix/vmix/pdv/*")
			time.sleep(2)
			ssh.close()
			contador += 1
		except:
			try:
				host = linecache.getline(numero_loja, contador)
				print(host)
				host = host.strip()
				ssh = SSHClient()
				ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				ssh.connect(hostname=host, username=user, password=pwd2)
				stdin, stdout, stderr = ssh.exec_command("mv /vmix/vmix/pdv/versao.nfce /vmix/vmix/pdv/versao.nfce.rollback && cp /vmix/vmix/pdv/versao.nfce.backup /vmix/vmix/pdv/versao.nfce && chmod 777 /vmix/vmix/pdv/*")
				time.sleep(2)
				ssh.close()
				contador += 1
			except:
				print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
				print(":Um erro foi encontrado durante a conexão com o host: ", host, ":")
				print(":::Por favor, verifique as informações inseridas e tente novamente::")
				print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
				contador += 1
	print("\n::::::::::::::Processo finalizado::::::::::::::::")
	input(".:Pressione ENTER para voltar ao menu principal:.\n")
	main_menu()

def reboot():
	print("\n::::::::::::::::")
	print(":::REBOOT-PDV:::")
	print("::::::::::::::::\n")

	resp = input("\nDeseja Reiniciar o PDV? Y/N: ")
	resp = resp.upper()

	if resp == "N":
		print("\n.:Retornando ao menu principal:.\n")
		main_menu()
	else:
		resp2 = input("\nTem .:CERTEZA:. de que Deseja Reiniciar o PDV? Y/N:")
		resp2 = resp2.upper()
		if resp2 == "N":
			print("\n.:Retornando ao menu principal:.\n")
			main_menu()
		else:
			print("\n!!!!!!Tenha a certeza de que nenhum processo esta rodando no PDV no momento do reboot!!!!!!")

	pdv_loja = input("\nInsira o IP da maquina: ")
	user = input("\nInsira o usuário da máquina: ")
	pwd = input("\nInsira a senha da máquina: ")

	try:
		host = pdv_loja
		print(host)
		host = host.strip()
		ssh = SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname=host, username=user, password=pwd)

		stdin, stdout, stderr = ssh.exec_command("reboot")
		time.sleep(2)
		ssh.close()

	except:
		print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
		print(":Um erro foi encontrado durante a conexão com o host: ", host, ":")
		print(":::Por favor, verifique as informações inseridas e tente novamente::")
		print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
	print("\n::::::::::::::Processo finalizado::::::::::::::::")
	input(".:Pressione ENTER para voltar ao menu principal:.\n")
	main_menu()

def ips():
	print("\n::::::::::::::::::")
	print(":::IPS-PDV/LOJA:::")
	print("::::::::::::::::::\n\n")

	ip_pdv = input("Como deseja nomear este preset: ")
	ip_pdv = ("L"+ip_pdv+".txt")
	print("O preset se chamara: ", ip_pdv)
	r = input("\nDeseja prosseguir? Y/N: ")
	r = r.upper()
	if r == "N":
		print(".:Reiniciando o processo:.")
		ips()
	else:
		ip_pdv = ("config\\ip-lojas\\"+ip_pdv)
	with open(ip_pdv, 'w') as l:
		resp = input("\nDeseja definir um padrão de domínio e um período de IPs para a configuração? Y/N:")
		resp = resp.upper()
		if resp == "Y":
			contador = 1
			domínio = input("\nUtilize o modelo a seguir: 10.13.22.\nDigite o domínio: ")
			hosts = input("Digite a quantidade de hosts que deseja utilizar: ")
			print("\n.:Iniciando o processo:.")
			while contador <= int(hosts):

				ip = domínio+str(contador)
				print("\nAdicionando o IP: ", ip)
				l.write(ip)
				l.write("\n")
				contador+=1
		else:
			print("\n.:Iniciando o processo:.\n.:Para concluir o processo Pressione ENTER:.")
			contador = 1
			ip = "ip"
			while ip.strip() != "":
				print("\nDigite o ", contador, " IP :\n ")
				ip = input()
				if ip == "":
					print("\n::Encerrando::\n")
				else:
					ip = ip+"\n"
					l.write(ip)
					contador+=1
		print(".:Processo concluido:.")

main_menu()

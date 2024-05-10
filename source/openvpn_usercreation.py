#!/usr/bin/env python3

import subprocess
import os, time, shutil, tempfile
from ovpn_config import openvpn_config

user_VPN = input("Escolha o nome do usuário da VPN ")

print("Entrar no diretório easy-rsa")

first_command = os.chdir("/home/openvpn/easy-rsa/")

print("Criação do Certificado")

second_command  = "./easyrsa gen-req {user} pass".format(user = user_VPN)
second_result = subprocess.run(second_command, shell=True)

time.sleep(2)

fourth_command = "./easyrsa sign-req client {user}".format(user = user_VPN)
fourth_result = subprocess.run(fourth_command, shell=True)

print("Criação do TLS Crypt V2")

fifth_command = os.chdir("/home/openvpn/easy-rsa/pki/")

sixth_command = "openvpn --tls-crypt-v2 private/vpn_server.pem --genkey tls-crypt-v2-client private/{user}.pem".format(user = user_VPN)
sixth_result = subprocess.run(sixth_command, shell=True)

print("Criação do diretório do usuário")

seventh_command = os.chdir("/home/openvpn/vpn_clients/")

eighth_command = "mkdir {user}".format(user = user_VPN)
eighth_result = subprocess.run(eighth_command, shell=True)

print("Cópia do arquivo ca.crt")

nineth_command = os.chdir("/home/openvpn/easy-rsa/pki/")
nineth_result = "cp ca.crt /home/openvpn/vpn_clients/{user}/".format(user = user_VPN)
nineth_results = subprocess.run(nineth_result, shell=True)

print("Cópia do arquivo crt e key")

tenth_command = os.chdir("/home/openvpn/easy-rsa/pki/issued/")

eleventh_command = "cp {user}.crt /home/openvpn/vpn_clients/{user}".format(user = user_VPN)
eleventh_result = subprocess.run(eleventh_command, shell=True)

twelfth_command = os.chdir("/home/openvpn/easy-rsa/pki/private/")

print("Cópia das chaves.")

thirteenth_command = "cp {user}.key /home/openvpn/vpn_clients/{user}/".format(user = user_VPN)
thirteenth_result = subprocess.run(thirteenth_command, shell=True)

fourteenth_command = "cp {user}.pem /home/openvpn/vpn_clients/{user}/".format(user = user_VPN)
fourteenth_result = subprocess.run(fourteenth_command, shell=True)

print("Criação do arquivo OpenVPN")

fifteenth_command = os.chdir("/home/openvpn/vpn_clients/{user}".format(user = user_VPN))

with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
    temp_file.write(openvpn_config)
try:
    shutil.move(temp_file.name, 'make_client_ovpn.sh')
    print("Configuração do openvpn_config foram aplicadas.")
except Exception as e:
    print(f'Erro ao aplicar as configs do OpenVPN {e}')

sixteenth_command = "nano make_client_ovpn.sh"
sixteenth_result = subprocess.run(sixteenth_command, shell=True)

print("Tornando o arquivo OpenVPN executável e atribuindo para {user}".format(user = user_VPN))

seventeenth_command = "chmod +x make_client_ovpn.sh"
seventeenth_result = subprocess.run(seventeenth_command, shell=True)

print("Atribuição ao user.")

eighteenth_command = "./make_client_ovpn.sh {user}".format(user = user_VPN)
eighteenth_result = subprocess.run(eighteenth_command, shell=True)

print("Pause")

while True:
    final = input("A VPN foi criada com sucesso? (Y/N): ").strip().upper()  # Remover espaços em branco e converter para maiúsculas
    
    if final == "Y" or "sim" or "yes":
        print("VPN criada com sucesso =)")
        break  # Sai do loop se a resposta for "Y"
    elif final == "N" or "nao" or "no":
        print("Algum erro ocorreu no código, contate o time de infraestrutura =(")
        break  # Sai do loop se a resposta for "N"
    else:
        print("Valor inválido, tente novamente usando Y ou N")
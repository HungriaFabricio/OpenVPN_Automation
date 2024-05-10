#!/usr/bin/env python3

import subprocess
import os, time

user_VPN = input("Escolha o nome do usuário da VPN ")
password_VPN = input("Escolha a senha do usuário da VPN ")

# Entrar no diretório easy-rsa

first_command = os.chdir("/home/openvpn/easy-rsa/")

# Criação do Certificado

second_command  = "./easyrsa gen-req {user} pass".format(user = user_VPN)
second_result = subprocess.run(second_command, shell=True)

time.sleep(2)

fourth_command = "./easyrsa sign-req client {user}".format(user = user_VPN)
fourth_result = subprocess.run(fourth_command, shell=True)

# Criação do TLS Crypt V2

fifth_command = os.chdir("/home/openvpn/easy-rsa/pki/")

sixth_command = "openvpn --tls-crypt-v2 private/vpn_server.pem --genkey tls-crypt-v2-client private/{user}.pem".format(user = user_VPN)
sixth_result = subprocess.run(sixth_command, shell=True)

#Criação do diretório do usuário

seventh_command = os.chdir("cd ~/vpn_clients")

eighth_command = "mkdir {user}".format(user = user_VPN)
eighth_result = subprocess.run(eighth_command, shell=True)

# Cópia do arquivo ca.crt

nineth_command = os.chdir("cd ~/easy-rsa/pki/")
nineth_result = "cp ca.crt ~/vpn_clients/{user}".format(user = user_VPN)
nineth_results = subprocess.run(nineth_result, shell=True)

# Cópia do arquivo crt e key

tenth_command = os.chdir("cd ~/easy-rsa/pki/issued/")

eleventh_command = "cp {user}.crt ~vpn_clientes/{user}".format(user = user_VPN)
eleventh_result = subprocess.run(eleventh_command, shell=True)

twelfth_command = os.chdir("cd ~/easy-rsa/pki/private/")

# Cópia das chaves.

thirteenth_command = "cp {user}.key ~/vpn_clients/{user}".format(user = user_VPN)
thirteenth_result = subprocess.run(thirteenth_command, shell=True)

fourteenth_command = "cp {user}.pem ~/vpn_clients/{user}".format(user = user_VPN)
fourteenth_result = subprocess.run(fourteenth_command, shell=True)

# Transfêrencia do make_client

fifteenth_command = os.chdir("cd /home/openvpn/vpn_clients")

sixteenth_command = "mv make_client_ovpn.sh /home/openvpn/vpn_clients/{user}".format(user = user_VPN)
sixteenth_result = subprocess.run(sixteenth_command, shell=True)

# Pause

final = input("O arquivo foi conclúido? Y/N ")
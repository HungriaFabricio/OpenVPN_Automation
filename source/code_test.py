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
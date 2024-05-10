#!/usr/bin/env python3

import subprocess
import os, time

user_VPN = input("Escolha o nome do usuário da VPN ")
password_VPN = input("Escolha a senha do usuário da VPN ")

# Entrar no diretório easy-rsa

first_command = os.chdir("cd ~/easy-rsa/")

# Criação do Certificado

second_command  = "./easyrsa gen-req {user} pass".format(user = user_VPN)
second_result = subprocess.run(second_command, shell=True)

time.sleep(2)

third_command = password_VPN
third_result = subprocess.run(third_command, shell=True)
# !/usr/bin/env python3

import subprocess
import os

user_VPN = input("Escolha o nome do usuário da VPN ")
password_VPN = input("Escolha a senha do usuário da VPN ")

# Entrar no diretório easy-rsa

first_command = "cd ~/easy-rsa/"
os.chdir("vapraesse")

print("O primeiro comando foi executado.")

second_result = subprocess.run("mkdir foicomsucesso", shell=True)
print("Verifique se o arquivo foi com sucesso")
# %%

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
# %%

# %%

# %%

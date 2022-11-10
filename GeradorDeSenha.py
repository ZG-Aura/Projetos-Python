import secrets
import string

print("-"*5 + "GERADOR DE SENHA" + "-"*5)
letra = string.ascii_letters
numero = string.digits
simbolo = "!@#$%&*_"
tamanho = input("Escolha o tamanho da senha: ")

senha_caracter = ''.join(secrets.choice(simbolo)) + ''.join(secrets.choice(letra) for i in range(int(tamanho) - 1))
senha_numero = ''.join(secrets.choice(numero) for i in range(int(tamanho)))

opcao = input("Deseja gerar senha ou pin ?").lower().strip()

while True:
    if opcao == "pin":
        print(f"O pin gerado é {senha_numero}")
        break
    if opcao == "senha":
        print(f"A senha gerada é `{senha_caracter}")
        break
    if opcao != "pin" or opcao != "senha":
        print("Digite uma opção válida!")
        opcao = input("Deseja gerar senha ou pin ?").lower().strip()

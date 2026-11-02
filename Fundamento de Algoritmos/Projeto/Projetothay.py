#cadastro
usuarios = []

def login():
    cpf_login = input("Digite seu CPF: ")
    senha_login = input("Digite sua senha: ")


    for usuario in usuarios:
        if usuario["cpf"] == cpf_login and usuario["senha"] == senha_login:
            print('Login realizado!')
            menu()
        

        else:
            while usuario["cpf"] != cpf_login and usuario["senha"] != senha_login:
                print("CPF ou senha incorretos.")
                cpf_login = input("Digite seu CPF: ")
                senha_login = input("Digite sua senha: ")



cpf = input("Digite seu CPF: ")

for usuario in usuarios:
    if usuario["cpf"] == cpf:
        print("Você já possui cadastro. Faça login para acessar sua conta.")
        login()
        break
else:
    print("Bem-vindo ao cadastro de usuário!")
    cpf_cadastro = input("Digite seu CPF sem pontos ou traços: ")
    while len(cpf_cadastro) != 11 or "." in cpf_cadastro or "-" in cpf_cadastro:
        print("CPF inválido. Tente novamente.")
        cpf_cadastro = input("Digite seu CPF sem pontos ou traços: ")
   


    senha_cadastro = input("Crie uma senha de até 6 dígitos: ")
    while len(senha_cadastro) > 6 or len(senha_cadastro) < 6:
        print("Senha inválida. Tente novamente.")
        senha_cadastro = input("Crie uma senha de até 6 dígitos: ")

    nome_cadastro = input("Digite seu nome completo: ")


print("Cadastro realizado com sucesso!")

usuarios.append ({
    "cpf": cpf_cadastro,
    "senha": senha_cadastro,
    "nome": nome_cadastro,
    "saldo": 0.0,
    "criptos" :{
        "Bitcoin": 0.0,
        "Ethereum": 0.0,
        "Ripple": 0.0,
    },
    "extrato": []
})




print(usuarios)

#menu

def menu():
    print("Bem-vindo ao menu de opções!")
    print("1. Consultar saldo")
    print("2. Consultar extrato")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Comprar criptomoedas")
    print("6. Vender criptomoedas")
    print("7. Atualizar cotação")
    print("8. Sair")

    while True:
        opcao = int(input("Digite o número da opção desejada: "))
    
        if opcao == 1:
            consultar_saldo()

        elif opcao == 2:
            consultar_extrato()
        elif opcao == 3:
            depositar()
        
        elif opcao == 4:
            sacar()
        elif opcao == 5:
            comprar_criptomoedas()
        elif opcao == 6:
            vender_criptomoedas()
        elif opcao == 7:
            atualizar_cotacao()
        elif opcao == 8:
            sair()
            break
        
        else:
            print("Opção inválida. Tente novamente.") 


#funcionamento das funções

def consultar_saldo():

    senha = input("Digite sua senha para consultar o saldo: ")
    if senha != senha_cadastro:
        print("Senha incorreta. Acesso negado.")
        return
    
    else:
        print(f"Nome: {nome_cadastro}")
        print(f"CPF: {cpf_cadastro}")
        print(f"Reais: R${saldo}")
        print(criptos[Bitcoin])
   


def consultar_extrato():
    senha = input("Digite sua senha para consultar o saldo: ")
    if senha != senha_cadastro:
        print("Senha incorreta. Acesso negado.")
        return
    



def depositar():
    global saldo
    valor_deposito = float(input("Digite o valor que deseja depositar: "))
    saldo += valor_deposito
    print(f"Depósito realizado com sucesso! Seu novo saldo é: R${saldo:.2f}")   


def sacar():
    global saldo
    valor_saque = float(input("Digite o valor que deseja sacar: "))
    if valor_saque <= saldo:
        saldo -= valor_saque
        print(f"Saque realizado com sucesso! Seu novo saldo é: R${saldo:.2f}")
    else:
        print("Saldo insuficiente.")




def comprar_criptomoedas():
    pass
def vender_criptomoedas():
    pass
def atualizar_cotacao():
    pass




def sair():
    print("Programa encerrado!")


#login



print(f"Bem-vindo ao login de usuário, {nome_cadastro}!")
login()
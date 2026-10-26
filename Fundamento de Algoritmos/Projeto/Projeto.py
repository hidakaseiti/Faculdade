#cadastro da pessoa (para registrar mais de um funcionario é necessario um vetor ou um dicionario)
cpf = int(input('CPF sem pontos e sem traços: '))
senha = int(input('Digite uma senha com seis dígitos: '))

#fazer um dicionario para cada usuario dentro de um dicionario, o primeiro guarda senha e login e o segundo guarda as informacoes de cada usuario

if not cpf or not senha:
    print("Erro: todos os campos são obrigatórios!")
else:
    print("Cadastro realizado com sucesso!")

cpf_login = input('Coloque seu cpf: ')
senha_login = input('Coloque sua senha: ')

#def consultarsaldo():
#def consultarextrato():
#def depositar():
#def sacar():
#def c_criptomoedas():
#def v_criptomoedas():
#def atu_cotacao():

def menu():
    print('1. Consultar saldo /n 2. Consultar extrato /n 3. Depositar /n 4. Sacar /n 5. Comprar criptomoedas /n 6. Vender criptomoedas /n 7. Atualizar cotação /n 8. Sair')
    while True:
        nav = int(input('Selecione o que quer fazer: '))
        if nav == 1:
            consultarsaldo()
        elif nav == 2:
            consultarextrato()
        elif nav == 3:
            depositar()
        elif nav == 4:
            sacar()
        elif nav == 5:
            c_criptomoedas()
        elif nav == 6:
            v_criptomoedas()
        elif nav == 7:
            atu_cotacao()
        elif nav == 8:
            print('Até logo!')
            break
        else:
            print('Erro: escolha um número de 1 a 8')
            menu()

if cpf == cpf_login and senha == senha_login:
    menu()
else:
    print('CPF ou senha incorretas')
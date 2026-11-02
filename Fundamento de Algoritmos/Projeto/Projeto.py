#cadastro da pessoa (para registrar mais de um funcionario é necessario um vetor ou um dicionario)
usuarios = {}
def cadastrar(usuarios):
    nome = input('Qual o seu nome? ')
    while True:
        cpf = int(input('CPF sem pontos e sem traços: '))
        if not cpf:
            print('Um CPF é necessário')
            continue
        if cpf in usuarios:
            print('CPF já cadastrado. Tente novamente.')
            continue
        else:
            break

    while True:
        senha = int(input('Digite uma senha com seis dígitos: '))
        if not senha:
            print('Uma senha de 6 dígitos é necessária')
            continue
        break

    usuarios[cpf] = {
        'cpf' : cpf,
        'nome' : nome,
        'senha' : senha,
        'brl': 0.0,
        'criptomoedas': {
            'bitcoin' : 0.0,
            'ethereum' : 0.0,
            'ripple' : 0.0,
        },
        'extrato' : []
    }

    print('Seu cadastro foi realizado!')

#fazer um dicionario para cada usuario dentro de um dicionario, o primeiro guarda senha e login e o segundo guarda as informacoes de cada usuario
from datetime import datetime

def consultarsaldo(cpf):
    senha = int(input('Digite sua senha: '))
    if senha == usuarios[cpf][senha]:
        print(f'{usuarios[cpf]['nome']}\n{usuarios[cpf]}\n\n{usuarios[cpf]['saldo']}\n{usuarios[cpf]['criptomoedas']}')
    else:
        print('Senha incorreta')
        menu()

def consultarextrato(cpf):
    senha = int(input('Digite sua senha: '))
    if senha == usuarios[cpf][senha]:
        print(f'{usuarios[cpf]['extrato']}')
    else:
        print('Senha incorreta')
        menu()

def depositar(cpf, deposito):
    senha = int(input('Digite sua senha: '))
    if senha == usuarios[cpf][senha]:
        deposito = float(input('Quanto deseja depositar: '))
        usuarios[cpf]['brl'] += deposito
        agora = datetime.now()
        transacao = [agora.strftime('%d/%m/%Y') ,agora.strftime('%H,%M:%S'),]
        usuarios[cpf]['extrato'].append[transacao]
        print(f'\n{usuarios[cpf]['brl']}\n{usuarios[cpf]['criptomoedas']}')
    else:
        print('Senha incorreta')
        menu()
        
def sacar(cpf, saque):
    senha = int(input('Digite sua senha: '))
    if senha == usuarios[cpf][senha]:
        saque = float(input('Quanto deseja sacar: '))
        usuarios[cpf]['brl'] -= saque
        extrato.append[transacao]
        print(f'\n{usuarios[cpf]['brl']}\n{usuarios[cpf]['criptomoedas']}')

    else:
        print('Senha incorreta')
        menu()
#def c_criptomoedas():
#def v_criptomoedas():
#def atu_cotacao():

def menu():
    print('1. Consultar saldo \n 2. Consultar extrato \n 3. Depositar \n 4. Sacar \n 5. Comprar criptomoedas \n 6. Vender criptomoedas \n 7. Atualizar cotação \n 8. Sair')
    while True:
        nav = int(input('Insira o que deseja fazer: '))
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
            print('Até logo,{usuarios[cpf][nome]}')
            break
        else:
            print('Erro: escolha um número de 1 a 8')
            menu()

def fazer_login(usuarios):
    cpf = int(input('CPF sem pontos e traços: '))
    senha = int(input('Digite sua senha de 6 dígitos: '))
    while True:
        if cpf in usuarios:
            if usuarios[cpf][senha] == senha:
                print(f'Bem vindo {usuarios[cpf][nome]}')
                break
        elif cpf not in usuarios or usuarios[cpf][senha] != senha:
            print('CPF ou senha incorreto(s)!')
        menu()
    #perguntar pro prof como fazer aqui em relação ao cpf e senha incorretos

def menuinicial():
    print('1.Cadastrar \n 2.Fazer login')
    nav = int(input('Insira o que deseja fazer'))
    while True:
        if nav == 1:
            cadastrar(usuarios)
        elif nav == 2:
            fazer_login(usuarios)

#criar uma função para salvar cada usuario num arquivo txt por ex:
#def save(f):
#    for u in usuarios.value:
#        f.write(f'u['cpf'])

#def load(f):
#    #de modo a reconstruir o dicionario e obter os valores
#cadastro da pessoa (para registrar mais de um funcionario é necessario um vetor ou um dicionario)
#Parâmetro: é a variável definida na criação da função. IMPORTANTE!!
#Argumento: é o valor que você passa quando chama a função. IMPORTANTE!!
usuarios = {}
## else: break é redundante Se a condição for verdadeira, o continue volta ao início do loop e o break nunca é alcançado. Se for falsa, o fluxo segue em frente e chega no break.
## int() derruba o programa com entrada vazia ou com letras. Se o usuário apertar Enter ou digitar abc, dá ValueError antes de chegar no if not cpf.
## int() remove zeros à esquerda. CPF 01234567890 vira 1234567890, e senha 012345 vira 12345. Com isso, nem dá para garantir que a senha tem 6 dígitos.
## Não há validação de tamanho. Hoje qualquer número passa, como 5 de CPF ou 1 de senha.

# def cadastrar(usuarios):
#     nome = input('Qual o seu nome? ')
#     while True:
#         cpf = int(input('CPF sem pontos e sem traços: '))
#         if not cpf:
#             print('Um CPF é necessário')
#             continue
#         if cpf in usuarios:
#             print('CPF já cadastrado. Tente novamente.')
#             continue
#         else:
#             break

#     while True:
#         senha = int(input('Digite uma senha com seis dígitos: '))
#         if not senha:
#             print('Uma senha de 6 dígitos é necessária')
#             continue
#         break

#     usuarios[cpf] = {
#         'cpf' : cpf,
#         'nome' : nome,
#         'senha' : senha,
#         'brl': 0.0,
#         'criptomoedas': {
#             'bitcoin' : 0.0,
#             'ethereum' : 0.0,
#             'ripple' : 0.0,
#         },
#         'extrato' : []
#     }
#     print('Seu cadastro foi realizado!')

def cadastrar(usuarios):
    nome = input('Qual o seu nome? ').strip()

    while True:
        cpf = input('CPF sem pontos e sem traços: ').strip()
        if len(cpf) != 11 or not cpf.isdigit():
            print('O CPF deve ter 11 dígitos numéricos.')
            continue
        if cpf in usuarios:
            print('CPF já cadastrado. Tente novamente.')
            continue
        break

    while True:
        senha = input('Digite uma senha com seis dígitos: ').strip()
        if len(senha) != 6 or not senha.isdigit():
            print('A senha deve ter exatamente 6 dígitos numéricos.')
            continue
        break

    usuarios[cpf] = {
        'cpf': cpf,
        'nome': nome,
        'senha': senha,
        'brl': 0.0,
        'criptomoedas': {
            'bitcoin': 0.0,
            'ethereum': 0.0,
            'ripple': 0.0,
        },
        'extrato': []
    }

    print('Seu cadastro foi realizado!')

#fazer um dicionario para cada usuario dentro de um dicionario, o primeiro guarda senha e login e o segundo guarda as informacoes de cada usuario
from datetime import datetime

def consultarsaldo(usuarios, cpf):
    senha = input('Digite sua senha: ')
    if senha == usuarios[cpf]['senha']:
        print(f'{usuarios[cpf]['nome']}\n{usuarios[cpf]['cpf']}\n\n{usuarios[cpf]['brl']}\n{usuarios[cpf]['criptomoedas']}')
    else:
        print('Senha incorreta')

def consultarextrato(usuarios, cpf):
    senha = input('Digite sua senha: ')
    if senha == usuarios[cpf]['senha']:
        print(f'{usuarios[cpf]['extrato']}')
    else:
        print('Senha incorreta')

def depositar(usuarios, cpf):
    senha = input('Digite sua senha: ')
    if senha == usuarios[cpf]['senha']:
        deposito = float(input('Quanto deseja depositar: '))
        if deposito > 0:
            usuarios[cpf]['brl'] += deposito
        else:
            print('Valor inválido')
        agora = datetime.now()
        transacao = [agora.strftime('%d/%m/%Y') ,agora.strftime('%H:%M:%S'), + , deposito, CT: cotacao, TX: taxa , REAL: usuarios[cpf]['brl'], BTC: usuarios[cpf][criptomoedas]['bitcoin'], ETH: usuarios[cpf][criptomoedas]['etherium'] ]
        usuarios[cpf]['extrato'].append(transacao)
        print(f'\n{usuarios[cpf]['brl']}\n{usuarios[cpf]['criptomoedas']}')
    else:
        print('Senha incorreta')
        
def sacar(usuarios, cpf):
    senha = input('Digite sua senha: ')
    if senha == usuarios[cpf]['senha']:
        saque = float(input('Quanto deseja sacar: '))
        if saque > 0 and saque <= usuarios[cpf]['brl']:
            usuarios[cpf]['brl'] -= saque
        else:
            print('Valor invalido ou saldo insuficiente')
        agora = datetime.now()
        transacao = [agora.strftime('%d/%m/%Y') ,agora.strftime('%H:%M:%S'), ]
        usuarios[cpf]['extrato'].append(transacao)
        print(f'\n{usuarios[cpf]['brl']}\n{usuarios[cpf]['criptomoedas']}')
    else:
        print('Senha incorreta')

#def c_criptomoedas():
#def v_criptomoedas():
#def atu_cotacao():

def menu(usuarios, cpf):
    print('1. Consultar saldo \n 2. Consultar extrato \n 3. Depositar \n 4. Sacar \n 5. Comprar criptomoedas \n 6. Vender criptomoedas \n 7. Atualizar cotação \n 8. Sair')
    while True:
        nav = int(input('Insira o que deseja fazer: '))
        if nav == 1:
            consultarsaldo(usuarios, cpf)
        elif nav == 2:
            consultarextrato(usuarios, cpf)
        elif nav == 3:
            depositar(usuarios, cpf)
        elif nav == 4:
            sacar(usuarios, cpf)
        elif nav == 5:
            c_criptomoedas(usuarios, cpf)
        elif nav == 6:
            v_criptomoedas(usuarios, cpf)
        elif nav == 7:
            atu_cotacao(usuarios, cpf)
        elif nav == 8:
            print(f'Até logo,{usuarios[cpf]['nome']}')
            break
        else:
            print('Erro: escolha um número de 1 a 8')

## cpf e senha estao fora do while true,ou seja,caso falhe,nao pedira novamente
## não é necessario elif,pois se o login nao da certo,o que resta é dar erro(senha incorreta)
## menu dentro de while true pode empilhar menus
## senha errada com cpf certo Quando o CPF existe, o if cpf in usuarios é verdadeiro. Se a senha estiver errada, o if interno não faz nada, e o elif nunca é avaliado, porque o if externo já foi escolhido. Resultado: nenhuma mensagem de erro.
## melhor deixar cpf e senha como strings e nao int

# def fazer_login(usuarios):
#     cpf = int(input('CPF sem pontos e traços: '))
#     senha = int(input('Digite sua senha de 6 dígitos: '))
#     while True:
#         if cpf in usuarios:
#             if usuarios[cpf]['senha'] == senha:
#                 print(f'Bem vindo {usuarios[cpf]['nome']}')
#                 break
#         elif cpf not in usuarios or usuarios[cpf]['senha'] != senha:
#             print('CPF ou senha incorreto(s)!')
#         menu()

def fazer_login(usuarios):
    while True:
        cpf = input('CPF sem pontos e traços: ')
        senha = input('Digite sua senha de 6 dígitos: ')

        if cpf in usuarios and usuarios[cpf]['senha'] == senha:
            print(f"Bem vindo {usuarios[cpf]['nome']}")
            return cpf

        print('CPF ou senha incorreto(s)!') #o print não é executado caso caia na condicional pois o return faz sair da função

def menuinicial():
    print('1.Cadastrar \n 2.Fazer login')
    while True:
        nav = int(input('Insira o que deseja fazer'))
        if nav == 1:
            cadastrar(usuarios)
        elif nav == 2:
            fazer_login(usuarios)
        else:
            print('Opção inválida')

#criar uma função para salvar cada usuario num arquivo txt por ex:
#def save(f):
#    for u in usuarios.value:
#        f.write(f'u['cpf'])

#def load(f):
#    #de modo a reconstruir o dicionario e obter os valores
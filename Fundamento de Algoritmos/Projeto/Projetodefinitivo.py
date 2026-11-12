from datetime import datetime
import random

usuarios = {}
cripto = {
    'bitcoin':  {'sigla': 'BTC', 'cotacao': 417026.10, 'taxa_compra': 0.02, 'taxa_venda': 0.03},
    'ethereum': {'sigla': 'ETH', 'cotacao': 12283.52,  'taxa_compra': 0.01, 'taxa_venda': 0.02},
    'ripple':   {'sigla': 'XRP', 'cotacao': 6.36,     'taxa_compra': 0.01, 'taxa_venda': 0.01},
}


def save_usuarios():
    with open('usuarios.txt', 'w'):

        for cpf, dados in usuarios.items():

            usuarios.txt.write(f"{cpf}\n")
            usuarios.txt.write(f"{dados['nome']}\n")
            usuarios.txt.write(f"{dados['senha']}\n")
            usuarios.txt.write(f"{dados['brl']}\n")

            for moeda, quantidade in dados['criptomoedas'].items():
                usuarios.txt.write(f"{quantidade}\n")

            for transacao in dados['extrato']:
                usuarios.txt.write(f"{transacao}\n")

            usuarios.txt.write("---\n")


def load_usuarios():
    global usuarios

    usuarios = {}

    try:
        with open('usuarios.txt', 'r'):

            linhas = usuarios.txt.readlines()

            cpf = None
            dados = []

            for linha in linhas:

                linha = linha.strip()

                if linha == '---':

                    usuarios[cpf] = {
                        'cpf': cpf,
                        'nome': dados[0],
                        'senha': dados[1],
                        'brl': float(dados[2]),
                        'criptomoedas': {
                            'bitcoin': float(dados[3]),
                            'ethereum': float(dados[4]),
                            'ripple': float(dados[5])
                        },
                        'extrato': dados[6:]
                    }

                    cpf = None
                    dados = []

                elif cpf is None:
                    cpf = linha

                else:
                    dados.append(linha)

    except FileNotFoundError:
        usuarios = {}


def save_cripto():
    with open('cripto.txt', 'w'):

        for moeda, dados in cripto.items():
            cripto.txt.write(f"{moeda}\n")
            cripto.txt.write(f"{dados['sigla']}\n")
            cripto.txt.write(f"{dados['cotacao']}\n")
            cripto.txt.write(f"{dados['taxa_compra']}\n")
            cripto.txt.write(f"{dados['taxa_venda']}\n")

def load_cripto():
    global cripto

    try:
        with open('cripto.txt', 'r'):

            linhas = cripto.txt.readlines()

            cripto = {}

            for i in range(0, len(linhas), 5):

                moeda = linhas[i].strip()

                cripto[moeda] = {
                    'sigla': linhas[i + 1].strip(),
                    'cotacao': float(linhas[i + 2].strip()),
                    'taxa_compra': float(linhas[i + 3].strip()),
                    'taxa_venda': float(linhas[i + 4].strip())
                }

    except FileNotFoundError:
        pass


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

    save_usuarios()

    print('Seu cadastro foi realizado!')

def fazer_login(usuarios, cripto):
    while True:
        cpf = input('CPF sem pontos e traços: ')
        senha = input('Digite sua senha de 6 dígitos: ')

        if cpf in usuarios and usuarios[cpf]['senha'] == senha:
            print(f"Bem vindo {usuarios[cpf]['nome']}")
            menu(usuarios, cripto, cpf)
            return
        else:
            print('CPF ou senha incorreto(s)!')

def mostrar_saldos(usuarios, cpf):
    print(f"Reais: {usuarios[cpf]['brl']:.2f}")
    print(f"Bitcoin: {usuarios[cpf]['criptomoedas']['bitcoin']:.2f}")
    print(f"Ethereum: {usuarios[cpf]['criptomoedas']['ethereum']:.2f}")
    print(f"Ripple: {usuarios[cpf]['criptomoedas']['ripple']:.2f}")    


def consultarsaldo(usuarios, cpf):
    senha = input('Digite sua senha: ')
    if senha == usuarios[cpf]['senha']:
        print(f"Nome: {usuarios[cpf]['nome']}")
        print(f"CPF: {usuarios[cpf]['cpf']}")
        mostrar_saldos(usuarios, cpf)
    else:
        print('Senha incorreta')

def consultarextrato(usuarios, cpf):
    senha = input('Digite sua senha: ')
    if senha == usuarios[cpf]['senha']:
        print(f"Nome: {usuarios[cpf]['nome']}\nCPF: {usuarios[cpf]['cpf']}")
        for elemento in usuarios[cpf]['extrato']:
            print(elemento)
    else:
        print('Senha incorreta')

def depositar(usuarios, cpf):
    deposito = float(input('Quanto deseja depositar: '))
    if deposito > 0:
        usuarios[cpf]['brl'] += deposito
    else:
        print('Valor inválido')
        return
    agora = datetime.now()
    transacao = (f"{agora.strftime('%d-%m-%Y %H:%M')} + {deposito:.2f} REAL "
                f"CT: 0.0 TX: 0.00 REAL: {usuarios[cpf]['brl']:.2f} "
                f"BTC: {usuarios[cpf]['criptomoedas']['bitcoin']} "
                f"ETH: {usuarios[cpf]['criptomoedas']['ethereum']} "
                f"XRP: {usuarios[cpf]['criptomoedas']['ripple']}")
    usuarios[cpf]['extrato'].append(transacao)

    save_usuarios()

    mostrar_saldos(usuarios, cpf)

        
def sacar(usuarios, cpf):
    saque = float(input('Quanto deseja sacar: '))
    if saque > 0 and saque <= usuarios[cpf]['brl']:
        usuarios[cpf]['brl'] -= saque
    else:
        print('Valor invalido ou saldo insuficiente')
        return
    agora = datetime.now()
    transacao = (f"{agora.strftime('%d-%m-%Y %H:%M')} - {saque:.2f} REAL "
                f"CT: 0.0 TX: 0.00 REAL: {usuarios[cpf]['brl']:.2f} "
                f"BTC: {usuarios[cpf]['criptomoedas']['bitcoin']} "
                f"ETH: {usuarios[cpf]['criptomoedas']['ethereum']} "
                f"XRP: {usuarios[cpf]['criptomoedas']['ripple']}")
    usuarios[cpf]['extrato'].append(transacao)

    save_usuarios()

    mostrar_saldos(usuarios, cpf)


def c_criptomoedas(usuarios, cripto, cpf):
    senha = input('Digite sua senha: ')
    if senha == usuarios[cpf]['senha']:
        print(f"Cotações: \n Bitcoin: {cripto['bitcoin']['cotacao']:.2f}\n Ethereum: {cripto['ethereum']['cotacao']:.2f}\n Ripple: {cripto['ripple']['cotacao']:.2f}")
        print(f"1.Bitcoin\n2.Ethereum\n3.Ripple")
        comprar = int(input('Qual moeda deseja comprar: '))
        if comprar == 1:
            moeda = 'bitcoin'
        elif comprar == 2:
            moeda = 'ethereum'
        elif comprar == 3:
            moeda = 'ripple'
        else:
            print('Opção inválida')
            return
        quantidade = float(input('Quanto gostaria de comprar? '))
        cotacao = cripto[moeda]['cotacao']
        taxa = cripto[moeda]['taxa_compra']
        precosemtaxa = quantidade * cotacao
        precocomtaxa = precosemtaxa * (1 + taxa)
        
        if quantidade > 0:
            if precocomtaxa <= usuarios[cpf]['brl']:
                usuarios[cpf]['criptomoedas'][moeda] += quantidade
                usuarios[cpf]['brl'] -= precocomtaxa
            else:
                print('Saldo insuficiente')
                return
        else:
            print('Quantidade inválida')
            return
        agora = datetime.now()
        transacao = (f"{agora.strftime('%d-%m-%Y %H:%M')} + {precosemtaxa:.2f} {moeda} "
                    f"CT: {cotacao:.2f} TX: {taxa:.2f} REAL: {usuarios[cpf]['brl']:.2f} "
                    f"BTC: {usuarios[cpf]['criptomoedas']['bitcoin']} "
                    f"ETH: {usuarios[cpf]['criptomoedas']['ethereum']} "
                    f"XRP: {usuarios[cpf]['criptomoedas']['ripple']}")
        usuarios[cpf]['extrato'].append(transacao)

        save_usuarios()
    else:
        print('Senha incorreta')
    
def v_criptomoedas(usuarios, cripto, cpf):
    senha = input('Digite sua senha: ')
    if senha == usuarios[cpf]['senha']:
        print(f"Cotações: \n Bitcoin: {cripto['bitcoin']['cotacao']:.2f}\n Ethereum: {cripto['ethereum']['cotacao']:.2f}\n Ripple: {cripto['ripple']['cotacao']:.2f}")
        print(f"1.Bitcoin\n2.Ethereum\n3.Ripple")
        vender = int(input('Qual moeda deseja vender: '))
        if vender == 1:
            moeda = 'bitcoin'
        elif vender == 2:
            moeda = 'ethereum'
        elif vender == 3:
            moeda = 'ripple'
        else:
            print('Opção inválida')
            return
        quantidade = float(input('Quanto gostaria de vender? '))
        cotacao = cripto[moeda]['cotacao']
        taxa = cripto[moeda]['taxa_venda']
        precosemtaxa = quantidade * cotacao
        precocomtaxa = precosemtaxa * (1 - taxa)

        if quantidade > 0:
            if quantidade <= usuarios[cpf]['criptomoedas'][moeda]:
                usuarios[cpf]['criptomoedas'][moeda] -= quantidade
                usuarios[cpf]['brl'] += precocomtaxa
            else:
                print('Saldo insuficiente')
                return
        else:
            print('Quantidade inválida')
            return
        agora = datetime.now()
        transacao = (f"{agora.strftime('%d-%m-%Y %H:%M')} - {precosemtaxa:.2f} {moeda} "
                    f"CT: {cotacao:.2f} TX: {taxa:.2f} REAL: {usuarios[cpf]['brl']:.2f} "
                    f"BTC: {usuarios[cpf]['criptomoedas']['bitcoin']} "
                    f"ETH: {usuarios[cpf]['criptomoedas']['ethereum']} "
                    f"XRP: {usuarios[cpf]['criptomoedas']['ripple']}")
        usuarios[cpf]['extrato'].append(transacao)

        save_usuarios()
    else:
        print('Senha incorreta')
    
def atu_cotacao(cripto):
    for moeda in cripto:
        variacao = random.uniform(-0.05, 0.05)
        nova = cripto[moeda]['cotacao'] * (1 + variacao)
        cripto[moeda]['cotacao'] = nova

    save_cripto()
    print(f"Cotações: \n Bitcoin: {cripto['bitcoin']['cotacao']:.2f}\n Ethereum: {cripto['ethereum']['cotacao']:.2f}\n Ripple: {cripto['ripple']['cotacao']:.2f}")

def menu(usuarios, cripto, cpf):
    while True:
        print('1. Consultar saldo \n 2. Consultar extrato \n 3. Depositar \n 4. Sacar \n 5. Comprar criptomoedas \n 6. Vender criptomoedas \n 7. Atualizar cotação \n 8. Sair')
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
            c_criptomoedas(usuarios, cripto, cpf)
        elif nav == 6:
            v_criptomoedas(usuarios, cripto, cpf)
        elif nav == 7:
            atu_cotacao(cripto)
        elif nav == 8:
            print(f"Até logo,{usuarios[cpf]['nome']}")
            break
        else:
            print('Erro: escolha um número de 1 a 8')

def menuinicial():
    print('1.Cadastrar \n2.Fazer login\n3.Sair')
    while True:
        nav = int(input('Insira o que deseja fazer'))
        if nav == 1:
            cadastrar(usuarios)
        elif nav == 2:
            fazer_login(usuarios, cripto)
        elif nav == 3:
            print('Até a próxima!')
            break
        else:
            print('Opção inválida')


load_usuarios()
load_cripto()

menuinicial()
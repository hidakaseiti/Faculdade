#cadastro da pessoa
cpf = int(input('CPF sem pontos e sem traços: '))
senha = int(input('Digite uma senha com seis dígitos: '))
menu = '1. Consultar saldo /n 2. Consultar extrato /n 3. Depositar /n 4. Sacar /n 5. Comprar criptomoedas /n 6. Vender criptomoedas /n 7. Atualizar cotação /n 8. Sair'

if not cpf or not senha:
    print("Erro: todos os campos são obrigatórios!")
else:
    print("Cadastro realizado com sucesso!")

cpf_login = input('Coloque seu cpf: ')
senha_login = input('Coloque sua senha: ')

if cpf == cpf_login and senha == senha_login:
    print(menu)
else:
    print('CPF ou senha incorretas')
import random

print('Bem Vindo ao Gerador de senhas! ')


caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~´-+!@#$%&*()_^><?/'

numeros = input('Quantas senhas você quer gerar: ')
numeros = int(numeros)

tamanho = input('Insira quantos caracteres você deseja: ')
tamanho = int(tamanho)

print('\nAqui estão as suas senhas: ')

for senha in range(numeros):
    senhas = ''
    for c in range(tamanho):
        senhas += random.choice(caracteres)
    print(senhas)


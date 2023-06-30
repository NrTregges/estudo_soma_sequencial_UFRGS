"""
Programa Soma Sequencial
Descrição: Programa realiza soma de dois números e imprime o resultado.
Autor: Nicholas R. Tregges.
Data: 30/06/2023
Versão: 0.0.1
"""
# Programa Sequencial
## Requisito
#Leia dois números do teclado e calcule a some deles. Apresente o resultado.

# Atribuição de variáveis

numero_1 = 0
numero_2 = 0
soma = 0

# Entrada de dados

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))

# # Processamento de dados

soma = numero_1 + numero_2

# Saída de dados
print(f'O resultado da soma entre {numero_1} e {numero_2} é igual a {soma}.')



# Programa Estruturado

# Atribuição de variáveis

numeros = [0,0]

soma = 0

# Entrada de dados

i = 0

while i < 2:
    numeros[i] = float(input("Digite o número: "))
    i+= 1
    
    
# Processamento de dados - Calculo da soma

for numero in numeros: 
    soma += numero
    
# Saída de dados

print(f'A soma do {numeros[0]} com o número {numeros[1]} é igual a {soma}.')





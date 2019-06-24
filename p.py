
# como abrir e usar o terminal para python?
    #abrir terminal>novo>digitar: python + nomedoarquivo.py > enter

#exercicio 1
# a = int(input("Digite um número"))
# b = int(input("Digite um número"))
# c = int(input("Digite um número"))
# d = int(input("Digite um número"))
# media = (a+b+c+d)/4
# print(media)


#exercicio 2
#vai ter que achar a letra que eu quero na frase que escrevi ( vai usar .count )

# exercicio 3
# fazer programa que receba quantos nº tera no calculo da media e retorne a media deles
# ex: "quantos numeros: 5" ->(n1+n2...+n10)/10
# DICA: pode usar estruturas de repetição... tipo o for...e definir o range
# soma = 0 é porque sempre some o numero anterior
# for i in range para fazer as operações até chegar no final dos numeros, do inicio ao fim
# esse "+= é para somar em cima da soma

quantidade = int(input("Digite aqui suas notas"))
soma = 0 

for i in range(quantidade):
num1 = int(input("Digite aqui suas notas"))
num2 = int(input("Digite aqui suas notas"))

def somar(num1, num2):
     return num1 + num2

def subtrair(num1, num2):
     return num1 - num2

def multiplicar(num1, num2):
     return num1 * num2

def dividir(num1, num2):
     return num1 / num2        
    



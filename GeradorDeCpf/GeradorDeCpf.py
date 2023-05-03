'''
    Gerador de CPFs Aleatórios

    Desenvolvido por Lucas Souza
    Version 1.0
'''

from random import *

regioes= {0:"RS",1:("DF","GO","MS","MT", "TO"),2:("AC","AM","AP","PA","RO","RR"),3:("CE","MA","PI"),4:("AL","PB","PE","RN"),
              5:("BA","SE"),6:"MG",7:("ES","RJ"),8:"SP",9:("PR","SC")}

def exibeNumero(numero):
    print()
    print("CPF GERADO -> %d" % numero)
    print()

def digitoVerificador(numero):
    global cpf
    for _ in range(1,3):
        temp = numero
        soma = 0
        for n in range(2,11):
            ultimo_digito = (temp % 10) * n
            temp = (int)(temp / 10) 
            soma += ultimo_digito

        ultimo_digito = 11 - (soma % 11)
        if ultimo_digito >= 10:
            ultimo_digito = 0

        numero = (numero * 10) + ultimo_digito

    cpf = numero

def Gerador(regiaoEmissora):
    numero = (randint(10000000,99999999) * 10) + regiaoEmissora # Gera 8 dígitos aleatórios somado com o digito do estado emissor
    digitoVerificador(numero)

def regiaoEmissora(uf):
    for key in regioes.keys():
        if uf == key:
            Gerador(key)

def main(option):
    regiaoEmissora(option)
    return cpf
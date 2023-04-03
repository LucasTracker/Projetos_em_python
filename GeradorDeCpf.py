'''
    Gerador de CPFs

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
    for x in range(1,3):
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

    exibeNumero(numero)

def Gerador(regiaoEmissora):
    numero = (randint(10000000,99999999) * 10) + regiaoEmissora # Gera 8 dígitos aleatórios somado com o digito do estado emissor
    digitoVerificador(numero)

def regiaoEmissora(uf):
    flag = False

    for key in regioes.keys():
        if uf == key:
            Gerador(key)
            flag = True
    
    if flag == False:
        print("Região Inválida")
        exit(1)

def main():
    print("#" * 60)
    print("#        GERADOR DE CPFs === Version 1.0                   #")
    print("#" * 60)
    print()
    
    
    for key, value in regioes.items():
        if(type(value) == str):
            print(key, " -> ", value)
        else:
            print(key, " -> ", end=" ")
            for item in range(0,len(value)):
                print(value[item], end=" ")
            print()
    print()
    
    try:
        uf = int(input("Escolha o UF emissor: "))
        regiaoEmissora(uf)
    except ValueError as e:
        print("Por favor digite apenas um número!!!")
        exit(1)

if __name__ == "__main__":
    main()
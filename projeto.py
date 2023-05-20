#Nome: Ithalo Amós Santos Laurentino
#RGM: 33581967

#Definições

def soma (n1, n2):
    resultado = int(n1,2) + int(n2,2)
    return (bin(resultado) [2:]) 

def subtracao (n1, n2):
    resultado = int(n1,2) - int(n2,2)
    return (bin(resultado) [2:])

def multiplicacao (n1, n2):
    resultado = int(n1,2) * int(n2,2)
    return (bin(resultado) [2:])
            

def divisao (n1, n2):
    resultado = int(n1,2) // int(n2,2)
    return (bin(resultado)[2:])

def resto (n1, n2):
    resultado = int(n1,2) % int(n2,2)
    return (bin(resultado)[2:])


print("\t\t ** Calculadora de sistema binário ** \n")

while True:

    try:
        print("-- Menu de Opções --\n")
        print("[+] Soma")
        print("[-] Subtração")
        print("[*] Multiplicação")
        print("[/] Divisão")
        print("[Qualquer outra tecla] = Encerramento\n")

        opcao = input("Digite a operação desejada: ").upper()[0]

        #Menu
            
        if opcao == "+":
            print("\n** Adição **")
            n1 = input("\nDigite um número: ")
            n2 = input("Digite um número: ")
            if n1.isdigit() and n2.isdigit():
                print(f"\n{n1} + {n2} = {soma(n1, n2)}\n")
            
            else:
                print("\nInvalido, você digitou letra,caracter ou letra,caracter + número. ")
                opcao = input("\nDeseja encerrar? (S/N): ").upper()[0]
            
                while opcao != "N" and opcao != "S":
                    print("\n* Opção Invalida *")
                    opcao = input("\nDeseja encerrar? (S/N): ").upper()[0]
                
                if opcao == "S":
                    print("\nObrigado por utilizar.")
                    quit("\n*Encerrando*")
            
        elif opcao == "-":
            print("\n** Subtração **")
            n1 = input("\nDigite um número: ")
            n2 = input("Digite um número: ")
            
            if n1.isdigit() and n2.isdigit():
                print(f"\n{n1} - {n2} = {subtracao(n1, n2)}\n")
            
            else:
                print("\nInvalido, você digitou letra,caracter ou letra,caracter + número. ")
                opcao = input("\nDeseja encerrar? (S/N): ").upper()[0]
            
                while opcao != "N" and opcao != "S":
                    print("\n* Opção Invalida *")
                    opcao = input("\nDeseja encerrar? (S/N): ").upper()[0]
                    
                if opcao == "S":
                    print("\nObrigado por utilizar.")
                    quit("*Encerrando*")

        elif opcao == "*":
            print("\n** Multiplicação **")
            n1 = input("\nDigite um número: ")
            n2 = input("Digite um número: ")
            
            if n1.isdigit() and n2.isdigit():
                print(f"\n{n1} * {n2} = {multiplicacao(n1, n2)}\n")
            
            else:
                print("\nInvalido, você digitou letra,caracter ou letra,caracter + número. ")
                opcao = input("\nDeseja encerrar? (S/N): ").upper()[0]
            
                while opcao != "N" and opcao != "S":
                    print("\n* Opção Invalida *")
                    opcao = input("\nDeseja encerrar? (S/N): ").upper()[0]
                    
                if opcao == "S":
                    print("\nObrigado por utilizar.")
                    quit("*Encerrando*")

        elif opcao == "/":
            print("\n** Divisão **")
            n1 = input("\nDigite um número: ")
            n2 = input("Digite um número: ")
            
            if n1.isdigit() and n2.isdigit():
                print(f"\n{n1} / {n2} = {divisao(n1, n2)} e o resto da divisão é {resto(n1,n2)}\n")
            
            else:
                print("\nInvalido, você digitou letra,caracter ou letra,caracter + número. ")
                opcao = input("\nDeseja encerrar? (S/N): ").upper()[0]
            
                while opcao != "N" and opcao != "S":
                    print("\n* Opção Invalida *")
                    opcao = input("\nDeseja encerrar? (S/N): ").upper()[0]
                
                if opcao == "S":
                    print("\nObrigado por utilizar.")
                    quit("*Encerrando*")
                
        else:
            print("\nVocê digitou uma opção invalida")
            opcao = input("\nDeseja encerrar? (S/N): ").upper()[0]
            
            while opcao != "N" and opcao != "S":
                print("\n* Opção Invalida *")
                opcao = input("\nDeseja encerrar? (S/N): ").upper()[0]

            if opcao == "S":
                print("\nObrigado por utilizar.")
                quit("*Encerrando*")

    except ZeroDivisionError:
        print("\n ** Não existe número divisivel por zero **")
        opcao = input("\nDeseja encerrar? (S/N): ").upper()[0]
        
        while opcao != "N" and opcao != "S":
                print("\n* Opção Invalida *")
                opcao = input("\nDeseja encerrar? (S/N): ").upper()[0]
                
        if opcao == "S":
                print("\nObrigado por utilizar.")
                quit("*Encerrando*")

    except ValueError:
        print("\n ** Você digitou um número fora da base 2 (binária) **")
        opcao = input("\nDeseja encerrar? (S/N): ").upper()[0]
        
        while opcao != "N" and opcao != "S":
                print("\n* Opção Invalida *")
                opcao = input("\nDeseja encerrar? (S/N): ").upper()[0]
            

        if opcao == "S":
                print("\nObrigado por utilizar.")
                quit("*Encerrando*")
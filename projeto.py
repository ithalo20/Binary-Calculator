# Nome: Ithalo Amós Santos Laurentino
# RGM: 33581967

# Deixei algumas anotações para lembrar de algumas coisas.

# Parametro não tem definição, como fosse virgem, não é int, str ou float até dev transformar (Por isso declarei como int)
# "[2:]" É pra contar range a partir do segundo caractér, assim eu tiro 0b
# ",2" após o num(parametro) serve para o que eu digitar ir para base 2
# bin() vai fazer que a operação de o resultado em binário e não em decimal
# unica exceção que consegui pensar já q esta em str, é usar o "in, not in" para mostrar um mensagem de "ERRO" (entre aspas mesmo)

def soma_bin (num1, num2):
    resultado = int(num1,2) + int(num2,2)
    return (bin(resultado) [2:]) 

def sub_bin (num1, num2):
    resultado = int(num1,2) - int(num2,2)
    return (bin(resultado) [2:])

def multi_bin (num1, num2):
    resultado = int(num1,2) * int(num2,2)
    return (bin(resultado) [2:])
            

def div_bin (num1, num2):
    resultado = int(num1,2) // int(num2,2)
    return (bin(resultado)[2:])

def resto_div_bin (num1, num2):
    resultado = int(num1,2) % int(num2,2)
    return (bin(resultado)[2:])

# Código principal

try:

    print("\t\t\t ** Calculadora para sistema binário ** \n")
    print("\n-- Opções para operações matemáticas em sistema binário -- \n")
    print("[1] - Adição")
    print("[2] - Subtração")
    print("[3] - Multiplicação")
    print("[4] - Divisão")
    print("[0] ou [9] - Para sair")

    opcao = int(input("\nDigite a opção desejada: "))

    print("")
    print(20*"---")
    print("")

    if opcao == 1:
        print("[1] - Calculadora de adição em sistema binário ")

        num1 = input("\nDigite os números binarios: ")
        if '1' not in num1 and '0' not in num1:
            print(20*"---")
            print("\n**(ERRO) Digite apenas em base binaria (0 ou 1)**")
            print("**Lembrando que letras, caracteres e espaço em branco, também ocasionará o encerramento da calculadora**")
            quit("\nEncerrando....")

        num2 = input("Digite os números binarios: ")
        if '1' not in num2 and '0' not in num2:
            print("\n**(ERRO) Digite apenas em base binaria (0 ou 1)**")
            print("**Lembrando que letras, caracteres e espaço em branco, também ocasionará o encerramento da calculadora**")
            quit("\nEncerrando....")

        print(f"\n\"{num1}\" + \"{num2}\" é = \"{soma_bin (num1, num2)}\"")
        

    elif opcao == 2:
        print("[2] - Calculadora de subtração em sistema binário ")
        
        num1 = input("\nDigite os números binarios: ")
        if '1' not in num1 and '0' not in num1:
            print(20*"---")
            print("\n**(ERRO) Digite apenas em base binaria (0 ou 1)**")
            print("**Lembrando que letras, caracteres e espaço em branco, também ocasionará o encerramento da calculadora**")
            quit("\nEncerrando....")

        num2 = input("Digite os números binarios: ")
        if '1' not in num2 and '0' not in num2:
            print("\n**(ERRO) Digite apenas em base binaria (0 ou 1)**")
            print("**Lembrando que letras, caracteres e espaço em branco, também ocasionará o encerramento da calculadora**")
            quit("\nEncerrando....")

        print(f"\n\"{num1}\" - \"{num2}\" é = \"{sub_bin (num1, num2)}\"")

    elif opcao == 3:
        print("[3] - Calculadora de multiplicação em sistema binário ")
        
        num1 = input("\nDigite os números binarios: ")
        if '1' not in num1 and '0' not in num1:
            print(20*"---")
            print("\n**(ERRO) Digite apenas em base binaria (0 ou 1)**")
            print("**Lembrando que letras, caracteres e espaço em branco, também ocasionará o encerramento da calculadora**")
            quit("\nEncerrando....")

        num2 = input("Digite os números binarios: ")
        if '1' not in num2 and '0' not in num2:
            print("\n**(ERRO) Digite apenas em base binaria (0 ou 1)**")
            print("**Lembrando que letras, caracteres e espaço em branco, também ocasionará o encerramento da calculadora**")
            quit("\nEncerrando....")
        
        print(f"\n\"{num1}\" x \"{num2}\" é = \"{multi_bin (num1, num2)}\"")

    elif opcao == 4:
        print("[4] - Calculadora de divisão em sistema binário ")
        
        num1 = input("\nDigite os números binarios: ")
        if '1' not in num1 and '0' not in num1:
            print(20*"---")
            print("\n**(ERRO) Digite apenas em base binaria (0 ou 1)**")
            print("**Lembrando que letras, caracteres e espaço em branco, também ocasionará o encerramento da calculadora**")
            quit("\nEncerrando....")

        num2 = input("Digite os números binarios: ")
        if '1' not in num2 and '0' not in num2:
            print("\n**(ERRO) Digite apenas em base binaria (0 ou 1)**")
            print("**Lembrando que letras, caracteres e espaço em branco, também ocasionará o encerramento da calculadora**")
            quit("\nEncerrando....")
        
        print(f"\n\"{num1}\" ÷ \"{num2}\" é = {div_bin (num1, num2)}, e o resto da divisão é {resto_div_bin (num1, num2)}")

    elif opcao == 9:
        print("\n[9] - Você selecionou para fechar o programa ")
        print("\n- Muito obrigado por ter usado a calculadora ;) -")
        quit("\nEncerrando a calculadora....")
    
    elif opcao == 0:
        print("\n[0] - Você selecionou para fechar o programa ")
        print("\n- Muito obrigado por ter usado a calculadora ;) -")
        quit("\nEncerrando a calculadora....")

    else:
        print(f" \n ** Você digitou \"{opcao}\", digite apenas números de \"1\" a \"4\" ou digite \"9\" caso queira sair **")
        

# Código de repetição, copia do código acima e alinha com o "while"

    while opcao:
            
        print("\n\n\t\t\t--------------------- REPETIÇÃO --------------------\n")    
        print("\n\t\t\t** Calculadora para sistema binário ** \n")
        print("\n-- Opções para operações matemáticas em sistema binário -- \n")
        print("[1] - Adição")
        print("[2] - Subtração")
        print("[3] - Multiplicação")
        print("[4] - Divisão")
        print("[0] ou [9] - Para sair")

        opcao = int(input("\nDigite a opção desejada: "))

        print("")
        print(20*"---")
        print("")

    
        if opcao == 1:
            print("\n[1] - Calculadora de adição em sistema binário ")

            num1 = input("\nDigite os números binarios: ")
            if '1' not in num1 and '0' not in num1:
                print(20*"---")
                print("\n**(ERRO) Digite apenas em base binaria (0 ou 1)**")
                print("**Lembrando que letras, caracteres e espaço em branco, também ocasionará o encerramento da calculadora**")
                quit("\nEncerrando....")

            num2 = input("Digite os números binarios: ")
            if '1' not in num2 and '0' not in num2:
                print("\n**(ERRO) Digite apenas em base binaria (0 ou 1)**")
                print("**Lembrando que letras, caracteres e espaço em branco, também ocasionará o encerramento da calculadora**")
                quit("\nEncerrando....")

            print(f"\n\"{num1}\" + \"{num2}\" é = \"{soma_bin (num1, num2)}\"")
            

        elif opcao == 2:
            print("\n[2] - Calculadora de subtração em sistema binário ")
            
            num1 = input("\nDigite os números binarios: ")
            if '1' not in num1 and '0' not in num1:
                print(20*"---")
                print("\n**(ERRO) Digite apenas em base binaria (0 ou 1)**")
                print("**Lembrando que letras, caracteres e espaço em branco, também ocasionará o encerramento da calculadora**")
                quit("\nEncerrando....")

            num2 = input("Digite os números binarios: ")
            if '1' not in num2 and '0' not in num2:
                print("\n**(ERRO) Digite apenas em base binaria (0 ou 1)**")
                print("**Lembrando que letras, caracteres e espaço em branco, também ocasionará o encerramento da calculadora**")
                quit("\nEncerrando....")

            print(f"\n\"{num1}\" - \"{num2}\" é = \"{sub_bin (num1, num2)}\"")

        elif opcao == 3:
            print("\n[3] - Calculadora de multiplicação em sistema binário ")
            
            num1 = input("\nDigite os números binarios: ")
            if '1' not in num1 and '0' not in num1:
                print(20*"---")
                print("\n**(ERRO) Digite apenas em base binaria (0 ou 1)**")
                print("**Lembrando que letras, caracteres e espaço em branco, também ocasionará o encerramento da calculadora**")
                quit("\nEncerrando....")

            num2 = input("Digite os números binarios: ")
            if '1' not in num2 and '0' not in num2:
                print("\n**(ERRO) Digite apenas em base binaria (0 ou 1)**")
                print("**Lembrando que letras, caracteres e espaço em branco, também ocasionará o encerramento da calculadora**")
                quit("\nEncerrando....")
            
            print(f"\n\"{num1}\" x \"{num2}\" é = \"{multi_bin (num1, num2)}\"")

        elif opcao == 4:
            print("\n[4] - Calculadora de divisão em sistema binário ")
            
            num1 = input("\nDigite os números binarios: ")
            if '1' not in num1 and '0' not in num1:
                print(20*"---")
                print("\n**(ERRO) Digite apenas em base binaria (0 ou 1)**")
                print("**Lembrando que letras, caracteres e espaço em branco, também ocasionará o encerramento da calculadora**")
                quit("\nEncerrando....")

            num2 = input("Digite os números binarios: ")
            if '1' not in num2 and '0' not in num2:
                print("\n**(ERRO) Digite apenas em base binaria (0 ou 1)**")
                print("**Lembrando que letras, caracteres e espaço em branco, também ocasionará o encerramento da calculadora**")
                quit("\nEncerrando....")
            
            print(f"\n\"{num1}\" ÷ \"{num2}\" é = {div_bin (num1, num2)}, e o resto da divisão é {resto_div_bin (num1, num2)}")

        elif opcao == 9:
            print("\n[9] - Você selecionou para fechar o programa ")
            print("\n- Muito obrigado por ter usado a calculadora ;) -")
            quit("\nEncerrando a calculadora....")
        
        elif opcao == 0:
            print("\n[0] - Você selecionou para fechar o programa ")
            print("\n- Muito obrigado por ter usado a calculadora ;) -")
            quit("\nEncerrando a calculadora....")
        
        else:
            print(f"\n ** Você digitou \"{opcao}\", digite apenas números de \"1\" a \"4\" ou digite \"9\" caso queira sair **")

except ZeroDivisionError:
    print("")
    print(20*"---")
    print("")
    print("*Zero ÷ Zero = 0 (Não é dívisivel)*")
    print("\nEncerrando programa, abra novamente...")

except ValueError:
        print("\n** (ERRO) Digite apenas números ** \n** Letras, caracteres ou espaço em branco ocasionara encerramento da calculadora **")
        print("\nEncerrando programa, abra novamente...")
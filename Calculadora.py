import math

def mostrar_menu():
    print("\n" + "="*40)
    print("Calculadora Científica".center(40))
    print("="*40)
    print("Operações básicas:")
    print(" 1: Soma (+)")
    print(" 2: Subtração (-)")
    print(" 3: Multiplicação (*)")
    print(" 4: Divisão (/)")
    print("\nOperações científicas:")
    print(" 5: Potência (x^y)")
    print(" 6: Raiz Quadrada (√x)")
    print(" 7: Logaritmo Natural (ln(x))")
    print(" 8: Logaritmo Base 10 (log10(x))")
    print(" 9: Seno (sin(x) em radianos)")
    print("10: Cosseno (cos(x) em radianos)")
    print("11: Tangente (tan(x) em radianos)")
    print("12: Fatorial (x!)")
    print("\n13: Converter graus para radianos")
    print("14: Converter radianos para graus")
    print("\n 0: Sair")
    print("="*40)

def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido! Digite um número.")

def obter_numero_positivo(mensagem):
    while True:
        num = obter_numero(mensagem)
        if num >= 0:
            return num
        print("O número deve ser positivo!")

def obter_numero_positivo_nao_zero(mensagem):
    while True:
        num = obter_numero(mensagem)
        if num > 0:
            return num
        print("O número deve ser maior que zero!")

def obter_inteiro_nao_negativo(mensagem):
    while True:
        num = obter_numero(mensagem)
        if num >= 0 and num.is_integer():
            return int(num)
        print("O número deve ser um inteiro não negativo!")

def calcular():
    while True:
        mostrar_menu()
        opcao = input("\nDigite o número da operação: ")

        if opcao == '0':
            print("Saindo da calculadora...")
            break

        # Operações com um único número
        if opcao in {'6', '7', '8', '9', '10', '11', '12', '13', '14'}:
            if opcao in {'6', '7', '8', '9', '10', '11', '12'}:
                num = obter_numero("Digite o número: ")
            
            if opcao == '6':  # Raiz quadrada
                if num < 0:
                    print("Erro: Não existe raiz real de número negativo!")
                else:
                    print(f"√{num} = {math.sqrt(num)}")
            
            elif opcao == '7':  # Log natural
                if num <= 0:
                    print("Erro: Logaritmo indefinido para números ≤ 0!")
                else:
                    print(f"ln({num}) = {math.log(num)}")
            
            elif opcao == '8':  # Log base 10
                if num <= 0:
                    print("Erro: Logaritmo indefinido para números ≤ 0!")
                else:
                    print(f"log10({num}) = {math.log10(num)}")
            
            elif opcao == '9':  # Seno
                print(f"sin({num}) = {math.sin(num)}")
            
            elif opcao == '10':  # Cosseno
                print(f"cos({num}) = {math.cos(num)}")
            
            elif opcao == '11':  # Tangente
                print(f"tan({num}) = {math.tan(num)}")
            
            elif opcao == '12':  # Fatorial
                if num < 0 or not num.is_integer():
                    print("Erro: Fatorial definido apenas para inteiros não negativos!")
                else:
                    print(f"{int(num)}! = {math.factorial(int(num))}")
            
            elif opcao == '13':  # Graus para radianos
                graus = obter_numero("Digite o valor em graus: ")
                radianos = math.radians(graus)
                print(f"{graus}° = {radianos} radianos")
            
            elif opcao == '14':  # Radianos para graus
                radianos = obter_numero("Digite o valor em radianos: ")
                graus = math.degrees(radianos)
                print(f"{radianos} radianos = {graus}°")

        # Operações com dois números
        elif opcao in {'1', '2', '3', '4', '5'}:
            num1 = obter_numero("Digite o primeiro número: ")
            num2 = obter_numero("Digite o segundo número: ")
            
            if opcao == '1':  # Soma
                print(f"{num1} + {num2} = {num1 + num2}")
            
            elif opcao == '2':  # Subtração
                print(f"{num1} - {num2} = {num1 - num2}")
            
            elif opcao == '3':  # Multiplicação
                print(f"{num1} * {num2} = {num1 * num2}")
            
            elif opcao == '4':  # Divisão
                if num2 == 0:
                    print("Erro: Divisão por zero!")
                else:
                    print(f"{num1} / {num2} = {num1 / num2}")
            
            elif opcao == '5':  # Potência
                print(f"{num1}^{num2} = {math.pow(num1, num2)}")
        
        else:
            print("Opção inválida! Tente novamente.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    calcular()

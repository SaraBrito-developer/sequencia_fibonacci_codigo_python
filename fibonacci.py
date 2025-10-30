# -*- coding: utf-8 -*-

def encontrar_sequencia_fibonacci(n):
    """
    Recebe um número 'n' (int) e retorna uma lista 
    com os 'n' primeiros números da sequência Fibonacci.
    """
    
    lista_fib = []
    contagem = 0
    num1, num2 = 0, 1

    while contagem < n:
        lista_fib.append(num1)
        soma = num1 + num2
        num1 = num2
        num2 = soma
        contagem += 1
        
    return lista_fib

def rodar_programa_principal():
    """
    Função principal para lidar com a entrada do usuário e imprimir.
    """
    
    while True:
        try:
            sequencia_str = input("Quantos números Fibonacci você deseja? ")
            sequencia = int(sequencia_str)
            
            if sequencia <= 0:
                print("Erro: Você precisa digitar um número maior que 0.\n")
                continue 
            else:
                break 

        except ValueError:
            print(f"Erro: '{sequencia_str}' não é um número válido. Tente novamente.\n")

    resultado_fib = encontrar_sequencia_fibonacci(sequencia)

    if sequencia == 1:
        print("\nO 1º número da sequência Fibonacci é:")
        print(resultado_fib[0])
    else:
        print(f"\nOs {sequencia} primeiros números da sequência Fibonacci são:")
        for numero in resultado_fib:
            print(numero, end=" ")
        print() 

if __name__ == "__main__":
    rodar_programa_principal()

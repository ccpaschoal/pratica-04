# -*- coding: utf-8 -*-
def calculadora():
    """Realiza operações básicas (+, -, *, /) entre dois números com tratamento de erros."""
    print("--- Calculadora Básica Python ---")
    while True:
        try:
            # Solicita o primeiro número e tenta convertê-lo para float
            num1_str = input("Digite o primeiro número: ")
            num1 = float(num1_str)

            # Solicita a operação e verifica se é válida
            op = input("Digite a operação (+, -, *, /): ")
            if op not in ['+', '-', '*', '/']:
                print("\nErro: Operação inválida. Use +, -, * ou /. Tente novamente.\n")
                continue  # Volta ao início do loop

            # Solicita o segundo número e tenta convertê-lo para float
            num2_str = input("Digite o segundo número: ")
            num2 = float(num2_str)

            # Realiza a operação
            resultado = 0
            if op == '+':
                resultado = num1 + num2
            elif op == '-':
                resultado = num1 - num2
            elif op == '*':
                resultado = num1 * num2
            elif op == '/':
                # Verifica divisão por zero
                if num2 == 0:
                    print("\nErro: Divisão por zero não é permitida. Tente novamente.\n")
                    continue # Volta ao início do loop
                resultado = num1 / num2

            # Exibe o resultado e encerra
            print(f"\nResultado: {num1} {op} {num2} = {resultado}")
            print("---------------------------------")
            break # Sai do loop while

        except ValueError:
            # Erro se a entrada não puder ser convertida para número
            print("\nErro: Entrada inválida. Por favor, insira apenas números. Tente novamente.\n")
        except Exception as e:
            # Captura outros erros inesperados
            print(f"\nOcorreu um erro inesperado: {e}. Tente novamente.\n")

if __name__ == "__main__":
    calculadora() # Executa a calculadora quando o script é rodado diretamente
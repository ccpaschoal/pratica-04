# -*- coding: utf-8 -*-
def contador_par_impar():
    "Conta a quantidade de números pares e ímpares inseridos pelo usuário."
    cont_par = 0
    cont_impar = 0
    print("--- Contador de Pares e Ímpares ---")
    print("Digite números inteiros. Digite 'fim' para ver o resultado.")

    while True:
        entrada = input("Digite um número inteiro ou 'fim': ")

        if entrada.lower() == 'fim':
            break # Sai do loop se o usuário digitar 'fim'

        try:
            # Tenta converter a entrada para inteiro
            numero = int(entrada)

            # Verifica se é par ou ímpar
            if numero % 2 == 0:
                cont_par += 1
                print(f"-> {numero} é par.")
            else:
                cont_impar += 1
                print(f"-> {numero} é ímpar.")
        except ValueError:
            # Informa sobre entrada inválida (não inteiro e não 'fim')
            print("-> Erro: Entrada inválida. Por favor, insira um número inteiro ou 'fim'.")

    # Exibe a contagem final
    print("\n--- Contagem Final ---")
    print(f"Quantidade de números pares inseridos: {cont_par}")
    print(f"Quantidade de números ímpares inseridos: {cont_impar}")
    print("------------------------")

if __name__ == "__main__":
    contador_par_impar()
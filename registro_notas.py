# -*- coding: utf-8 -*-
def registro_notas():
    """Registra notas válidas (0-10) e calcula a média da turma."""
    notas_validas = []
    print("--- Registro de Notas e Média da Turma ---")
    print("Digite as notas dos alunos (0 a 10). Digite 'fim' para calcular a média.")

    while True:
        entrada = input("Digite uma nota ou 'fim': ")

        if entrada.lower() == 'fim':
            break # Sai do loop se o usuário digitar 'fim'

        try:
            # Tenta converter a entrada para float
            nota = float(entrada)

            # Verifica se a nota está no intervalo válido
            if 0 <= nota <= 10:
                notas_validas.append(nota)
                print(f"-> Nota {nota} adicionada.")
            else:
                # Informa sobre nota fora do intervalo
                print("-> Nota inválida. A nota deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            # Informa sobre entrada não numérica (e não 'fim')
            print("-> Entrada inválida. Por favor, digite um número entre 0 e 10 ou 'fim'.")

    # Calcula e exibe a média se houver notas válidas
    if notas_validas:
        media = sum(notas_validas) / len(notas_validas)
        print(f"\n--- Resultados ---")
        print(f"Total de notas válidas inseridas: {len(notas_validas)}")
        # print(f"Notas: {notas_validas}") # Opcional: mostrar todas as notas
        print(f"Média da turma: {media:.2f}")
        print("--------------------")
    else:
        print("\nNenhuma nota válida foi inserida para calcular a média.")
        print("--------------------")

if __name__ == "__main__":
    registro_notas()
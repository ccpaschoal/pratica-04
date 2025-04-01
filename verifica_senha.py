# -*- coding: utf-8 -*-
def verifica_senha_forte():
    """Verifica se uma senha atende aos critérios de força (>=8 chars, >=1 número)."""
    print("--- Verificador de Senha Forte ---")
    print("Critérios: Mínimo 8 caracteres e pelo menos 1 número.")
    print("Digite 'sair' para terminar.")

    while True:
        senha = input("\nDigite a senha: ")

        if senha.lower() == 'sair':
            print("\nEncerrando o verificador.")
            print("-----------------------------")
            break # Sai do loop se o usuário digitar 'sair'

        # Verifica os critérios
        tem_comprimento_minimo = len(senha) >= 8
        tem_numero = any(char.isdigit() for char in senha) # Verifica se há algum dígito

        if tem_comprimento_minimo and tem_numero:
            print("-> Senha forte aceita!")
            print("-----------------------------")
            break # Sai do loop pois a senha é válida
        else:
            # Informa quais critérios não foram atendidos
            print("-> Senha fraca. Critérios não atendidos:")
            if not tem_comprimento_minimo:
                print("  - A senha deve ter pelo menos 8 caracteres.")
            if not tem_numero:
                print("  - A senha deve conter pelo menos um número.")
            print("Tente novamente ou digite 'sair'.")

if __name__ == "__main__":
    verifica_senha_forte()
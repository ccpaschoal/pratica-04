# Exercícios Básicos de Python

Este repositório contém soluções para alguns exercícios que envolvem tratamento de erros e entrada de dados, utilizando estruturas de repetição e condicionais em Python.

## Scripts Incluídos

1. **`calculadora.py`**:  
   Desenvolve uma calculadora que realiza as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números.  
   - Solicita ao usuário que insira dois números e uma operação.
   - As operações válidas são: `+` (adição), `-` (subtração), `*` (multiplicação) e `/` (divisão).
   - Continua solicitando entradas até que uma operação válida seja concluída.
   - Trata erros como entrada inválida (não numérica), divisão por zero e operação inválida utilizando `try/except`.
   - Após uma operação concluída com sucesso, exibe o resultado e encerra o programa.

2. **`registro_notas.py`**:  
   Permite que um professor registre as notas de uma turma.  
   - Continua solicitando as notas até que o professor digite `fim`.
   - Aceita apenas notas válidas entre 0 e 10, ignorando as inválidas.
   - Ao final, calcula e exibe a média da turma.

3. **`verifica_senha.py`**:  
   Verifica se uma senha é forte.  
   - Uma senha forte deve ter pelo menos 8 caracteres e conter ao menos um número.
   - O programa continua pedindo senhas até que uma senha válida seja inserida ou o usuário digite `sair`.

4. **`contador_par_impar.py`**:  
   Solicita ao usuário que insira números inteiros.  
   - Continua solicitando números até que o usuário digite `fim`.
   - Para cada entrada inválida (quando não for possível converter para inteiro), informa o erro e continua.
   - Ao final, exibe a quantidade de números pares e ímpares inseridos.

## Como Executar

Para executar qualquer um dos scripts, abra seu terminal, navegue até o diretório onde os scripts foram salvos e utilize o comando `python`:

```bash
python calculadora.py
python registro_notas.py
python verifica_senha.py
python contador_par_impar.py

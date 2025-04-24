# Kaggle Tutorial

# For and While Loops


| Estrutura                     | Descrição                                                                 | Exemplo                                                                 |
|------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `for item in iterable:`      | Itera sobre cada item de um iterável (lista, tupla, string, etc).         | `for i in range(5): print(i)`                                          |
| `while condição:`            | Executa o bloco enquanto a condição for verdadeira.                       | `while x < 10: x += 1`                                                 |
| `break`                      | Encerra o loop imediatamente.                                             | `for i in range(10): if i == 5: break`                                 |
| `continue`                   | Pula para a próxima iteração do loop.                                     | `for i in range(5): if i == 2: continue`                               |
| `else` (em loops)            | Executa um bloco se o loop terminar sem `break`.                          | `for i in range(3): ... else: print("Fim do loop")`                    |
| List Comprehension           | Cria listas de forma concisa e elegante.                                  | `[x**2 for x in range(5)]`                                             |
| List Comprehension com cond. | Com filtro condicional.                                                   | `[x for x in range(10) if x % 2 == 0]`                                 |
| Nested List Comprehension    | Compreensões aninhadas (listas de listas, por exemplo).                   | `[[i*j for j in range(3)] for i in range(3)]`                          |

Explicando os termos:

| Termo / Símbolo           | Tipo                  | Descrição                                                                 |
|---------------------------|-----------------------|---------------------------------------------------------------------------|
| `for`                     | Palavra-chave         | Inicia um loop que itera sobre elementos de uma sequência (lista, etc.). |
| `i`, `x`, `item`, etc.    | Variável              | Variável de controle que recebe cada valor da sequência durante o loop.  |
| `in`                      | Palavra-chave         | Indica que se está iterando **dentro de** uma sequência ou iterável.     |
| `range(n)`                | Função embutida       | Gera uma sequência de números de `0` até `n-1`.                           |
| `while`                   | Palavra-chave         | Inicia um loop que continua **enquanto** a condição for verdadeira.      |
| `break`                   | Palavra-chave         | Interrompe o loop imediatamente.                                         |
| `continue`                | Palavra-chave         | Pula a iteração atual e vai para a próxima.                              |
| `else` (com loops)        | Palavra-chave         | Executa se o loop terminar **sem** `break`.                              |
| `x**2`, `x % 2`, etc.     | Expressões            | Usadas para transformar ou filtrar dados nas list comprehensions.        |
| `[expr for x in iter]`    | List comprehension     | Cria uma nova lista com base em uma expressão aplicada a cada item.      |
| `if condição`             | Condicional            | Filtra os elementos em uma list comprehension.                           |
| `[[... for ...] for ...]` | List comprehension aninhada | Cria listas dentro de listas, como matrizes.                          |

# String syntax
Essas são as definições para strings 

| O que você digita... | O que você obtém | Exemplo                        | Resultado do `print(exemplo)`       | Explicação                                                                 |
|----------------------|------------------|--------------------------------|--------------------------------------|-----------------------------------------------------------------------------|
| `\'`                 | `'`              | `'What\'s up?'`               | What's up?                           | Permite inserir uma aspa simples dentro de uma string delimitada por aspas simples. |
| `\"`                 | `"`              | `"That's \"cool\""`           | That's "cool"                        | Permite inserir aspas duplas dentro de uma string delimitada por aspas duplas.       |
| `\\`                 | `\`              | `"Look, a mountain: /\\"`     | Look, a mountain: /\                | Exibe uma barra invertida (`\`), que normalmente é usada como caractere de escape.   |
| `\n`                 | (nova linha)     | `"1\n2 3"`                     | 1<br>2 3                             | Insere uma quebra de linha, dividindo o texto em duas linhas.                        |



# Import syntax



Definiçoes para importar bibliotecas
| Sintaxe                              | Descrição                                                                    | Exemplo                          |
|-------------------------------------|-------------------------------------------------------------------------------|----------------------------------|
| `import módulo`                     | Importa o módulo completo.                                                   | `import math`                    |
| `import módulo as alias`            | Importa o módulo com um nome alternativo.                                    | `import numpy as np`            |
| `from módulo import objeto`         | Importa um objeto específico (função, classe, variável) do módulo.           | `from math import sqrt`         |
| `from módulo import objeto as alias`| Importa um objeto específico com um nome alternativo.                        | `from math import sqrt as raiz` |
| `from módulo import *`              | Importa todos os objetos do módulo (não recomendado, pode causar conflitos). | `from math import *`            |

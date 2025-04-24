# Kaggle Tutorial


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

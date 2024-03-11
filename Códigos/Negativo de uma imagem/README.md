# Códigos Relativos a Negativo de uma Imagem para PMG

## Descrição

O negativo de uma imagem é uma operação que inverte as cores de uma imagem. Onde
a cor preta se torna branca, a cor branca se torna preta e as outras cores se tornam
seus complementos. O negativo de uma imagem é obtido subtraindo-se cada pixel
de uma imagem de um valor fixo, que é o valor máximo que um pixel pode ter. Para
uma imagem de 8 bits, o valor máximo é 255. Portanto, o negativo de uma imagem
de 8 bits é obtido subtraindo-se cada pixel de 255.

## Códigos


Os códigos foram subdivididos em 3 partes:

1. **main.py**: Esse arquivo é responsável pela execução geral das funções, nele está
sendo chamado a função `menu` que é responsável por exibir as opções de
funcionalidades do programa.
2. **imagens.py**: Esse arquivo contém duas constantes: `FOTO_PNG` e `FOTO_PGM`.
Altere o valor dessas constantes para novas imagens.
3. **functions.py**: Esse arquivo contém as funções que realizam as operações
sobre as imagens.

## Execução

Para executar o programa, basta executar o arquivo `main.py` e seguir as
instruções exibidas no terminal.

## Licença

Esse código é livre para ser usado dentro dos termos da licença MIT.

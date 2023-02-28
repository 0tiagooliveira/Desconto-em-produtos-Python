# Phyton
Desconto em produtos
Este programa Python calcula o valor de um produto após aplicar um desconto de 5%.

Como executar o código
Certifique-se de que você tenha o Python 3 instalado em seu computador. Caso contrário, você pode baixá-lo aqui.

Faça o download do arquivo desconto.py deste repositório.

Abra um terminal ou prompt de comando e navegue até a pasta onde você salvou o arquivo desconto.py.

Digite o seguinte comando para executar o código:

python desconto.py
Digite o preço do produto quando solicitado pelo programa e pressione Enter.

O programa calculará o preço final do produto com o desconto aplicado e exibirá a mensagem no seguinte formato:

O produto que custava R$ <preco_original> na promoção de desconto vai custar R$ <preco_final>
Substitua <preco_original> e <preco_final> pelos valores correspondentes calculados pelo programa.

Agora você pode executar o programa Python e ver o resultado do cálculo do desconto em um produto.


Agora vou explicar cada linha do código em detalhes:

produto = float(input('Qual o preço de um produto?: R$ '))

Nesta linha, o código está pedindo ao usuário que digite o preço de um produto como um valor em ponto flutuante (float), usando a função input(). O valor digitado é então armazenado na variável produto.

promocao = produto * 5 / 100
Nesta linha, o código está calculando o valor do desconto. Ele multiplica o preço original do produto (armazenado em produto) por 5% (dividindo por 100), e armazena o resultado na variável promocao.

valorfinal = produto - promocao
Nesta linha, o código está calculando o preço final do produto após o desconto ser aplicado. Ele subtrai o valor do desconto (armazenado em promocao) do preço original do produto (armazenado em produto), e armazena o resultado na variável valorfinal.

print('O produto que custava R$ {} na promoção de desconto vai custar R$ {:.2f}'.format( produto, valorfinal))
Nesta linha, o código está exibindo o resultado do cálculo para o usuário. Ele usa a função print() para exibir uma mensagem na tela que inclui o preço original do produto (formatado como um valor em reais usando a sintaxe {}), e o preço final após o desconto ser aplicado (também formatado como um valor em reais com duas casas decimais usando a sintaxe {:.2f}). A função format() é usada para substituir os valores dos argumentos produto e valorfinal nas posições apropriadas na mensagem.

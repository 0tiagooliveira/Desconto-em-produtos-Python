produto = float(input('Qual o preço de um produto?: R$ '))
promocao = produto * 5 / 100
valorfinal = produto - promocao
print('O produto que custava R$ {} na promoção de desconto vai custar R$ {:.2f}'.format( produto, valorfinal))

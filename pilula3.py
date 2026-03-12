import datetime
#entrada
data_compra = input('Digite a data da compra d/m/y: ')
meses = int(input('Prazo de garantia: '))
#processamento
data_inicial = datetime.datetime.strptime(data_compra, '%d/%m/%y')
data_final = data_inicial + datetime.timedelta(days=meses * 30)
#saida
print(f"Garantian Válida até{data_final.strftime('%d/%m/%y')}")
print(f'Dia da semana:{data_final.strftime('%A')}')

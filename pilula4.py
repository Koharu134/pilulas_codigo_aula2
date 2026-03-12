import statistics as st
#entradas
lote1 = int(input('Produção lote1: '))
lote2 = int(input('Produção lote2: '))
lote3 = int(input('Produção lote3: '))
#processamento
media = st.mean((lote1,lote2,lote3))
desvio = st.stdev((lote1,lote2,lote3))
#saida
print(f'Média: {media:.2f}')
print(f'Desvio padrão: {desvio:.2f}')

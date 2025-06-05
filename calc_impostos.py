print("---------------------------------------")
print("Calculadora de Impostos Retidos - NFS-e")
print("---------------------------------------")

valor = input('\nDigite um valor em R$: ')
valor = valor.replace('.', '').replace(',', '.').strip()
valor_corrigido = float(valor)

if valor_corrigido < 216:
    valor_liquido = valor_corrigido

pis = (valor_corrigido * 0.65) / 100
pis_arredondado = round(pis, 2)

cofins = (valor_corrigido * 3) / 100
cofins_arredondado = round(cofins, 2)

ir = (valor_corrigido * 1.5) / 100
ir_arredondado = round(ir, 2)

if ir < 10:
    ir_arredondado = 0
else:
    ir_arredondado = round(ir, 2)

csll = (valor_corrigido * 1) / 100
csll_arredondado = round(csll, 2)

fed = (valor_corrigido * 3.65) / 100
fed_arredondado = round(fed, 2)

mun = (valor_corrigido * 2) / 100
mun_arredondado = round(mun, 2)

com_ir = 6.15
sem_ir = 4.65

if ir_arredondado < 10:
    valor_liquido = valor_corrigido - (valor_corrigido * sem_ir) / 100
elif ir_arredondado > 9.99:
    valor_liquido = valor_corrigido - (valor_corrigido * com_ir) / 100
valor_liquido_arredondado = round(valor_liquido, 2)

print('\nPIS = R$', pis_arredondado)
print('COFINS = R$', cofins_arredondado)
print('IRRF = R$', ir_arredondado)
print('CSLL = R$', csll_arredondado)
print('FEDERAIS = R$', fed_arredondado)
print('MUNICIPAIS = R$', mun_arredondado)
print('\nVALOR LÍQUIDO = R$', valor_liquido_arredondado)

input('\nPressione Enter para sair...')

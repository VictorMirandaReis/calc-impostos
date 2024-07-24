print("---------------------------------------")
print("Calculadora de Impostos Retidos - NFS-e")
print("---------------------------------------")

valor = input('\nDigite um valor em R$: ')
valor_corrigido = float(valor.replace(',', '.'))

pis = (valor_corrigido * 0.65) / 100
pis_arredondado = round(pis, 2)

cofins = (valor_corrigido * 3) / 100
cofins_arredondado = round(cofins, 2)

ir = (valor_corrigido * 1.5) / 100
ir_arredondado = round(ir, 2)

inss = (valor_corrigido * 11) / 100
inss_arredondado = round(inss, 2)

csll = (valor_corrigido * 1.5) / 100
csll_arredondado = round(csll, 2)

print('PIS = R$', pis_arredondado)
print('COFINS = R$', cofins_arredondado)
print('IRRF = R$', ir_arredondado)
print('INSS = R$', inss_arredondado)
print('CSLL = R$', csll_arredondado)
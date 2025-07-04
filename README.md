# Calculadora de Impostos Retidos - NFS-e

Este projeto é uma calculadora simples para simular o cálculo de impostos retidos em Notas Fiscais de Serviço Eletrônicas (NFS-e), desenvolvida em Python.

## Como usar

1. Execute o script `calc_impostos.py`:

   ```sh
   python calc_impostos.py
   ```
2. Digite o valor bruto em R$ quando solicitado.
3. O programa exibirá os valores de PIS, COFINS, IRRF, CSLL, FEDERAIS, MUNICIPAIS e o valor líquido.

## Cálculos dos impostos

- **PIS:** 0,65%
- **COFINS:** 3%
- **IRRF:** 1,5% (isento para valores inferiores a R$ 10,00)
- **CSLL:** 1%
- **FEDERAIS:** 3,65%
- **MUNICIPAIS:** 2% (Verificar serviço/CNAE)
- **Valor Líquido:** 
  - Se IRRF < R$ 10,00: desconta 4,65%
  - Se IRRF ≥ R$ 10,00: desconta 6,15%

## Estrutura do projeto

- `calc_impostos.py`: Script principal da calculadora.
- `build/`: Pasta gerada por ferramentas de empacotamento (ex: PyInstaller).

## Requisitos

- Python 3.x

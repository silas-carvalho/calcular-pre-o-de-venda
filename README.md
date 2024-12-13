# calcular_preco_venda_v1

O projeto "calcular_preco_venda_v1" está em desenvolvimento com o objetivo de calcular o preço de venda com base nos custos e nas margens de lucro. Para utilizá-lo, é imprescindível que o usuário tenha os custos previamente definidos, permitindo que a aplicação determine automaticamente o preço de venda.

## Pré-requisitos

Certifique-se de que você tem o Python 3.x instalado em seu sistema. O Python 3.x pode ser encontrado na Microsoft Store.

## Instalar dependências

Windows Power Shell
```bash
pip install colorama
```

Linux ou MacOs
```bash
sudo pip install colorama
```

## Cálculos realizados pelo programa; exemplo

```bash
Custo: R$19.37
Preço de Venda Total (PV): R$43.04
----------------------------------------
Lucro Bruto (LB): R$23.67
Margem Percentual (M%): 55.00%
----------------------------------------
Preço de Venda por Produto: R$2.15
Comissão do Vendedor por Produto: R$0.11
Comissão Total do Vendedor: R$2.20
Comissão Total para 1 Vendedores: R$2.20
----------------------------------------
Pró-labore Total: R$11.84
Pró-labore Sócio 1: R$2.37
Pró-labore Sócio 2: R$2.37
Pró-labore Sócio 3: R$2.37
Pró-labore Sócio 4: R$2.37
Pró-labore Sócio 5: R$2.37
Lucro Líquido: R$11.83
```

## Fórmulas Utilizadas nos Cálculos Financeiros

Custo dos Produtos Vendidos (CMV):
```bash
CMV=19,37
```
Preço de Venda (PV):
```bash
PV = CMV / (1 - 0,55) = 19,37 / 0,45 ≈ 43,04
```
Lucro Bruto (LB):
```bash
LB = PV - CMV = 43,04 - 19,37 = 23,67
```

Margem Percentual (M%):
```bash
M% = (LB / PV) * 100 = (23,67 / 43,04) * 100 ≈ 55%
```

Preço de Venda por Produto (PV por unidade):
```bash
PV por unidade = PV / 20 = 43,04 / 20 ≈ 2,15
```

Comissão do Vendedor por Produto:
```bash
Comissão por unidade = PV por unidade * 0,05 = 2,15 * 0,05 = 0,1075 ≈ 0,11
```

Comissão Total do Vendedor:
```bash
Comissão total = Comissão por unidade * 20 = 0,11 * 20 = 2,20
```

Pró-labore:
```bash
Pró-labore total = LB * 0,5 = 23,67 * 0,5 = 11,835 ≈ 11,84
Pró-labore por sócio = Pró-labore total / 5 = 11,84 / 5 = 2,368 ≈ 2,37
```

Lucro Líquido (LL):
```bash
LL = LB - Pró-labore total = 23,67 - 11,84 = 11,83
```















# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:01:26 2024

@author: Silas Carvalho

This code is released under the MIT License.

Copyright (c) 2024 Silas Carvalho

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
from colorama import Fore, Style, init
from decimal import Decimal, getcontext, ROUND_HALF_UP

# Inicializa o colorama
init(autoreset=True)

# Define a precisão dos cálculos
getcontext().prec = 10

def round_decimal(value):
    return value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def calcular_preco_venda():
    while True:
        try:
            print(Fore.LIGHTGREEN_EX + "=" * 40)
            print(Fore.LIGHTWHITE_EX + " CÁLCULO DE PREÇO DE VENDA E LUCROS ".center(40))
            print(Fore.LIGHTGREEN_EX + "=" * 40)
            
            custo = Decimal(input(Fore.LIGHTYELLOW_EX + "Digite o custo total dos produtos (em R$): ").replace(',', '.'))
            margem_lucro = Decimal(input(Fore.LIGHTYELLOW_EX + "Digite a margem de lucro desejada (em %): ").replace(',', '.')) / 100
            quantidade_produtos = int(input(Fore.LIGHTYELLOW_EX + "Digite a quantidade de produtos: "))
            num_vendedores = int(input(Fore.LIGHTYELLOW_EX + "Digite o número de vendedores: "))
            comissao_vendedor = Decimal(input(Fore.LIGHTYELLOW_EX + "Digite a comissão de cada vendedor (em %): ").replace(',', '.')) / 100

            margem_total = margem_lucro + comissao_vendedor

            if margem_total <= 0:
                print(Fore.LIGHTRED_EX + "Erro: A margem total (lucro + comissão) deve ser maior que 0%.")
                continue

            incluir_pro_labore = input(Fore.LIGHTYELLOW_EX + "Deseja incluir pró-labore no cálculo? (s/n): ").strip().lower() == 's'
            porcentagem_socios = []

            if incluir_pro_labore:
                num_socios = int(input(Fore.LIGHTYELLOW_EX + "Digite o número de sócios: "))
                for i in range(num_socios):
                    porcentagem = Decimal(input(Fore.LIGHTYELLOW_EX + f"Porcentagem do pró-labore para o sócio {i + 1} (%): ").replace(',', '.')) / 100
                    porcentagem_socios.append(porcentagem)
                if sum(porcentagem_socios) != Decimal('1'):
                    print(Fore.LIGHTRED_EX + "Erro: A soma das porcentagens dos sócios deve ser 100%.")
                    continue

            print(Fore.LIGHTYELLOW_EX + "\nEscolha o tipo de desconto no preço de venda:")
            print(Fore.LIGHTYELLOW_EX + "[1] Por unidade")
            print(Fore.LIGHTYELLOW_EX + "[2] Total")
            print(Fore.LIGHTYELLOW_EX + "[3] Sem desconto")
            tipo_desconto = input(Fore.LIGHTYELLOW_EX + "Opção: ").strip()

            desconto_total = Decimal('0')
            if tipo_desconto == '1':
                print(Fore.LIGHTYELLOW_EX + "\nEscolha o tipo de desconto por unidade:")
                print(Fore.LIGHTYELLOW_EX + "[1] R$")
                print(Fore.LIGHTYELLOW_EX + "[2] %")
                tipo_unidade = input(Fore.LIGHTYELLOW_EX + "Opção: ").strip()
                valor = Decimal(input(Fore.LIGHTYELLOW_EX + "Valor do desconto por unidade: ").replace(',', '.'))
                desconto_total = (valor / 100 * custo / quantidade_produtos) if tipo_unidade == '2' else valor

            elif tipo_desconto == '2':
                print(Fore.LIGHTYELLOW_EX + "\nEscolha o tipo de desconto total:")
                print(Fore.LIGHTYELLOW_EX + "[1] R$")
                print(Fore.LIGHTYELLOW_EX + "[2] %")
                tipo_total = input(Fore.LIGHTYELLOW_EX + "Opção: ").strip()
                valor = Decimal(input(Fore.LIGHTYELLOW_EX + "Valor do desconto total: ").replace(',', '.'))
                desconto_total = (valor / 100 * custo) if tipo_total == '2' else valor

            if margem_total >= Decimal('1'):
                pv = round_decimal(custo * (1 + margem_total))
            else:
                pv = round_decimal(custo / (1 - margem_total))

            if tipo_desconto == '1':
                pv_unitario = round_decimal(pv / quantidade_produtos) - desconto_total
                pv_total = round_decimal(pv_unitario * quantidade_produtos)
            elif tipo_desconto == '2':
                pv_total = round_decimal(pv - desconto_total)
                pv_unitario = round_decimal(pv_total / quantidade_produtos)
            else:
                pv_total = pv
                pv_unitario = round_decimal(pv_total / quantidade_produtos)

            lucro_bruto = round_decimal(pv_total - custo)
            margem_percentual = round_decimal((lucro_bruto / pv_total) * 100)
            comissao_por_produto = round_decimal(pv_unitario * comissao_vendedor)
            comissao_total = round_decimal(comissao_por_produto * quantidade_produtos)
            comissao_total_vendedores = round_decimal(comissao_total * num_vendedores)
            pro_labore_total = round_decimal(lucro_bruto * Decimal('0.5')) if incluir_pro_labore else Decimal('0')
            pro_labore_por_socio = [round_decimal(pro_labore_total * p) for p in porcentagem_socios] if incluir_pro_labore else []
            lucro_liquido = round_decimal(lucro_bruto - pro_labore_total)

            print("\n" + Fore.LIGHTGREEN_EX + "=" * 40)
            print(Fore.LIGHTWHITE_EX + "RESULTADOS DO CÁLCULO")
            print(Fore.LIGHTGREEN_EX + "=" * 40)
            print(Fore.LIGHTCYAN_EX + f"Custo: R${custo:,.2f}")
            print(Fore.LIGHTCYAN_EX + f"Preço de Venda Total (PV): R${pv_total:,.2f}")
            print(Fore.LIGHTGREEN_EX + "-" * 40)
            print(Fore.LIGHTCYAN_EX + f"Lucro Bruto (LB): R${lucro_bruto:,.2f}")
            print(Fore.LIGHTCYAN_EX + f"Margem Percentual (M%): {margem_percentual:.2f}%")
            print(Fore.LIGHTGREEN_EX + "-" * 40)
            print(Fore.LIGHTCYAN_EX + f"Preço de Venda por Produto: R${pv_unitario:,.2f}")
            print(Fore.LIGHTCYAN_EX + f"Comissão do Vendedor por Produto: R${comissao_por_produto:,.2f}")
            print(Fore.LIGHTCYAN_EX + f"Comissão Total do Vendedor: R${comissao_total:,.2f}")
            print(Fore.LIGHTCYAN_EX + f"Comissão Total para {num_vendedores} Vendedores: R${comissao_total_vendedores:,.2f}")
            print(Fore.LIGHTGREEN_EX + "-" * 40)
            if incluir_pro_labore:
                print(Fore.LIGHTCYAN_EX + f"Pró-labore Total: R${pro_labore_total:,.2f}")
                for i, pro_labore in enumerate(pro_labore_por_socio, 1):
                    print(Fore.LIGHTCYAN_EX + f"Pró-labore Sócio {i}: R${pro_labore:,.2f}")
            print(Fore.LIGHTCYAN_EX + f"Lucro Líquido: R${lucro_liquido:,.2f}")
            print(Fore.LIGHTGREEN_EX + "=" * 40)

            continuar = input(Fore.LIGHTYELLOW_EX + "Deseja realizar outro cálculo? (s/n): ").strip().lower()
            if continuar != 's':
                print(Fore.LIGHTMAGENTA_EX + "Encerrando o programa. Obrigado!")
                break

        except ValueError:
            print(Fore.LIGHTRED_EX + "Erro: Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    calcular_preco_venda()

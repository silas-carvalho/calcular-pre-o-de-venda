from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

def calcular_preco_venda():
    while True:
        try:
            # Solicitação de dados do usuário com substituição de vírgulas por pontos
            custo = float(input(Fore.LIGHTYELLOW_EX + "Digite o custo total dos produtos (em R$): ").replace(',', '.'))
            margem_total = float(input(Fore.LIGHTYELLOW_EX + "Digite a margem total desejada (em %): ").replace(',', '.')) / 100
            
            # Verificação de margem total logo após a entrada
            if margem_total < 0 or margem_total > 1:
                print(Fore.LIGHTRED_EX + "Erro: A margem total deve ser um valor entre 0% e 100%.")
                continue

            quantidade_produtos = int(input(Fore.LIGHTYELLOW_EX + "Digite a quantidade de produtos: "))
            num_vendedores = int(input(Fore.LIGHTYELLOW_EX + "Digite o número de vendedores: "))
            comissao_vendedor = float(input(Fore.LIGHTYELLOW_EX + "Digite a comissão de cada vendedor (em %): ").replace(',', '.')) / 100
            num_socios = int(input(Fore.LIGHTYELLOW_EX + "Digite o número de sócios: "))

            # Verificações para evitar divisões por zero ou valores inválidos
            if quantidade_produtos <= 0:
                print(Fore.LIGHTRED_EX + "Erro: A quantidade de produtos deve ser maior que zero.")
                continue
            if num_socios <= 0:
                print(Fore.LIGHTRED_EX + "Erro: O número de sócios deve ser maior que zero.")
                continue
            if num_vendedores <= 0:
                print(Fore.LIGHTRED_EX + "Erro: O número de vendedores deve ser maior que zero.")
                continue
        except ValueError:
            print(Fore.LIGHTRED_EX + "Erro: Por favor, insira valores numéricos válidos.")
            continue

        # Verificar se a margem é 100%, se for, o PV é 2 vezes o custo
        if margem_total == 1:
            pv = 2 * custo  # Para margem de 100%, PV = 2 * custo
        else:
            # Cálculo do preço de venda (PV) com base na fórmula PV = Custo / (1 - Margem Percentual)
            pv = custo / (1 - margem_total)  # Calcula o preço de venda com base na margem percentual

        # Cálculo do lucro bruto (LB) e margem percentual (M%)
        lucro_bruto = pv - custo

        # Ajuste para margem de 100%
        if margem_total == 1:
            margem_percentual = 100.00  # Se a margem for 100%, a margem percentual é 100%
        else:
            margem_percentual = (lucro_bruto / pv) * 100  # Caso contrário, calcula normalmente

        # Preço de venda por unidade (produto)
        preco_por_produto = pv / quantidade_produtos

        # Comissão do vendedor por produto e no total
        comissao_por_produto = preco_por_produto * comissao_vendedor
        comissao_total = comissao_por_produto * quantidade_produtos
        comissao_total_vendedores = comissao_total * num_vendedores  # Total de comissão para todos os vendedores

        # Pró-labore por sócio
        pro_labore_total = lucro_bruto * 0.5
        pro_labore_por_socio = pro_labore_total / num_socios

        # Lucro líquido após pró-labore
        lucro_liquido = lucro_bruto - pro_labore_total

        # Exibição dos resultados com cores e formatação de moeda
        print("\n" + Fore.LIGHTGREEN_EX + "=" * 40)
        print(Fore.LIGHTWHITE_EX + "RESULTADOS DO CÁLCULO")
        print(Fore.LIGHTGREEN_EX + "=" * 40)
        print(Fore.LIGHTCYAN_EX + f"Custo: R${custo:,.2f}")
        print(Fore.LIGHTCYAN_EX + f"Preço de Venda Total (PV): R${pv:,.2f}")
        print(Fore.LIGHTGREEN_EX + "-" * 40)
        print(Fore.LIGHTCYAN_EX + f"Lucro Bruto (LB): R${lucro_bruto:,.2f}")
        print(Fore.LIGHTCYAN_EX + f"Margem Percentual (M%): {margem_percentual:,.2f}%")
        print(Fore.LIGHTGREEN_EX + "-" * 40)
        print(Fore.LIGHTCYAN_EX + f"Preço de Venda por Produto: R${preco_por_produto:,.2f}")
        print(Fore.LIGHTCYAN_EX + f"Comissão do Vendedor por Produto: R${comissao_por_produto:,.2f}")
        print(Fore.LIGHTCYAN_EX + f"Comissão Total do Vendedor: R${comissao_total:,.2f}")
        print(Fore.LIGHTCYAN_EX + f"Comissão Total para {num_vendedores} Vendedores: R${comissao_total_vendedores:,.2f}")
        print(Fore.LIGHTGREEN_EX + "-" * 40)
        print(Fore.LIGHTCYAN_EX + f"Pró-labore Total: R${pro_labore_total:,.2f}")
        print(Fore.LIGHTCYAN_EX + f"Pró-labore por Sócio: R${pro_labore_por_socio:,.2f}")
        print(Fore.LIGHTCYAN_EX + f"Lucro Líquido: R${lucro_liquido:,.2f}")
        print(Fore.LIGHTGREEN_EX + "=" * 40)

        # Perguntar se deseja realizar novo cálculo
        continuar = input(Fore.LIGHTYELLOW_EX + "Deseja realizar outro cálculo? (s/n): ").strip().lower()
        if continuar != 's':
            print(Fore.LIGHTMAGENTA_EX + "Encerrando o programa. Obrigado!")
            break

if __name__ == "__main__":
    calcular_preco_venda()

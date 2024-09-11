import streamlit as st

# Função para calcular INSS de acordo com o salário bruto
def calcular_inss(salario_bruto):
    # Faixas de INSS para 2023 (valores em reais)
    faixas_inss = [
        (1302.00, 0.075),
        (2571.29, 0.09),
        (3856.94, 0.12),
        (7507.49, 0.14),
    ]
    
    desconto_inss = 0
    salario_restante = salario_bruto

    for faixa, aliquota in faixas_inss:
        if salario_restante > faixa:
            desconto = faixa * aliquota
            desconto_inss += desconto
            salario_restante -= faixa
        else:
            desconto = salario_restante * aliquota
            desconto_inss += desconto
            break

    # O teto máximo para o desconto é o salário acima de 7507.49
    if salario_bruto > 7507.49:
        desconto_inss = 877.24  # Valor máximo de INSS em 2023

    return desconto_inss

# Função para calcular IRPF de acordo com o salário base
def calcular_irpf(salario_base):
    # Faixas de IRPF para 2023
    faixas_irpf = [
        (1903.98, 0.0),
        (2826.65, 0.075),
        (3751.05, 0.15),
        (4664.68, 0.225),
        (float('inf'), 0.275)
    ]
    
    # Deduções fixas para cada faixa
    deducoes_irpf = [
        0.0,
        142.80,
        354.80,
        636.13,
        869.36
    ]
    
    desconto_irpf = 0
    salario_restante = salario_base

    for i, (faixa, aliquota) in enumerate(faixas_irpf):
        if salario_restante > faixa:
            desconto = faixa * aliquota
            desconto_irpf += desconto
            salario_restante -= faixa
        else:
            desconto = salario_restante * aliquota
            desconto_irpf += desconto
            break

    # Subtraindo as deduções de cada faixa
    for i, (faixa, aliquota) in enumerate(faixas_irpf):
        if salario_base > faixa:
            desconto_irpf -= deducoes_irpf[i]
        else:
            break

    return desconto_irpf

# Função para calcular salário líquido
def calcular_salario_liquido(salario_bruto, outros_descontos=0):
    desconto_inss = calcular_inss(salario_bruto)
    salario_base_irpf = salario_bruto - desconto_inss
    desconto_irpf = calcular_irpf(salario_base_irpf)
    salario_liquido = salario_bruto - desconto_inss - desconto_irpf - outros_descontos
    return salario_liquido, desconto_inss, desconto_irpf

# Função principal do Streamlit
def main():
    st.title('Calculadora de Salário Líquido')
    
    # Entrada do salário bruto
    salario_bruto = st.number_input('Digite seu salário bruto:', min_value=0.0, step=100.0)
    
    # Entrada para outros descontos
    outros_descontos = st.number_input('Digite outros descontos (como plano de saúde, etc):', min_value=0.0, step=10.0)
    
    if st.button('Calcular Salário Líquido'):
        salario_liquido, desconto_inss, desconto_irpf = calcular_salario_liquido(salario_bruto, outros_descontos)
        
        # Mostra os resultados
        st.subheader('Detalhes do Cálculo')
        st.write(f"**Salário Bruto:** R$ {salario_bruto:,.2f}")
        st.write(f"**Desconto INSS:** R$ {desconto_inss:,.2f}")
        st.write(f"**Base de cálculo para o IRPF:** R$ {salario_bruto - desconto_inss:,.2f}")
        st.write(f"**Desconto IRPF:** R$ {desconto_irpf:,.2f}")
        st.write(f"**Outros descontos:** R$ {outros_descontos:,.2f}")
        st.write(f"**Salário Líquido:** R$ {salario_liquido:,.2f}")

if __name__ == '__main__':
    main()

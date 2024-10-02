import streamlit as st

# Função para calcular os valores
def calcular_custos(salario_base):
    # Percentuais e valores
    fgts = salario_base * 0.08  # 8% do salário
    ferias = salario_base / 12  # 1/12 do salário
    decimo_terceiro = salario_base / 12  # 1/12 do salário
    terco_ferias = ferias / 3  # 1/3 das férias
    fgts_ferias_13 = (ferias + decimo_terceiro) * 0.08  # FGTS sobre férias e 13º
    vt = salario_base * 0.06  # Exemplo de 6% do salário (pode ser ajustado conforme política da empresa)
    vr = 150.00  # Vale Refeição fixo, pode ser ajustado conforme regra
    
    # Custo Total Mensal
    custo_total = salario_base + fgts + ferias + decimo_terceiro + terco_ferias + fgts_ferias_13 + vt + vr
    
    # Salário Líquido do Funcionário (desconto de VT)
    salario_liquido = salario_base - vt  # Salário menos o desconto do vale transporte
    
    return fgts, ferias, decimo_terceiro, terco_ferias, fgts_ferias_13, vt, vr, custo_total, salario_liquido

# Interface com o Streamlit
st.title('Cálculo do Custo Completo de um Funcionário')

# Input de salário
salario_base = st.number_input('Digite o Salário Base (R$)', value=1500.00)

# Botão para realizar o cálculo
if st.button('Calcular'):
    fgts, ferias, decimo_terceiro, terco_ferias, fgts_ferias_13, vt, vr, custo_total, salario_liquido = calcular_custos(salario_base)
    
    st.subheader('Resultados Detalhados')
    st.write(f'FGTS (8%): R$ {fgts:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))
    st.write(f'Férias (1/12): R$ {ferias:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))
    st.write(f'13º Salário (1/12): R$ {decimo_terceiro:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))
    st.write(f'1/3 Férias: R$ {terco_ferias:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))
    st.write(f'FGTS sobre Férias e 13º: R$ {fgts_ferias_13:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))
    st.write(f'Vale Transporte (6%): R$ {vt:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))
    st.write(f'Vale Refeição: R$ {vr:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))
    
    st.subheader('Resumo')
    st.write(f'Custo Total Mensal: R$ {custo_total:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))
    st.write(f'Salário Líquido do Funcionário: R$ {salario_liquido:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))

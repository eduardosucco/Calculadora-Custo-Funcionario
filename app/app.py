import streamlit as st

# Função para calcular o custo total de um funcionário
def calcular_custo_total(salario_bruto):
    # Valores fixos conforme o exemplo fornecido
    fgts = 0.08 * salario_bruto  # 8% do salário
    ferias = salario_bruto / 12   # 1/12 do salário para férias
    decimo_terceiro = salario_bruto / 12  # 1/12 do salário para 13º
    um_terco_ferias = ferias / 3  # 1/3 de férias
    fgts_ferias_13 = (ferias + decimo_terceiro) * 0.08  # FGTS sobre férias e 13º
    vt = 150.00  # Exemplo fixo para VT
    vr = 150.00  # Exemplo fixo para VR

    custo_total = (salario_bruto + fgts + ferias + decimo_terceiro +
                   um_terco_ferias + fgts_ferias_13 + vt + vr)
    
    # Salário líquido (considerando desconto INSS e IRPF hipotéticos)
    salario_liquido = salario_bruto - (fgts * 0.07)  # Supondo 7% de desconto para simplificação
    return {
        "FGTS": fgts,
        "Férias": ferias,
        "13º": decimo_terceiro,
        "1/3 Férias": um_terco_ferias,
        "FGTS Férias/13º": fgts_ferias_13,
        "VT": vt,
        "VR": vr,
        "Custo Total Mensal": custo_total,
        "Salário Líquido": salario_liquido
    }

# Função principal do Streamlit
def main():
    st.title('Calculadora de Custo Completo de Funcionário')

    # Entrada do salário bruto
    salario_bruto = st.number_input('Digite o salário bruto do funcionário:', min_value=0.0, step=100.0, value=1500.0)
    
    if st.button('Calcular Custo Completo'):
        # Cálculos
        custos = calcular_custo_total(salario_bruto)
        
        # Mostra os resultados
        st.subheader('Detalhes do Cálculo')
        st.write(f"**Salário Bruto:** R$ {salario_bruto:,.2f}")
        for item, valor in custos.items():
            st.write(f"**{item}:** R$ {valor:,.2f}")

if __name__ == '__main__':
    main()

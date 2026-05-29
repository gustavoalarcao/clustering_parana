import numpy as np
import streamlit as st
from streamlit import session_state as ss


from config.caminhos import arquivo_maj_daniel

from coleta.coleta_impacto_proporcional import coletando_ocorrencias_de_desastres

from analise.impacto_proporcional import gerando_grafico_de_barras_impacto_proporcional

from utils.auxiliar_plotagem import mostrar_grafico




def pg_maj_daniel() -> None:
    # Carregamento dos dados.
    df_desastres = coletando_ocorrencias_de_desastres(arquivo_maj_daniel)

    # Limpeza.
    df_desastres['Prejuízo Público'] = df_desastres['Prejuízo Público'].str.replace('R$', '')
    df_desastres['Prejuízo Público'] = df_desastres['Prejuízo Público'].str.replace('.', '')
    df_desastres['Prejuízo Público'] = df_desastres['Prejuízo Público'].str.replace(',', '.')

    # Visualização dados limpos.
    st.write(df_desastres)

    # Agrupando por impaco proporcional ao tamanho da população.
    df_desastres['impacto proporcional a populacao'] = df_desastres['Pessoas Afetadas'] / df_desastres['População'] 
    impacto_proporcional_a_populacao = df_desastres.groupby('Município')['impacto proporcional a populacao'].sum()
    impacto_proporcional_a_populacao = impacto_proporcional_a_populacao.sort_values(ascending=False)
    # Removendo cidades com impacto relativo mínimo.
    impacto_proporcional_a_populacao = impacto_proporcional_a_populacao.replace([np.inf, -np.inf], np.nan).dropna()
    norma = impacto_proporcional_a_populacao.sum()
    impacto_normalizado = impacto_proporcional_a_populacao / norma
    mais_impactadas = impacto_normalizado[impacto_normalizado > 0.01]

    # Visualização impacto proporcional.
    st.write(mais_impactadas)
    grafico_de_barras_impacto_proporcional = gerando_grafico_de_barras_impacto_proporcional(mais_impactadas)
    mostrar_grafico(grafico_de_barras_impacto_proporcional)
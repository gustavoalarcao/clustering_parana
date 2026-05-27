import numpy as np
import streamlit as st
from streamlit import write, session_state as ss


import config.caminhos as cam

from coleta.coleta_impacto_proporcional import coletando_ocorrencias_de_desastres

from processamento.impacto_proporcional import gerando_grafico_de_barras_impacto_proporcional

from utils.auxiliar_plotagem import mostrar_grafico




def pg_impacto_proporcional() -> None:
    df_desastres = coletando_ocorrencias_de_desastres(cam.arquivo_ocorrencia_desastres)
    # df_desastres
    # df_desastres.dtypes

    df_desastres['Prejuízo Público'] = df_desastres['Prejuízo Público'].str.replace('R$', '')
    df_desastres['Prejuízo Público'] = df_desastres['Prejuízo Público'].str.replace('.', '')
    df_desastres['Prejuízo Público'] = df_desastres['Prejuízo Público'].str.replace(',', '.')

    df_desastres['impacto proporcional a populacao'] = df_desastres['Pessoas Afetadas'] / df_desastres['População'] 

    impacto_proporcional_a_populacao = df_desastres.groupby('Município')['impacto proporcional a populacao'].sum()
    impacto_proporcional_a_populacao = impacto_proporcional_a_populacao.sort_values(ascending=False)
    # Removendo cidades com impacto relativo mínimo.
    impacto_proporcional_a_populacao = impacto_proporcional_a_populacao.replace([np.inf, -np.inf], np.nan).dropna()

    norma = impacto_proporcional_a_populacao.sum()
    impacto_normalizado = impacto_proporcional_a_populacao / norma
    write(impacto_normalizado)

    mais_impactadas = impacto_normalizado[impacto_normalizado > 0.01]
    grafico_de_barras_impacto_proporcional = gerando_grafico_de_barras_impacto_proporcional(mais_impactadas)
    mostrar_grafico(grafico_de_barras_impacto_proporcional)
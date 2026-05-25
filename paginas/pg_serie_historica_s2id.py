import streamlit as st
from streamlit import write, session_state as ss


from config.caminhos import arquivo_serie_hitorica_2016

from coleta.dados_serie_historica_s2id import extraindo_dados_serie_historica_s2id




def pg_serie_historica_s2id() -> None:
    df = extraindo_dados_serie_historica_s2id(arquivo_serie_hitorica_2016)
    write(df)
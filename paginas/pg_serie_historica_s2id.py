import streamlit as st


from coleta.coleta_serie_historica_s2id import coletando_dados_serie_historica_s2id





def pg_serie_historica_s2id() -> None:
    df = coletando_dados_serie_historica_s2id()
    st.write(df)

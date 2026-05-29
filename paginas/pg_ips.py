import streamlit as st


from coleta.coleta_ips import coletando_dados_ips




def pg_ips() -> None:
    df = coletando_dados_ips()
    st.write(df.sort_values(by='Nota Mediana no Enem'))
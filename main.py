"""
Visualização das análises de dados via Streamlit.

Este módulo provê uma interface para facilitar a visualização 
de operações em DataFrames e gráficos durante o desenvolvimento. 
A utilização do Streamlit permite uma prototipagem mais ágil 
em comparação com ambientes de Notebook tradicionais.
"""



import streamlit as st
from streamlit import session_state as ss

st.set_page_config(layout='wide')


from paginas.pg_maj_daniel import pg_maj_daniel
from paginas.pg_serie_historica_s2id import pg_serie_historica_s2id
from paginas.pg_atlas import pg_atlas
from paginas.pg_ips import pg_ips



paginas = [
    st.Page(pg_maj_daniel),
    st.Page(pg_serie_historica_s2id),
    st.Page(pg_atlas),
    st.Page(pg_ips),
]


pg = st.navigation(paginas)
pg.run()



















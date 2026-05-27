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


from paginas.pg_impacto_proporcional import pg_impacto_proporcional
from paginas.pg_serie_historica_s2id import pg_serie_historica_s2id
from paginas.pg_atlas import pg_atlas




pg_1 = st.Page(pg_impacto_proporcional)
pg_2 = st.Page(pg_serie_historica_s2id)
pg_3 = st.Page(pg_atlas)


pg = st.navigation([pg_1, pg_2, pg_3])
pg.run()



















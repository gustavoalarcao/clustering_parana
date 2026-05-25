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


from paginas.impacto_proporcional import pg_impacto_proporcional




pg_1 = st.Page(pg_impacto_proporcional)

pg = st.navigation([pg_1])
pg.run()



















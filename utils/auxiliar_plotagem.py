from pathlib import Path


import plotly.graph_objects as go
import streamlit as st


import utils.estilos as est




def baixar_grafico( 
        plot: go.Figure, 
        filename: str, 
        width: int=est.largura,
        height: int=est.altura, 
) -> None:
    downloads_path = Path.home() / "Downloads"
    output_file = downloads_path / filename
    plot.write_image(output_file, height=height, width=width)
    

def mostrar_grafico(plot: go.Figure) -> None:
    st.plotly_chart(
        plot, 
        key=f'key-{id(plot)}',
        width='stretch', 
        config={'staticPlot': True}
    )
    
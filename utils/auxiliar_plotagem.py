import plotly.graph_objects as go
import streamlit as st

from pathlib import Path

import utils.constantes as cte




def baixar_grafico( 
        plot: go.Figure, 
        filename: str, 
        width: int=cte.largura,
        height: int=cte.altura, 
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
    
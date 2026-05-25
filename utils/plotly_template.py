import plotly.graph_objects as go

import utils.constantes as cte


template = go.layout.Template()
template.layout = dict(
    autosize=False,
    showlegend=False,

    xaxis=dict( 
        showgrid=False,
        zeroline=False,
        showline=True,
        mirror=True,

        title=dict(
            font=dict(
                size=14,
                color=cte.cor_principal
            ),
            standoff=10,
        ),
        tickfont=dict(
            size=10,
            color=cte.cor_principal
        ),

        gridcolor=cte.cor_principal,
        linecolor=cte.cor_principal,
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=True,
        mirror=True,

        title=dict(
            font=dict(
                size=14,
            ),
            standoff=10,
        ),
        tickfont=dict(
            size=10,
            color=cte.cor_principal
        ),

        gridcolor=cte.cor_principal,
        linecolor=cte.cor_principal, 
    ),
    margin=dict(t=30,b=60,r=60,l=60),
    paper_bgcolor='white',
    plot_bgcolor='white',
    width=cte.largura,
    height=cte.altura,
)
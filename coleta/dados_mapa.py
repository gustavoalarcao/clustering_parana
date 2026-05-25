import requests


import clustering_parana.utils.estilos as cte





def coletando_coordenadas_parana(url):
    try:
        pr_geo_json = requests.get(url).json()
        pr_geo_json['features'][0]['id'] = 'PR'
    except:
        print('Erro na coleta de dados para a mapa')
    else:
        return pr_geo_json
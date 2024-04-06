from pathlib import Path
import json

import plotly.express as px 

#le os dados como uma string e os converte em um objeto Python
path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

#Examina todos os terremotos no conjunto de dados 
all_eq_dicts = all_eq_data['features']

#Passa por cada arquivo e o separa 
mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

#Plota o mapa mundi     
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=eq_title,
        color=mags,
        color_continuous_scale='Viridis',
        labels={'color':'Magnitude'},
        projection='natural earth',
        hover_name=eq_titles,
    )
fig.show()    
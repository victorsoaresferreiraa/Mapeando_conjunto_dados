from pathlib import Path 
import json

import plotly.express as px 

#le os dados como uma string e os converte em um objeto python
path = Path('eq_data\eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)


#Cria uma versao mais legivel do arquivo de dados 
path = Path('eq_data\readable_eq_data_.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

#Examina todos os terremotos no conjunto de dados 
all_eq_dicts = all_eq_data['Features']

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
title = 'Global Eathquakes'
fig = px.scatter_geo(lat=lats, lon=lons, title=title,
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_title,)

fig.show()    


#print(len(all_eq_dicts))

mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)

print(mags[:10]) 


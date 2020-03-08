from arcgis.gis import GIS
from arcgis.geometry import distance
from IPython.display import display
from arcgis.features import FeatureLayer
gis = GIS("https://www.arcgis.com")
lyr_url = 'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/1'

layer = FeatureLayer(lyr_url)

a=layer.query(where="Country_Region='US'")

# a.features[0].attributes['Lat']
list_of_virus_locations = []
for i in range(len(a.features)):
    list_of_virus_locations.append((a.features[i].geometry['x'],a.features[i].geometry['y']))

# print(list_of_virus_locations)
# print(a.features[0].geometry)

user_geometry = {'x': 20.40119999999996, 'y': 39.07310000000007}
d=distance(geometry1=user_geometry,geometry2=a.features[0].geometry,spatial_ref=a.spatial_reference['latestWkid'])
for i in range(len(list_of_virus_locations)):
    temp_d = distance(geometry1=user_geometry,geometry2=a.features[i].geometry,spatial_ref=a.spatial_reference['latestWkid'])
    if(temp_d['distance'] < d['distance']):
        d=temp_d

# layer.properties
# a.spatial_reference
# print(d)
print("Distance between you and the nearest coronavirus is ",d['distance']," miles")

if(d['distance'] < 50):
    print("Distance between you and the virus is less than 50 and hence you might be at risk")

# docs @ http://flask.pocoo.org/docs/1.0/quickstart/

# from flask import Flask, jsonify, request, render_template
# app = Flask(__name__)

# @app.route('/hello', methods=['GET', 'POST'])
# def hello():

#     # POST request
#     if request.method == 'POST':
#         print('Incoming..')
#         print(request.get_json())  # parse as JSON
#         return 'OK', 200

#     # GET request
#     else:
#         message = {'greeting':'Hello from Flask!'}
#         return jsonify(message)  # serialize and use JSON headers

# @app.route('/test')
# def test_page():
#     # look inside `templates` and serve `index.html`
#     return render_template('index.html')
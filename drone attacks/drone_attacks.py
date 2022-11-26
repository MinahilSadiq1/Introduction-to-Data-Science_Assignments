import folium
import pandas as pd

pakistan_map = folium.Map(location=[30.37,69.34],zoom_start=4.5,tiles='OpenStreetMap')

#load the dataset (csv file) into the Pandas dataframe
df = pd.read_csv('DroneSet.csv')

#calculate total number of cases using a loop
t = 0
for c in df['total cases']:
  t = int(c)+int(t)

# mark circles on the map and display the map
for region, lat, long, tc, d in zip(list(df['Region']), list(df['Latitude']), list(df['Longitude']), list(df['total cases']), list(df['Date'])):
    folium.CircleMarker(location=[lat, long],
                        radius=(tc/t)*100,
                        color='red',
                        fill=False,
                        fill_color='green').add_to(pakistan_map)

    xyz = '<strong>Region:  ' + region + '</strong><br>' + 'Total Cases: ' + str(tc) + '<br>' + 'Deaths: ' + str(
        d)
    iframe = folium.IFrame(xyz, width=200, height=150)
    popupData = folium.Popup(iframe, max_width=500)
    folium.Marker(location=[lat, long], popup=popupData).add_to(pakistan_map)

pakistan_map.save('map1.html')
#!/usr/local/pyenv/versions/anaconda3-4.3.0/bin/python

print("Content-Type: text/html\n")

import folium
points = []
points.append(tuple([35.658505, 139.802043]))
points.append(tuple([35.660445, 139.800450]))
points.append(tuple([35.661617, 139.802349]))

m = folium.Map(location=[35.660445, 139.800450], zoom_start=15)
folium.PolyLine(points).add_to(m)
folium.Marker(points[0], popup='Mt. Hood Meadows').add_to(m)
folium.Marker(points[1], popup='Timberline Lodge').add_to(m)
folium.Marker(points[2], popup='Timberline Lodge').add_to(m)

print(m.get_root().render())

#m.save(outfile="map.html")

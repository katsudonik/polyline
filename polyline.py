#!/usr/local/pyenv/versions/anaconda3-4.3.0/bin/python

print("Content-Type: text/html\n")

import folium
import numpy as np

points = []
points.append([35.658505, 139.802043])
points.append([35.661617, 139.802349])
points.append([35.660445, 139.800450])

points = np.array(points)
location = [( np.max(points[:,0]) + np.min(points[:,0]) ) / 2, ( np.max(points[:,1]) + np.min(points[:,1]) ) / 2]

points = points.tolist()

m = folium.Map(location=location, zoom_start=15)
folium.PolyLine(points).add_to(m)
folium.Marker(points[0], popup='Mt. Hood Meadows').add_to(m)
folium.Marker(points[1], popup='Timberline Lodge').add_to(m)
folium.Marker(points[2], popup='Timberline Lodge').add_to(m)

print(m.get_root().render())

#m.save(outfile="map.html")

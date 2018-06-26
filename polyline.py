#!/usr/local/pyenv/versions/anaconda3-4.3.0/bin/python

print("Content-Type: text/html\n")

import folium
import numpy as np
import math

points = []
points.append([35.658505, 139.802043])
points.append([35.660445, 139.800450])
points.append([35.661617, 139.802349])
#points.append([35.660445, 159.809724])



points = np.array(points)
location = [( np.max(points[:,0]) + np.min(points[:,0]) ) / 2, ( np.max(points[:,1]) + np.min(points[:,1]) ) / 2]

width = np.max([( np.max(points[:,0]) - np.min(points[:,0]) ),  ( np.max(points[:,1]) - np.min(points[:,1]) )])

points = points.tolist()

x = width

#zoom = math.log(5*x/12280, 0.5)
zoom = math.log(5*x/9500, 0.5)

#print(width)
#print(" ")
#print(zoom)

m = folium.Map(location=location, zoom_start=zoom)
folium.PolyLine(points, color='red').add_to(m)
for point in points:
  folium.Marker(point).add_to(m)
print(m.get_root().render())

#m.save(outfile="map.html")

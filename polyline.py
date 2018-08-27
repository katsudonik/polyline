#!/usr/local/pyenv/versions/anaconda3-4.3.0/bin/python

print("Content-Type: text/html\n")

import folium
import numpy as np
import math
import copy

def get_center(points):
  return [( np.max(points[:,0]) + np.min(points[:,0]) ) / 2, ( np.max(points[:,1]) + np.min(points[:,1]) ) / 2]

def get_width(points):
  return np.max([( np.max(points[:,0]) - np.min(points[:,0]) ),  ( np.max(points[:,1]) - np.min(points[:,1]) )])

def get_zoom_rate(width):
  #zoom = math.log(5*x/12280, 0.5)
  return math.log(5*width/9500, 0.5)

def get_map(center, zoom):
  return folium.Map(location=center, zoom_start=zoom)

def draw_polyline(m, points):
  folium.PolyLine(points, color='blue').add_to(m)

def draw_marker(m, point, color):
  folium.Marker(location=point, icon=folium.Icon(color=color)).add_to(m)


points = []
points.append([35.658505, 139.802043])
points.append([35.660445, 139.800450])
points.append([35.661617, 139.802349])
#points.append([35.660445, 159.809724])

start_point = [35.658505, 139.802043]
goal_point = [35.671650, 139.822349]


_points = copy.deepcopy(points)
_points.append(start_point)
_points.append(goal_point)
_points = np.array(_points)

center = get_center(_points)
zoom = get_zoom_rate(get_width(_points))

m = get_map(center, zoom)

points = np.array(points)
points = points.tolist()

draw_polyline(m, points)
draw_marker(m, start_point, 'blue')
draw_marker(m, goal_point, 'red')
print(m.get_root().render())

#m.save(outfile="map.html")



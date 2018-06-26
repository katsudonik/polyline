# polyline

# middleware
* Python 3.6.0 :: Anaconda 4.3.0 (64-bit) (pyenv)
```
/usr/local/pyenv/
```
* folium==0.5.0
* npm 3.10.10
* nodejs v6.14.2
* phantomjs@2.1.7
* httpd

# setting
* httpd.conf
```
<IfModule alias_module>
    ScriptAlias /cgi-bin/ "/var/www/cgi-bin/"
</IfModule>
```

```
<Directory "/var/www/cgi-bin">
    AllowOverride None
    Options ExecCGI
    Require all granted
    AddHandler cgi-script .cgi .py

</Directory>
```
* polyline.py  
deploy on "/var/www/cgi-bin/"
* screenshot.py  
deploy

# run
```
python screenshot.py 
```

# view img:  
http://localhost:8080/polyline.png


## CO2 emissions

### emissions_per_unit[kg-CO2/L]
https://www.env.go.jp/council/16pol-ear/y164-04/mat04.pdf

### by distance
#### required params
* fuel_efficient[km/L]
* distance[km]
* fuel

#### function
```
emissions = (emissions_per_unit / fuel_efficient) * distance
```
### by hour
#### required params
* fuel_consumption_rate[L/kw･h]
* engine_output[kw]
* fuel_efficient_by_hour[L/h]: fuel_consumption_rate * engine_output
* hour[h]
* fuel
#### function
```
emissions = (emissions_per_unit / fuel_efficient_by_hour) * hour
```



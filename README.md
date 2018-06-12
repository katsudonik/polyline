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

# run
```
python screenshot.py 
```

# view img:  
http://localhost:8080/polyline.png

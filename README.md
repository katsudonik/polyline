# polyline

# middleware
* Python 3.6.0 :: Anaconda 4.3.0 (64-bit) (pyenv)
```
/usr/local/pyenv/
```
* npm 3.10.10
* nodejs v6.14.2
* phantomjs
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

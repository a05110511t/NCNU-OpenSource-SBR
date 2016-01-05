# PPQ
Poorman's Printed Quadcopter

1. Let pi learning use WiFi, so we can ssh it.
http://inpega.blogspot.tw/2013/09/blog-post_15.html

2. Install RPi.GPIO 
$sudo apt-get install python-dev
$wget https://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.5.4.tar.gz
$tar xvzf RPi.GPIO-0.5.4.tar.gz
$cd RPi.GPIO-0.5.4
$sudo apt-get install libevent-dev
$sudo python3 setup.py install #python will crash.

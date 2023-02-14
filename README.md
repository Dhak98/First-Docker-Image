# First-Docker-Image
#1. Install all required dependencies

python and it dependencies

apt-get install -y python python -setuptools python-dev build-essential python-pip ptython-mysqldb

#2. Install and configure Web Server

install python flask dependencies

pip install flask
pip install flask-mysql

----copy app.py or download it from source repositary
----configure database credentials and parameters

#3. start web server

FLASK_APP=app.py flask run --host=0.0.0.0

#4. Test

open browser and go to URL

http://<ip>:5000    ==> Home page

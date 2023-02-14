import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def method_name():
    return "This is just a Sample docker image for learn how to build the image"

if __name__ == "__main__":
    app.run()
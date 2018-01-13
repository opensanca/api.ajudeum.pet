from flask import Flask
from api.animals.endpoints import animal

app = Flask(__name__) 

app.register_blueprint(animal)

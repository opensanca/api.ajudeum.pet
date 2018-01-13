from flask import Flask
from api.animals.endpoints import animal
from mongoengine import connect
import settings

connect(host=settings.MONGODB_URI)
app = Flask(__name__) 

app.register_blueprint(animal)

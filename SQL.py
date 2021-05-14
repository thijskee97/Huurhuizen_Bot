from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from main import submit
from webscraping_with_sel import aantal_woningen_zoekopdracht


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database_users1.sqlite"
db = SQLAlchemy(app)
submit = submit()
stad = submit[0]
minprijs = submit[1]
maxprijs = submit[2]
telnr = submit[3]
aantal_woningen = aantal_woningen_zoekopdracht(stad=stad,minprijs=minprijs,maxprijs=maxprijs)


class Preference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stad = db.Column(db.String, nullable=True)
    minprijs = db.Column(db.Integer, nullable=False)
    maxprijs = db.Column(db.Integer, nullable=False)
    telnr = db.Column(db.Integer, unique=True)
    aantal_woningen_db = db.Column(db.Integer)



db.session.add(Preference(stad=stad, minprijs=minprijs,maxprijs=maxprijs, telnr=telnr,aantal_woningen_db=aantal_woningen))
db.session.commit()




import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT  #Flask JWT:  Json  Web Tok -> encoding Data

from db import db
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db') # probiert erst 1 dann 2
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key = "philipp"
api = Api(app)



# Add endpoints/resources
jwt = JWT(app, authenticate, identity) # creates new endpoint: /
api.add_resource(Store,'/store/<string:name>') 
api.add_resource(Item,'/item/<string:name>') 
api.add_resource(ItemList,'/items')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    app.run(port=5000, debug=True)

#Status Codes
# 200 Ok
# 201 Created (succesfully)
# 202 Accepted
# 400 bad request
# 404 Error Code



from flask import Flask
from flask_restful import Resource, Api
from resources.hotel import Hoteis,Hotel
from resources.user import user, UserRegister, UserLogin, UserLougot
from con_sql import bd  
from flask_jwt_extended import JWTManager

# variavel representar a minha aplicação 
app = Flask(__name__)

#configurar
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hoteis.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET-KEY"]= " a_minha_palavra_secreta_para_aminha_api_vai_ser_forte"

api = Api(app)
jwt = JWTManager (app)


#rotas
api.add_resource(Hoteis, "/hoteis")
api.add_resource(Hotel, "/hoteis/<string:id_hotel>")
api.add_resource(user, "/users/<string:username>")
api.add_resource(UserRegister, "/registar")
api.add_resource(UserLogin, "/login")
api.add_resource(UserLougot, "/logout>")

if __name__ == "__main__":
    bd.init_app(app)
    with app.app_context():
        bd.create_all()
    app.run(debug=True)
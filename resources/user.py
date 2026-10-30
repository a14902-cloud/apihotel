from flask_restful import Resource, reqparse
from models.user import userModel
from hmac import compare_digest
from flask_jwt_extended import create_access_token, jwt_required

class user (Resource):

    def get(self, username):
        user_encontrado = userModel.find_user(username)
        if user_encontrado:
                return user_encontrado.json(), 200
        return { "message" : "User not found"}, 404
    @jwt_required()
    def delete(self, username):
        hotel_encontrado = userModel.find_hotel(username)
        if hotel_encontrado:
            hotel_encontrado.delete_hotel()
            return { "message": f"User with {username} deleted"}
        return { "message": "User not found"}, 404
x
class UserRegister(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("username", type=str, help="username obrigatótio")
    argumentos.add_argument("password", type=str, help="password obrigatótio")

    def post(self, ):
        dados = UserRegister.argumentos.parse_args()# Dicionário
        user_encontrado = userModel.find_user(dados["username"])
        if user_encontrado:
            return { " message": "User with this username already exists"}
        novo_user = userModel(**dados)
        novo_user.save_hotel()
        return novo_user.json(), 200

class UserLogin(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("username", type=str, help="username obrigatótio")
    argumentos.add_argument("password", type=str, help="password obrigatótio")

    def post(self):
        dados =UserLogin.argumentos.parse_args()
        user =userModel.find_user(dados["username"])

        if user and compare_digest(user.password,dados["password"]):
            token =create_access_token(identity=user.username)
            return{ " access_token": token }
        return{"message": "Username or password invalid!"}
    

class UserLougot(Resource):
    ...


from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required




# Listar todos os hóteis
class Hoteis(Resource):
    def get(self):
        return { "hoteis": [hotel.json() for hotel in HotelModel.query.all()]}


# Listar, inserir, atualizar e eliminar um hotel específico
class Hoteis(Resource):
    path_params = reqparse.RequestParser()
    path_params.add_argument("cidade", type=str, default="", loacation="args")
    path_params.add_argument("Estrelas_min", type=float, default=0, loacation="args")
    path_params.add_argument("Estrelas_max", type=float, default=5, loacation="args")
    path_params.add_argument("diaria_min", type=float, default=0, loacation="args")
    path_params.add_argument("diaria_max", type=float, default=0, loacation="args")
    path_params.add_argument("itens", type=int, default=3, loacation="args")
    path_params.add_argument("page", type=int, default=1, loacation="args")

def get(self):
    meus_filtros = Hoteis.path_params.parse_args()



class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome", type=str, help="Nome obrigatótio")
    argumentos.add_argument("estrelas", type=float, help="Estrelas obrigatótio")
    argumentos.add_argument("diaria", type=float, help="Diária obrigatótio")
    argumentos.add_argument("cidade", type=str, help="Cidade obrigatótio")


    def get(self, id_hotel):
        hotel_encontrado = HotelModel.find_hotel(id_hotel)
        if hotel_encontrado:
                return hotel_encontrado.json(), 200
        return { "message" : "Hotel not found"}, 404
        

    @jwt_required()
    def post(self, id_hotel):
        dados = Hotel.argumentos.parse_args()# Dicionário
        hotel_encontrado = HotelModel.find_hotel(id_hotel)
        if hotel_encontrado:
         return { " message": "Hotel with this id already exists"}
        novo_hotel = HotelModel(id_hotel, **dados)
        novo_hotel.save_hotel()
        return novo_hotel.json(), 200


    def put(self, id_hotel):
        dados = Hotel.argumentos.parse_args()
        Hotel_encontrado = HotelModel.find_hotel(id_hotel)
        if Hotel_encontrado:
            lista = [dado for dado in dados.values()]
            hotel_atualizado = HotelModel(id_hotel, **dados)
            hotel_atualizado.update_hotel(**dados)
            hotel_atualizado.save_hotel()
            return hotel_atualizado.json(), 200


        novo_hotel = HotelModel(id_hotel, **dados)
        novo_hotel.save_hotel()
        return novo_hotel.json(), 200
            
    

    @jwt_required()
    def delete(self, id_hotel):
        hotel_encontrado = HotelModel.find_hotel(id_hotel)
        if hotel_encontrado:
            hotel_encontrado.delete_hotel()
            return { "message": f"Hotel with {id_hotel} deleted"}
        return { "message": "Hotel not found"}, 404
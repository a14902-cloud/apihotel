from flask_restful import Resource, reqparse

hoteis =[
    { "hotel_id" : "paraiso", "nome": "Hotel paraiso", "estrelas":4.6, "diaria": 123.99, "cidade": "porto"},
    { "hotel_id" : "fukui", "nome": "Fukui Resort", "estrelas":4.8, "diaria": 255.99, "cidade": "Viena"},
    { "hotel_id" : "agua", "nome": "Hotel agua", "estrelas":4.2, "diaria": 193.99, "cidade": "lisboa"},
]

# listar todos os hoteis 
class Hoteis(Resource):
    def get(self):
        return { "hoteis" : hoteis}

# Listar, inserir, atualizar e eliminar um hotel específico

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome" , type=str, help="Nome obrigatório")
    argumentos.add_argument("estrelas" , type=float, help="Estrelas obrigatório")
    argumentos.add_argument("diaria" , type=float, help="Diaria obrigatório")
    argumentos.add_argument("cidade" , type=str, help="Cidade obrigatório")
    def get(self, id_hotel):
        for hotel in hoteis:
            if hotel["hotel_id"] == id_hotel:
                return hotel, 200
        return { "message": "hotel not found"}, 404

    def post(self, id_hotel):
        dados = Hotel.argumentos.parse_args() #Dicionário                    
        for hotel in hoteis:
             if hotel["hotel_id"] == id_hotel:
                 return{ "message": "Hotel witch this id already exists"}
             
        novo_hotel = {"hotel_id" : id_hotel, **dados }
        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, id_hotel):
        dados = Hotel.argumentos.parse_args() #Dicionário                    
        for hotel in hoteis:
             if hotel["hotel_id"] == id_hotel:
                 hotel_atualizado = {"hotel_id": id_hotel, **dados}
                 hotel.update(hotel_atualizado)
                 return hotel, 200
             
        novo_hotel = {"hotel_id" : id_hotel, **dados }
        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, id_hotel):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel["hotel_id"] != id_hotel]
        return {"mesage": f"hotel witch {id_hotel} deleted"}
    
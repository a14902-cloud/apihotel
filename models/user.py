from con_sql import bd

class userModel(bd.Model):
    __tablename__="utilizadores"
    user_id= bd.Column(bd.String, primary_key=True)
    username= bd.Column(bd.String(40))
    password = bd.Column(bd.String(40))
    

    #construtor da classe
    def __init__ (self,username, password):
        self.username = username
        self.password = password

    def json(self):
        return{
            "user_id": self.user_id,
            "username": self.username,
            "password": self.password
        }

    @classmethod
    def find_user (cls, username):
            user = cls.query.filter_by(username=username).first() # 0 ou 1
            # SELECT * FROM hoteis WHERE hotel_id=id_hotel LIMIT 1
            if user:
                return user
            return None


    def save_hotel(self):
            bd.session.add(self)
            bd.session.commit()


    def delete_hotel(self):
            bd.session.delete(self)
            bd.session.commit()

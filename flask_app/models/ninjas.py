from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojos import Dojo

class Ninja():
    db = "dojos_and_ninjas_1"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod 
    def get_all_ninjas(cls):

        query = "SELECT * FROM ninjas;"

        results = connectToMySQL(cls.db).query_db(query)

        ninjas = []

        for ninja in results:
            new_ninja = cls(ninja)
            ninjas.append(new_ninja)
        return ninjas

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s,%(dojo_id)s);"

        results = connectToMySQL(cls.db).query_db(query,data)
        return results
    
    

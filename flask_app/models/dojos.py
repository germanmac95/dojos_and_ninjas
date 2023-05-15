from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninjas




class Dojo():
    db = "dojos_and_ninjas_1"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas_list = []
    
    
    #read
    @classmethod 
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        all_dojos = []

        for dojo in results:
            all_dojos.append(cls(dojo))
        return all_dojos
    
    
    #create
    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"

        results = connectToMySQL(cls.db).query_db(query,data)
        return results

    
    #Read
    @classmethod
    def get_ninja_with_dojo(cls,data):
        query = """
        SELECT * 
        FROM dojos
        LEFT JOIN ninjas on ninjas.dojo_id = dojos.id
        WHERE dojos.id = %(id)s;
        """
        

        results = connectToMySQL(cls.db).query_db(query,data)
        dojo_for_ninja = cls(results[0])
        for row in results:
            ninja_data = {
                "id": row["dojo_id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "age": row["age"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }

            ninja_in_dojo = ninjas.Ninja(ninja_data)
            dojo_for_ninja.ninjas_list.append(ninja_in_dojo)

        return dojo_for_ninja
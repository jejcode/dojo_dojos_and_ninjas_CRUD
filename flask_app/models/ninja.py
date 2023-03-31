#model for dojo table
from flask_app.config.mysqlconnection import connectToMySQL # import database connection function
class Ninja:
    DB = 'dojos_and_ninjas_schema'
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.dojo_name = data['dojo_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #Class methods for CRUD
    # CREATE
    @classmethod
    def create_ninja(cls,data): 
        query = """INSERT INTO ninjas (first_name, last_name, age, dojo_id)
        VALUES (%(fname)s, %(lname)s, %(age)s, %(dojo_id)s)"""
        return connectToMySQL(cls.DB).query_db(query, data) #returns the id of the new record
    # READ
    @classmethod # get one ninja based on id
    def get_one_ninja(cls, ninja_id):
        print('ID:', ninja_id)
        query = "SELECT * FROM ninjas WHERE id=%(id)s"
        results = connectToMySQL(cls.DB).query_db(query, {'id': ninja_id})
        return results[0] # results is a list of one, so return the first item in that list
    @classmethod
    def get_all_ninjas_in_one_dojo(cls, dojo_id):
        query = """SELECT name AS dojo_name, ninjas.id, first_name, last_name, age, dojo_id, ninjas.created_at, ninjas.updated_at FROM dojos
                LEFT JOIN ninjas on dojos.id = ninjas.dojo_id
                where dojos.id=%(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query, {'id': dojo_id})
        print(results)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
    # UPDATE
    @classmethod
    def update_ninja(cls, data): # update ninja record
        query = """UPDATE ninjas
        SET first_name=%(fname)s, last_name=%(lname)s, age=%(age)s, dojo_id=%(dojo_id)s
        WHERE id=%(id)s"""
        return connectToMySQL(cls.DB).query_db(query, data)
    # DELETE
    @classmethod
    def delete_ninja_by_id(cls, ninja_id): # delete row ninja_id from table
        query = """DELETE FROM ninjas WHERE id=%(id)s"""
        return connectToMySQL(cls.DB).query_db(query, {'id': ninja_id})
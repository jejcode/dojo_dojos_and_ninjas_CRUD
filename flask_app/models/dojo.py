#model for dojo table
from flask_app.config.mysqlconnection import connectToMySQL # import database connection function

class Dojo:
    DB = 'dojos_and_ninjas_schema'
    def __init__(self, data) -> None: # each instance models a row from dojo table
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # CRUD class methods
    # CREATE
    @classmethod
    def create_dojo(cls,data): 
        query = """INSERT INTO dojos (name)
        VALUES (%(name)s)"""
        return connectToMySQL(cls.DB).query_db(query, data) #returns the id of the new record
    # READ
    # Read One
    @classmethod
    def get_one_dojo(cls,dojo_id): # gets one record from dojo according to given id
        query = """SELECT * FROM dojos
                WHERE id=%(id)s"""
        results = connectToMySQL(cls.DB).query_db(query,{'id': dojo_id}) # sends id to database and returns a list of 1
        return results[0]
    # Read all
    @classmethod
    def get_all_dojos(cls): # get all dojos from database
        query = "SELECT * FROM dojos ORDER BY name"
        results = connectToMySQL(cls.DB).query_db(query) # sends query to DB
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo)) # creates Dojo instance of each record and adds it to dojos list 
        return dojos
    # UPDATE
    # DELETE
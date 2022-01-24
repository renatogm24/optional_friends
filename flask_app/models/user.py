from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.friends = []
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s, NOW() , NOW() );"
        return connectToMySQL('friendships_schema').query_db( query, data )
    
    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users where users.id = %(id)s;"
        results = connectToMySQL('friendships_schema').query_db(query, data)
        return cls( results[0] )
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('friendships_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

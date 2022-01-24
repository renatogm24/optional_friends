from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import user

class Friendship:
    def __init__( self , data ):
        self.user1 = data['user1']
        self.user2 = data['user2']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO friendships ( user_id , friend_id , created_at, updated_at ) VALUES ( %(user_id)s , %(friend_id)s, NOW() , NOW() );"
        return connectToMySQL('friendships_schema').query_db( query, data )
    
    @classmethod
    def get_friendships(cls):
        query = "SELECT users.id, friends.id, friendships.created_at, friendships.updated_at  FROM users inner join friendships on users.id = friendships.user_id inner join users as friends on friends.id = friendships.friend_id;"
        results = connectToMySQL('friendships_schema').query_db(query)
        friendships = []
        for friendshipAux in results:
            friendship_data = {
                "user1" : user.User.get_user_by_id({"id":friendshipAux["id"]}),
                "user2" : user.User.get_user_by_id({"id":friendshipAux["friends.id"]}),
                "created_at" : friendshipAux["created_at"],
                "updated_at" : friendshipAux["updated_at"],
            }
            friendships.append( cls( friendship_data ) )
        return friendships
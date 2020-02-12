from Database.connection import Connection
from flask_jwt_extended import create_access_token, create_refresh_token


class User:
    def __init__(self):
        self.user_collection = Connection.connect('users')
        self.theater_collection = Connection.connect('theaters')

    def UserRegistration(self, *args):
        result = self.user_collection.count_documents({'username': args[0]})
        result1 = self.user_collection.count_documents({'email': args[1]})
        if result or result1:
            return 0
        inserting = self.user_collection.insert_one({"username": args[0], "email": args[1], "password": args[2], "role": args[3]})
        if inserting.inserted_id:
            return "<p>Registered Successfully</p><small class='text-muted'>" \
                   "<a href = '/login'>Login</a></small>"
        else:
            return "<p>Something Went Wrong Try again</p><small class='text-muted'>" \
                   "<a href = '/register'>Register</a></small>"


    def UserAuthentication(self, *args):
        result = self.user_collection.count_documents({"username": args[0], "password": args[1]})
        if result:
            data = self.user_collection.find_one({"username": args[0]}, {"_id": 0, "email": 0})
            access_token = create_access_token(identity=data, fresh=True)
            refresh_token = create_refresh_token(identity=data)
            return access_token, refresh_token
        else:
            return "There Is No Such User With That Username"

    # def MovieListAndTheaterList(self):
    #     theaterlist =self.theater_collection.find({}, {"theatername": 1, "_id": 0})
    #     movielist = self.theater_colletion.find({}, {""})

    def SeatDetails(self, *args):
        result = self.theater_collection.find_one({"theatername": args[0], "movies.moviename": args[1]},{"movies":1,"theatername":1})
        if result:
            return result
        return 0
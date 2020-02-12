from Database.connection import Connection
from flask import redirect

class Admin:
    def __init__(self):
        self.user_collection = Connection.connect('users')
        self.theater_collection = Connection.connect('theaters')

    def TheaterListData(self):
        result = self.theater_collection.find({}, {"theatername": 1, "_id": 0})
        return result

    def TheaterCreation(self, *args):
        result = self.theater_collection.count_documents({'theatername': args[0]})
        if result:
            return "<p>Already A theater with that name exists</p><small><a href='/theater'>CreateTheater<a></small>"
        # form.theatername.data, form.noofshows.data, form.noofscreens.data, form.screencapacity.data
        inserting = self.theater_collection.insert_one({'theatername': args[0], 'noofshows': args[1], 'noofscreens': args[2], "screencapacity": args[3], 'movies': []})
        if inserting.inserted_id:
            return 0
        else:
            return "<p>Something Went try Again</p><small class= 'text-muted'><a href = '/theater'>CreateTheater</a></small>"

    def AddAMovieToParticularTheater(self, *args):
        result = self.theater_collection.find_one({'theatername': args[0]})
        if result:
            if len(result['movies'])<=result['noofscreens']:
                updatingTheaters = self.theater_collection.update_one({"theatername": args[0]},
                                                                 {
                                                                     "$push": {"movies": {"moviename": args[1],
                                                                                          "availableseats": result['screencapacity'],
                                                                                          "bookedseats": 0,
                                                                                          "inprocessseats": 0
                                                                                          }
                                                                               }
                                                                 }
                                                                      )
            else:
                # All screens are filled
                pass
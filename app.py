from flask_bootstrap import Bootstrap
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from Routes.routes import Main, UserRegister, UserLogin, RedirectingBasedOnRole, AdminPanel, CreateTheater, TheaterList, AddAMovie, Customer

app = Flask(__name__)
Bootstrap(app)
api = Api(app)
app.config['SECRET_KEY'] = '8db93d05e2ff4bb213712ceaf7fadc01'
app.config['JWT_SECRET_KEY'] = 'a14ab99b7478fa6349b591673088b422'
jwt = JWTManager(app)


@jwt.user_claims_loader
def Complex_Object_Token(user):
    return {'user': user}


@jwt.user_identity_loader
def Complex_Object_Username_Identity(user):
    return user['username']


api.add_resource(Main, '/')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(RedirectingBasedOnRole, '/verify')
api.add_resource(AdminPanel, '/admin/')
api.add_resource(CreateTheater, '/theater')
api.add_resource(TheaterList, '/theaterlist')
api.add_resource(AddAMovie, '/addamovie')
api.add_resource(Customer, '/user')



app.run(port=8080, debug=True)

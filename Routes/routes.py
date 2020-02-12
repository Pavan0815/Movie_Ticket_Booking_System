from flask_jwt_extended import jwt_required, get_jwt_claims
from flask_restful import Resource
from flask import make_response, render_template, render_template_string, jsonify, redirect

from Models.adminmodel import Admin
from Models.usermodel import User
from forms import UserRegistrationForm, UserLoginForm, TheaterCreationForm, MovieForm
from werkzeug.security import safe_str_cmp


#/Main
class Main(Resource):
    def get(self):
        return make_response(render_template('base.html'))


#/register
class UserRegister(Resource):

    def get(self):
        form = UserRegistrationForm()
        return make_response(render_template('UserRegistrationForm.html', form=form))

    def post(self):
        form = UserRegistrationForm()
        if form.validate_on_submit():
            u = User()
            returnvalue = u.UserRegistration(form.username.data, form.email.data, form.password.data, 'U')
            if returnvalue:
                return make_response(render_template_string(returnvalue))
            return make_response(render_template_string("<p>There is Already An User With That Username or Email</p>"
                                                        "<small class='text-muted'><a href = '/register'>Register</a></small>"))


#/login
class UserLogin(Resource):

    def get(self):
        form = UserLoginForm()
        return make_response(render_template('UserLoginForm.html', form=form))

    def post(self):
        form = UserLoginForm()
        if form.validate_on_submit():
            u = User()
            returnvalue = u.UserAuthentication(form.username.data, form.password.data)
            if not returnvalue == 'There Is No Such User With That Username':
                return jsonify(Access_token=returnvalue[0], Refresh_token=returnvalue[1])
            return "<p>There Is No Such User With That Username</p><small class='text-muted'><a href = '/login'>Login</a></small>"


# /verify
class RedirectingBasedOnRole(Resource):
    @jwt_required
    def get(self):
        role = get_jwt_claims()['user']['role']
        if safe_str_cmp(role, 'A'):
            return redirect('/admin/')
        elif safe_str_cmp(role, 'U'):
            return redirect('/user')
        else:
            return "UnAuthorized Access", 401


#/admin
class AdminPanel(Resource):
    def get(self):
        print('I am in get')
        return make_response(render_template('Admin/AdminPage.html'))


class TheaterList(Resource):
    def get(self):
        # Display List Of Theaters
        a = Admin()
        returnvalue = a.TheaterListData()
        return make_response(render_template('Admin/TheaterList.html', result=returnvalue))


class CreateTheater(Resource):
    def get(self):
        # Register The Theater Name
        form = TheaterCreationForm()
        return make_response(render_template('Admin/CreatingTheater.html', form=form))

    def post(self):
        form = TheaterCreationForm()
        if form.validate_on_submit():
            a = Admin()
            returnvalue = a.TheaterCreation(form.theatername.data, form.noofshows.data, form.noofscreens.data, form.screencapacity.data)
            if returnvalue:
                return make_response(render_template_string(returnvalue))
            return redirect('/theaterlist')


class AddAMovie(Resource):
    def get(self):
        form = MovieForm()
        return make_response(render_template('Movie.html', form=form, action = '/addamovie'))

    def post(self):
        form = MovieForm()
        if form.validate_on_submit():
            print(form.theatername.data)
            print(form.moviename.data)
            a = Admin()
            returnvalue = a.AddAMovieToParticularTheater(form.theatername.data, form.moviename.data)
            return 1
        return 0

class Customer(Resource):
    def get(self):
        form = MovieForm()
        u = User()
        # returnvalue = u.MovieListAndTheaterList()
        return make_response(render_template('Movie.html', form=form, action ='/user' ))

    def post(self):
        form = MovieForm()
        if form.validate_on_submit():
            u = User()
            returnvalue = u.SeatDetails(form.theatername.data, form.moviename.data)
            if returnvalue:
                print(returnvalue['movies'])
                # return 1
                return make_response(render_template("MovieDetails.html", form=form, data=returnvalue))
        return 0
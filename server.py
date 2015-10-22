"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Rating, Movie, connect_to_db, db

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")

@app.route("/users")
def user_list():
    """Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)


@app.route("/movies")
def movie_list():
    """Show list of users."""

    movies = Movie.query.all()
    return render_template("movie_list.html", movies=movies)

@app.route('/signin')
def signin():
    """Signin."""

    return render_template("signin.html")

@app.route('/process_signin', methods=["POST"])
def process_signin():
    """Signin."""
    username = request.form.get('username')
    password = request.form.get('password')

    # If user table has username in it already:
    #   if password is in same row as username (i.e. it's correct)
    #        say "welcome username"...
    #   else:
    #         say "wrong password"
    #        
    # else: # if the username isn't even in the table
    #        say "invalid login information"
            # try again or new account
    # insert username and password into the table
    
    return password, username

@app.route("/user-add", methods=['POST'])
def user_add():
    """Add a student."""

    github = request.form.get('github')
    first = request.form.get('first')
    last = request.form.get('last')

    hackbright.make_new_student(first, last, github)

    return render_template("student_added.html",
                           github=github)


def make_new_user(username,password):
    """Add a new user and print confirmation.

    Given a username and password, add user to the
    database and print a confirmation message.
    """

    QUERY = """INSERT INTO User VALUES (:username, :password)"""
    db_cursor = db.session.execute(QUERY, {'email': username, 'password': password})
    db.session.commit()
    print "Successfully added user: %s" % (username)




@app.route('/make_account', methods=["POST"])
def make_account():

    email = request.form.get('email')
    password = request.form.get('password')
    age = request.form.get('age')
    zipcode = request.form.get('zipcode')

# to do: insert this data into database


    db.session.add()
    db.session.commit()
    redirect confirm_new_user.html

@app.route('/confirm_new_user')
def confirm_new_user(username):
    

    print "Hey %s You successfully made a new account. " % (username)



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()
"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
# from flask_debugtoolbar import DebugToolbarExtension

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

# same as the first /register
@app.route('/signin') 
def signin():
    """Signin."""
    #flash("testing /signin flash")
    return render_template("signin.html")



@app.route('/process_signin', methods=["POST"])
def process_signin():
    """Signin."""
    username = request.form['username']
    password = request.form['password']
    print username, password
    

    current_user = User.query.filter_by(email=username).first()
    print current_user
    print "whatup"
    

    print "/users/%d" % current_user.user_id
    return redirect("/users/%s" % current_user.user_id)


@app.route("/users/<int:user_id>")
def show_user(user_id):
    """Return page showing the details of a given user.

    Show all info about a user. Also, provide a button to logout.
    """
    print user_id
    # make logout button here ---------------------------

    current_user = User.query.filter_by(user_id=user_id).first()
    print current_user
    return render_template("user_info.html", current_user=current_user)



# same as the second /register
@app.route('/make_account', methods=["POST"])
def make_account():

    email = request.form.get('email')
    password = request.form.get('password')
    age = request.form.get('age')
    zipcode = request.form.get('zipcode')
# to do: insert this data into database

    new_user = User(email=email, password=password, age=age, zipcode=zipcode)

    db.session.add(new_user)
    db.session.commit()

    flash("User %s added." % email)
    return redirect("/")




@app.route('/logout', methods=["POST"])
def logout():
    """Logout."""
    
    pass

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    # app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run()
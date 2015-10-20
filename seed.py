"""Utility file to seed ratings database from MovieLens data in seed_data/"""

import datetime
from model import User
# from model import Rating
from model import Movie

from model import connect_to_db, db
from server import app


def load_users():
    """Load users from u.user into database."""

    print "Users"

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    User.query.delete()

    # Read u.user file and insert data
    for row in open("seed_data/u.user"):
        row = row.rstrip()
        user_id, age, gender, occupation, zipcode = row.split("|")

        users = User(user_id=user_id,
                    age=age,
                    zipcode=zipcode)

        # We need to add to the session or it won't ever be stored
        db.session.add(users)

    # Once we're done, we should commit our work
    db.session.commit()


def load_movies():
    """Load movies from u.item into database."""

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct","Nov","Dec"]
    month_dict = dict(zip(months, range(1,13,1)))

    #Read in u.item and insert data
    for row in open("seed_data/u.item"):
        row = row.strip()
        movie_id, title, released, imdb_url = row.split("|")[0:4]
        movie_id = movie_id[:-7]
        released_day = int(released[0:2])
        released_month = month_dict[released[3:6]]
        released_year = int(released[7:])

        #released_at = datetime.date(released_year, released_month, released_day)
        released_at = datetime.datetime(released_year, released_month, released_day,0,0,0)

        movies = Movie(movie_id=movie_id,
                        title=title,
                        released_at=released_at,
                        imdb_url=imdb_url)

        db.session.add(movies)
    db.session.commit()

def load_ratings():
    """Load ratings from u.data into database."""


if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data
    load_users()
    load_movies()
    load_ratings()

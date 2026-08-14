import os
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
Bootstrap5(app)

load_dotenv()

API_ROOT = "https://api.themoviedb.org/3"
HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.environ.get('API_KEY')}",
}


# CREATE DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    image_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def __repr__(self):
        return f"<Movie '{self.title}'>"


with app.app_context():
    db.create_all()

# with app.app_context():
#     # new_movie = Movie(
#     #     title="Phone Booth",
#     #     year=2002,
#     #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     #     rating=7.3,
#     #     ranking=10,
#     #     review="My favourite character was the caller.",
#     #     image_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg",
#     # )
#     # second_movie = Movie(
#     #     title="Avatar The Way of Water",
#     #     year=2022,
#     #     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     #     rating=7.3,
#     #     ranking=9,
#     #     review="I liked the water.",
#     #     image_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg",
#     # )
#     # db.session.add(second_movie)
#     # db.session.commit()


def get_all_movies():
    with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(Movie.id))
        all_movies = list(result.scalars())
    return all_movies


def get_movie(id, title=None):
    with app.app_context():
        if title is None:
            result = db.session.execute(db.select(Movie).where(Movie.id == id))
        else:
            result = db.session.execute(db.select(Movie).where(Movie.title == title))
        return result.scalar()


def update_movie_rating(id, rating, review):
    with app.app_context():
        movie_to_update = db.session.execute(
            db.select(Movie).where(Movie.id == id)
        ).scalar()
        movie_to_update.rating = rating
        if review is not None:
            movie_to_update.review = review
        db.session.commit()


def delete_movie_rating(id):
    with app.app_context():
        movie_to_delete = db.session.execute(
            db.select(Movie).where(Movie.id == id)
        ).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()


def search_movies(title):
    return requests.get(
        f"{API_ROOT}/search/movie", params={"query": title}, headers=HEADERS
    ).json()


def add_new_movie_to_db(id):
    movie_info = requests.get(f"{API_ROOT}/movie/{id}", headers=HEADERS).json()

    new_movie = Movie(
        title=movie_info["title"],
        year=int(movie_info["release_date"].split("-")[0]),
        description=movie_info["overview"],
        image_url=f"https://image.tmdb.org/t/p/original{movie_info["poster_path"]}",
        rating=0,
        review="",
        ranking=0,
    )
    with app.app_context():
        db.session.add(new_movie)
        db.session.commit()
    return movie_info["title"]


# Edit Movie Rating Form
class RateMovieForm(FlaskForm):
    rating = FloatField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review")
    submit = SubmitField("Save")


# Add New Movie Form
class AddNewMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    return render_template("index.html", movies=get_all_movies())


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    id = request.args.get("id")
    if form.validate_on_submit():
        new_rating = request.form["rating"]
        new_review = request.form["review"]
        if not new_review:
            new_review = None
        update_movie_rating(id, new_rating, new_review)
        return redirect(url_for("home"))
    return render_template("edit.html", movie=get_movie(id), form=form)


@app.route("/delete", methods=["GET"])
def delete():
    id = request.args.get("id")
    delete_movie_rating(id)
    return redirect(url_for("home"))


@app.route("/add_new_movie", methods=["GET"])
def add_new_movie():
    id = request.args.get("id")
    title = add_new_movie_to_db(id)
    id = get_movie(id=None, title=title).id
    return redirect(url_for("edit", id=id))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddNewMovieForm()
    if form.validate_on_submit():
        title = request.form["title"]
        movies = search_movies(title)["results"]
        return render_template("select.html", movies=movies)
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)

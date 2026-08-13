from flask import Flask, render_template, request, redirect, url_for
from config import Config
from flask_sqlalchemy import SQLAlchemy

import sqlalchemy as sa
import sqlalchemy.orm as so

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

all_books = []


class Book(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(250), unique=True, nullable=False)
    author: so.Mapped[str] = so.mapped_column(
        sa.String(250), unique=True, nullable=False
    )
    rating: so.Mapped[float] = so.mapped_column(sa.Float(), nullable=False)

    def items(self):
        return {
            "id": self.id,
            "name": self.name,
            "author": self.author,
            "rating": self.rating,
        }.items()

    def __repr__(self):
        return f"<Books {self.name}>"


all_books = []
total_books = 0


def create_db():
    with app.app_context():
        db.create_all()


def get_all_books():
    global all_books
    global total_books
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.id))
        all_books = list(result.scalars())
    total_books = len(all_books)


@app.route("/")
def home():
    get_all_books()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    global total_books
    if request.method == "POST":
        all_books.append(dict(request.form))
        with app.app_context():
            total_books += 1
            new_book = Book(**request.form, id=total_books)
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for("home"))
    else:
        return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    print(id)
    if request.method == "POST":
        new_rating = request.form["rating"]
        with app.app_context():
            book_to_update = db.session.execute(
                db.select(Book).where(Book.id == id)
            ).scalar()
            if book_to_update:
                book_to_update.rating = new_rating
            db.session.commit()
        return redirect(url_for("home"))
    else:
        return render_template("edit.html", id=id)


if __name__ == "__main__":
    create_db()
    app.run(debug=True)

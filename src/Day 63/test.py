# import sqlite3

# db = sqlite3.connect("books-collection.db")

# cursor = db.cursor()

# # cursor.execute(
# #     "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)"
# # )

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

import sqlalchemy as sa
import sqlalchemy.orm as so

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class Book(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(
        sa.String(250), unique=True, nullable=False
    )
    author: so.Mapped[str] = so.mapped_column(
        sa.String(250), unique=True, nullable=False
    )
    rating: so.Mapped[float] = so.mapped_column(sa.Float(), nullable=False)

    def __repr__(self):
        return f"<Books {self.title}>"


with app.app_context():
    db.create_all()


# with app.app_context():
#     new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()

with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    print(all_books)

with app.app_context():
    book_to_update = db.session.execute(
        db.select(Book).where(Book.title == "Harry Potter")
    ).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

book_id = 1
with app.app_context():
    book_to_update = db.session.execute(
        db.select(Book).where(Book.id == book_id)
    ).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()

book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(
        db.select(Book).where(Book.id == book_id)
    ).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from flask_ckeditor.utils import cleanify
from datetime import datetime, timezone

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)
ckeditor = CKEditor(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def to_dict(self):
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }


# Add New Post Form
class AddNewPostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Blog Post Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    image_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])

    submit = SubmitField("Add Blog Post")


with app.app_context():
    db.create_all()


@app.route("/")
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    all_posts = result.scalars().all()
    posts = [x.to_dict() for x in all_posts]

    return render_template("index.html", all_posts=posts)


@app.route("/show_post/<int:post_id>")
def show_post(post_id):
    result = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id))

    requested_post = result.scalar().to_dict()
    return render_template("post.html", post=requested_post)


@app.route("/new_post/", methods=["GET", "POST"])
def new_post():
    form = AddNewPostForm()
    if form.validate_on_submit():
        # id: Mapped[int] = mapped_column(Integer, primary_key=True)
        #     title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
        #     subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
        #     date: Mapped[str] = mapped_column(String(250), nullable=False)
        #     body: Mapped[str] = mapped_column(Text, nullable=False)
        #     author: Mapped[str] = mapped_column(String(250), nullable=False)
        #     img_url: Mapped[str] = mapped_column(String(250), nullable=False)
        new_post = BlogPost()
        new_post.title = request.form["title"]
        new_post.subtitle = request.form["subtitle"]
        new_post.author = request.form["author"]
        new_post.img_url = request.form["image_url"]
        new_post.date = datetime.now(timezone.utc).date().strftime("%B %m, %Y")
        new_post.body = cleanify(request.form["body"])
        with app.app_context():
            db.session.add(new_post)
            id = (
                db.session.execute(
                    db.select(BlogPost).where(BlogPost.title == new_post.title)
                )
                .scalar()
                .id
            )
            db.session.commit()
        return redirect(url_for("show_post", post_id=id))
    return render_template("make-post.html", form=form)


# TODO: edit_post() to change an existing blog post

# TODO: delete_post() to remove a blog post from the database


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)

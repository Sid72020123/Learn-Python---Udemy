import sqlalchemy as sa
import sqlalchemy.orm as so

from test import db


class Books(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(
        sa.String(250), unique=True, nullable=False
    )
    author: so.Mapped[str] = so.mapped_column(
        sa.String(250), unique=True, nullable=False
    )
    rating: so.Mapped[float] = so.mapped_column(sa.Float(), nullable=False)

    def __repr__(self):
        return f"<Books {self.username}>"

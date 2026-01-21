from datetime import date, datetime
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from base import Base


class Author(Base):
    name: Mapped[str] = mapped_column(unique=True)
    bio: Mapped[str]

    books: Mapped[list["Book"]] = relationship(back_populates="author", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Author {self.name}>"


class Book(Base):
    title: Mapped[str]
    summary: Mapped[str]
    publication_date: Mapped[date]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))

    author: Mapped["Author"] = relationship(back_populates="books")

    def __repr__(self) -> str:
        return f"<Book {self.title}>"


class Tag(Base):
    name: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), default=datetime.now)

    def __repr__(self) -> str:
        return f"<Tag {self.name}>"

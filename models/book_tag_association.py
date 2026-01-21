from sqlalchemy import Table, Column, ForeignKey, Integer, UniqueConstraint
from .base import Base

book_tag_association_table = Table(
    "book_tag_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),  # best practice to have a separate primary key
    Column("book_id", ForeignKey("books.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
    UniqueConstraint("book_id", "tag_id", name="unique_book_tag"),
)

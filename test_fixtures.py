import pytest

from app.models.book import Book
from app import create_app
from app import db

@pytest.fixture
def two_saved_books(app):
    # Arrange
    ocean_book = Book(title="Ocean Book",
                    description="watr 4evr")
    mountain_book = Book(title="Mountain Book",
                        description="i luv 2 climb rocks")

    db.session.add_all([ocean_book, mountain_book])
    db.session.commit()
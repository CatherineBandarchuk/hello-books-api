from flask import Blueprint, jsonify

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
    Book(2, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
    Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
] 

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods = ["GET"])
def get_list_of_books():
    books_list = []
    for book in books:
        books_list.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_list)

@books_bp.route("/<book_id>", methods = ["GET"])
def handle_book(book_id):
    book_id = int(book_id)
    for book in books:
        if book.id == book_id:
            return {
                "id": book.id,
                "title": book.title,
                "description": book.description}
    return {"message":f"book {book_id} not found"}, 404
    
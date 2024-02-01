from flask import make_response, request, jsonify
from app import app, db
from models import User, Book, BookDetails, BorrowedBooks
from datetime import datetime


# initialize tables
@app.route('/inittables', methods=['GET'])
def initTables():
    """
    Endpoint to initialize database tables.
    """
    db.create_all()
    return make_response(jsonify({'message': 'Database Tables created'}), 200)


# create user
@app.route('/api/users', methods=['POST'])
def create_user():
    """
    Endpoint to create a new user.
    """
    try:
        data = request.get_json()
        new_user = User(Name=data['Name'], Email=data['Email'],
                        MembershipDate=datetime.now().date())
        db.session.add(new_user)
        db.session.commit()

        # Return the user details in the response
        user_details = {
            'UserID': new_user.UserID,
            'Name': new_user.Name,
            'Email': new_user.Email,
            'MembershipDate': new_user.MembershipDate.strftime("%Y-%m-%d")
        }

        return make_response(jsonify({'message': 'user created', 'user': user_details}), 201)
    except Exception as e:
        exception_info = str(e)
        print(e)
        return make_response(jsonify({'error': exception_info}), 500)


# get all users
@app.route('/api/users', methods=['GET'])
def get_users():
    """
    Endpoint to retrieve a list of all users.
    """
    try:
        users = User.query.all()
        return make_response(jsonify([user.json() for user in users]), 200)
    except Exception as e:
        exception_info = str(e)
        print(e)
        return make_response(jsonify({'error': exception_info}), 500)


# get a user by id
@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    """
    Endpoint to fetch a user's details using their UserID.
    """
    try:
        user = User.query.filter_by(UserID=id).first()
        if user:
            return make_response(jsonify({'user': user.json()}), 200)
        return make_response(jsonify({'message': 'user not found'}), 404)
    except Exception as e:
        exception_info = str(e)
        print(e)
        return make_response(jsonify({'error': exception_info}), 500)


# Add a book
@app.route('/api/books', methods=['POST'])
def add_book():
    """
    Endpoint to add a new book record.
    """
    try:
        data = request.get_json()
        # changing the json date to python date object
        issueDate = datetime.strptime(data['PublishedDate'], "%Y-%m-%d").date()

        new_book = Book(Title=data['Title'], ISBN=data['ISBN'],
                        PublishedDate=issueDate, Genre=data['Genre'])
        db.session.add(new_book)
        db.session.commit()

        # Return the book details in the response
        book_details = {
            'BookID': new_book.BookID,
            'Title': new_book.Title,
            'ISBN': new_book.ISBN,
            'PublishedDate': new_book.PublishedDate.strftime("%Y-%m-%d"),
            'Genre': new_book.Genre
        }

        return make_response(jsonify({'message': 'New book added', 'book': book_details}), 201)
    except Exception as e:
        exception_info = str(e)
        print(e)
        return make_response(jsonify({'error': exception_info}), 500)


# get all books
@app.route('/api/books', methods=['GET'])
def get_books():
    """
    Endpoint to retrieve a list of all books in the library.
    """
    try:
        books = Book.query.all()
        return make_response(jsonify([book.json() for book in books]), 200)
    except Exception as e:
        exception_info = str(e)
        print(e)
        return make_response(jsonify({'error': exception_info}), 500)


# add book details
@app.route('/api/books/<int:id>/bookdetails', methods=['POST'])
def add_book_details(id):
    """
    Endpoint to add details to a book.
    """
    try:
        data = request.get_json()
        new_book_details = BookDetails(
            BookID=id, NumberOfPages=data['NumberOfPages'], Publisher=data['Publisher'], Language=data['Language'])
        db.session.add(new_book_details)
        db.session.commit()
        # Optionally, you can return a response with the details of the added book details
        book_details_response = {
            'DetailsID': new_book_details.DetailsID,
            'BookID': new_book_details.BookID,
            'NumberOfPages': new_book_details.NumberOfPages,
            'Publisher': new_book_details.Publisher,
            'Language': new_book_details.Language
        }
        return make_response(jsonify({'message': 'New book details added', 'book': book_details_response}), 201)

    except Exception as e:
        exception_info = str(e)
        print(e)
        return make_response(jsonify({'error': exception_info, 'message': 'make sure the json format matches the documentation'}), 500)


# get a book details by id
@app.route('/api/books/<int:id>/bookdetails', methods=['GET'])
def get_book_details(id):
    """
    Endpoint to retrieve details of a specific book using its BookID.
    """
    try:

        # find book by BookID in db
        book = Book.query.filter_by(BookID=id).first()
        book_details = BookDetails.query.filter_by(BookID=id).first()
        if book and book_details:  # if both book and book_details exist in db
            book_response = book.json()
            book_details_response = book_details.json()
            return make_response(jsonify({'book': book_response, 'book_details': book_details_response}), 200)
        elif book and not book_details:  # if only book but no details of book
            book_response = book.json()
            return make_response(jsonify({'book': book_response, 'book_details': 'no book details found'}), 200)
        return make_response(jsonify({'message': 'book not found'}), 404)

    except Exception as e:
        exception_info = str(e)
        print(e)
        return make_response(jsonify({'error': exception_info}), 500)


# update book details
@app.route('/api/books/<int:id>/bookdetails', methods=['PUT'])
def update_book_details(id):
    """
    Endpoint to update details of a specific book using its BookID.
    """
    try:
        book_details = BookDetails.query.filter_by(BookID=id).first()
        if book_details:
            data = request.get_json()

            # if anyone of the fields are empty put value as it was
            book_details.NumberOfPages = data.get(
                'NumberOfPages', book_details.NumberOfPages)
            book_details.Publisher = data.get(
                'Publisher', book_details.Publisher)
            book_details.Language = data.get('Language', book_details.Language)
            db.session.commit()

            # book details json to return
            updated_book_details_response = {
                'DetailsID': book_details.DetailsID,
                'BookID': book_details.BookID,
                'NumberOfPages': book_details.NumberOfPages,
                'Publisher': book_details.Publisher,
                'Language': book_details.Language
            }

            return make_response(jsonify({'message': 'book details updated', 'updated book details': updated_book_details_response}), 200)
        return make_response(jsonify({'message': 'book not found'}), 404)

    except Exception as e:
        exception_info = str(e)
        print(e)
        return make_response(jsonify({'error': exception_info}), 500)


# record book borrowed
@app.route('/api/bookborrow', methods=['POST'])
def record_book_borrowed():
    """
    Endpoint to record the borrowing of a book by linking a user with a book.
    """
    try:
        data = request.get_json()
        new_borrow = BorrowedBooks(BookID=data['BookID'], UserID=data['UserID'],
                                   BorrowDate=datetime.now().date())
        db.session.add(new_borrow)
        db.session.commit()

        # Return the details of book borrowed
        borrow_details_return = {
            'BookID': new_borrow.BookID,
            'UserID': new_borrow.UserID,
            'BorrowDate': new_borrow.BorrowDate.strftime("%Y-%m-%d")
        }

        return make_response(jsonify({'message': 'Book issued Successfully', 'user': borrow_details_return}), 201)
    except Exception as e:
        exception_info = str(e)
        print(e)
        return make_response(jsonify({'error': exception_info}), 500)


# update returned book
@app.route('/api/bookborrow', methods=['PUT'])
def record_book_returned():
    """
    Endpoint to update the system when a book is returned.
    """
    try:
        data = request.get_json()
        returned_book = BorrowedBooks.query.filter_by(
            BookID=data['BookID'], ReturnDate=None).first()
        if returned_book:

            returned_book.ReturnDate = datetime.now().date()
            db.session.commit()

            returned_book_response = {
                'BookID': returned_book.BookID,
                'ReturnDate': returned_book.ReturnDate.strftime("%Y-%m-%d"),
                'UserID': returned_book.UserID,
                'BorrowDate': returned_book.BorrowDate.strftime("%Y-%m-%d")
            }

            return make_response(jsonify({'message': 'Book Returned Successfully', 'updated book details': returned_book_response}), 200)
        return make_response(jsonify({'message': 'this book has not beed issued yet'}), 404)

    except Exception as e:
        exception_info = str(e)
        print(e)
        return make_response(jsonify({'error': exception_info}), 500)


# get all Borrowed Books
@app.route('/api/bookborrow', methods=['GET'])
def get_borrowed_books():
    """
    Endpoint to list all books currently borrowed from the library.
    """
    try:
        data = request.get_json()
        borrowed_books = BorrowedBooks.query.filter_by(
            BookID=data['BookID'], ReturnDate=None).all()
        if borrowed_books:
            return make_response(jsonify([book.json() for book in borrowed_books]), 200)
        return make_response(jsonify({'message': 'No books are currenty issued'}), 404)
    except Exception as e:
        exception_info = str(e)
        print(e)
        return make_response(jsonify({'error': exception_info}), 500)

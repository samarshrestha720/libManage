from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app import db


# User Model
class User(db.Model):
    __tablename__ = 'users'

    UserID = db.Column(Integer, primary_key=True, autoincrement=True)
    Name = db.Column(String(255), nullable=False)
    Email = db.Column(String(255), unique=True, nullable=False)
    MembershipDate = Column(Date)

    # Relationship with BorrowedBooks
    borrowed_books = relationship('BorrowedBooks', backref='user')

    def json(self):
        return {
            'UserId': self.UserID,
            'Name': self.Name,
            'Email': self.Email,
            'MembershipDate': self.MembershipDate
        }


# Book Model
class Book(db.Model):
    __tablename__ = 'books'

    BookID = Column(Integer, primary_key=True, autoincrement=True)
    Title = Column(String(255), nullable=False)
    ISBN = Column(String(20), unique=True, nullable=False)
    PublishedDate = Column(Date)
    Genre = Column(String(50))

    # Relationship with BookDetails
    details = relationship('BookDetails', uselist=False, backref='book')

    def json(self):
        return {
            'BookID': self.BookID,
            'Title': self.Title,
            'ISBN': self.ISBN,
            'PublishedDate': self.PublishedDate.strftime("%Y-%m-%d"),
            'Genre': self.Genre
        }


# BookDetails Model
class BookDetails(db.Model):
    __tablename__ = 'book_details'

    DetailsID = Column(Integer, primary_key=True, autoincrement=True)
    BookID = Column(Integer, ForeignKey('books.BookID'), unique=True)
    NumberOfPages = Column(Integer)
    Publisher = Column(String(255))
    Language = Column(String(50))

    def json(self):
        return {
            'DetailsID': self.DetailsID,
            'BookID': self.BookID,
            'NumberOfPages': self.NumberOfPages,
            'Publisher': self.Publisher,
            'Language': self.Language
        }

    # Relationship with Book
    # book = relationship('Book', back_populates='details')


# BorrowedBooks Model
class BorrowedBooks(db.Model):
    __tablename__ = 'borrowed_books'

    BorrowedID = Column(Integer, primary_key=True, autoincrement=True)
    BookID = Column(Integer, ForeignKey('books.BookID'), nullable=False)
    BorrowDate = Column(Date, nullable=False)
    ReturnDate = Column(Date)
    UserID = Column(Integer, ForeignKey('users.UserID'), nullable=False)

    def json(self):
        return {
            'BorrowedID': self.BorrowedID,
            'BookID': self.BookID,
            'BorrowDate': self.BorrowDate.strftime("%Y-%m-%d"),
            'ReturnDate': self.ReturnDate.strftime("%Y-%m-%d") if self.ReturnDate else 'book still in issue',
            'UserID': self.UserID
        }

    # # Relationship with User
    # user = relationship('User', backref='borrowed_books')

    # # Relationship with Book
    # book = relationship('Book', back_populates='borrowed_books')

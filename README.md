
# Library Management System RestAPI

A Library Management System RestAPI using flask and SQLite


## Setup
Follow the steps to initialize the project.

Step 1: Cloning the Repositoy to your local machine using a terminal or cmd

Step 2: cd libManage or open the folder in VsCode.

step 3: Create a virtual environment using `python -m venv venv` in the terminal

step 4: Activate the virtual environment using `.\venv\Scripts\activate` in the terminal. Once you see the (env) in the terminal, the virtual environment has beed activated.

step 5: Install all requirements in the requirements.txt by using `pip install -r requirements.txt`

*Skip to step 10 if you want to use the existing db with already loaded data.

step 6: Delete the `lib.db` inside the instance folder

step 7: Start flask server by using `python run.py` in the terminal

step 8: Create tables by using the given url by flask in the terminal and adding `/inittables` 
eg: `http://127.0.0.1:5000/inittables`
expected result: `'message': 'Database Tables created'`

step 9: Stop flask server by using Ctrl+C in the terminal

step 10: Start flask server by using `python run.py` in the terminal

step 11: Use postman or other software to test the api

## Documentation

* *Create User:* Endpoint to create a new user:
    `POST /api/users` eg:`http://127.0.0.1:5000/api/users`
Payload:
`{
  "Name": "John Doe",
  "Email": "john.doe@example.com"
}
`
* *Get All Users:* Endpoint to retrieve details of all users:
    `GET /api/users`
    eg: `http://127.0.0.1:5000/api/users`

* *Get User by ID:* Endpoint to retrieve details of a specific user by UserID.
    `GET /api/users/{UserID:int}` eg: `http://127.0.0.1:5000/api/users/1`
* *Add a book:* `POST /api/books`
Payload: `{
    "Title": "Programming",
    "ISBN": "112333aa321das1",
    "PublishedDate":"2009-06-08",
    "Genre":"Edu"
}`

* *Add book details:* `POST /api/books/{BookID:int}/bookdetails`
eg: `http://127.0.0.1:5000/api/books/1/bookdetails`
Payload: `{
    "NumberOfPages": 300,
    "Publisher": "Test Publisher 1",
    "Language": "English"
}`

* *Get all books:* `GET /api/books`

* *Get a book details by id:* `GET /api/books/{BookID:int}/bookdetails` eg:`http://127.0.0.1:5000/api/books/1/bookdetails` 


* *Update book details:* `PUT /api/books/{BookID:int}/bookdetails`   eg: `http://127.0.0.1:5000/api/books/1/bookdetails` 
Payload: `{
    "Language": "Nepali",
    "NumberOfPages": 800,
    "Publisher" : "Abc Publisher"
}`

* *Record book borrowed:* `POST /api/bookborrow`
eg: `http://127.0.0.1:5000/api/bookborrow`
Payload: `{
    "BookID": 1,
    "UserID": 1
}`

* *Update returned book:* `PUT /api/bookborrow`
eg: `http://127.0.0.1:5000/api/bookborrow`
Payload: `{
    "BookID": 2
}`

* *Get all Borrowed Books:* `GET /api/bookborrow`
eg: `http://127.0.0.1:5000/api/bookborrow`

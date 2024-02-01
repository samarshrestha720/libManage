
# Library Management System RestAPI

A Library Management System RestAPI using Flask and SQLite


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

[Documentation](https://linktodocumentation)


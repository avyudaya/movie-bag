## User can crud Genre, Movie, and Casts.

### Technologies Used:

- Flask - For our web server.
- flask-restful - For building cool Rest-APIs.
- Pipenv For managing python virtual environments.
- mongoengine - For managing our database.
- flask-marshmallow - For serializing user requests.
- Postman - For testing our APIs
- Flask-Bcrypt For hashing user password
- Flask-JWT-Extended For creating tokens for authorization and authentication.

## Getting started:
`
pip install --user pipenv
python -m pipenv shell
python -m pipenv install
`

# Setting env file location
1. Create a .env file by following .env.example 
2. On Linux: export ENV_FILE_LOCATION=./.env
3. On Windows: set ENV_FILE_LOCATION=./.env

### STEPS:
1. Creating a basic CRUD API
2. Adding Mongodb
3. Better structure with blueprint and flask-restful
4. Authentication and Authorization
5. Exception handling
6. Password reset
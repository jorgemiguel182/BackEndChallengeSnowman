# BackEndChallengeSnowman

> <p> <a href="https://gitlab.com/snowman-labs/backend-challenge"> Link do desafio </a> </p> 
> <p> <a href="https://snowmanapi.herokuapp.com/swagger/"> Link Heroku</a> </p> 


**Tecnologias usadas**

- Python (Django/Django Rest Framework)
- PostgreSQL
- Docker
- Heroku

---

## Table of Contents 

- [Installation](#installation)
- [Tests](#tests)
- [Auth](#auth)
- [Swagger](#swagger)
- [Deploy](#deploy)

---

## Installation

- All the `code` required to configure locally and in docker

### Clone

- Clone this repo to your local machine 
```shell
$> git clone https://github.com/jorgemiguel182/BackEndChallengeSnowman
$> cd BackEndChallengeSnowman
```

### Setup Locally or with Docker (Tested on Windows)

##### - **Local**
- In the cloned project directory, with python, pip and virtualenv installed, create a virtual environment:

```shell
$ virtualenv venv
$ cd venv/Scripts
$ activate
$(venv) cd ..
$(venv) cd ..
```
- Install dependencies
```shell
$(venv) pip install -r requirements.txt
```
- Create a file .env in root project directory to store your local variables.
- Run Migrations
```shell
$(venv) python manage.py migrate --settings SnowManAPI.settings.local
```
- Start server
```shell
$(venv) python manage.py runserver --settings SnowManAPI.settings.local
```
- Enjoy!

##### - Docker - COM PROBLEMAS
- In the cloned project directory, with docker installed, first create a file .env in root project directory, and after
```shell
$ docker-compose up --build -d
```

- To stop docker instances

```shell
$ docker-compose down -v
```

---

## Tests
- Run the tests to make sure everything is ok!
- After installation, run this command
```shell
$ python manage.py test apps --settings SnowManAPI.settings.local
```


## Auth
- In this project, a simple authentication method was used. Simple token-based HTTP Authentication.
You must use the token in the HTTP Authorization header like this "Authorization: Token 123token123token ...", replace 
"123token12..." with the token value


### Register/Signup
- Endpoint > http://127.0.0.1:8000/api/auth/new
    - Method: POST
    - Data {"username": "STRING","password": "STRING","email": "STRING"}
### Get a Token to pass in Header HTTP > Authorization
- Endpoint > http://127.0.0.1:8000/api/auth/token
    - Method: POST
    - Data {"username": "STRING","password": "STRING"}





## Swagger Documentation
- Access the link
    - http://127.0.0.1:8000/swagger/
## Deploy

heroku run python manage.py migrate
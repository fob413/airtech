<p align="center">
  <img src="https://github.com/fob413/airtech/blob/master/api/utils/airtech.png?raw=true">
</p>

Airtech is a flight booking system that allows users of the platform to book flights and pay for tickets.

# Features
* A user can create an account and log into the app
* A user can upload his passport photographs
* A user can make flight reservations
* A user can make payment for their flight ticket and receive the ticket as an email
* A user can check the status of their flight
* A user receives an email notification a day before about their upcoming fligh
# Technology Stack
* [Python3](https://www.python.org/download/releases/3.0/): Python is an interpreted, high-level, general-purpose programming Language. See the [source](https://www.python.org/download/releases/3.0/) for installation guide.
* [Virtualenv](https://virtualenv.pypa.io/en/latest/): Virtualenv is a tool to create isolated Python environments. See the [source](https://virtualenv.pypa.io/en/latest/) for installation guide.
* [Pip](https://pypi.org/project/pip/): Pip is the package installer for python. Pip is used to install packages from the Python Package Index and other indexes. See the [source](https://pypi.org/project/pip/) for installation guide.
* [Flask](http://flask.pocoo.org/): Flask is a microframework for python. It is focused on simplicity and minimalism, leaving the developer with the freedom of choice in terms of modules and add-ons. See the [source](http://flask.pocoo.org/) for installation guide.
* [Postgresql](https://www.postgresql.org/): Postgresql is a powerful, open source object-relational database system. Postgresql 10 (or above) is used to build this project. See the [source](https://www.postgresql.org/) for installation guide.

# Installation
* Clone this repo and navigate into the project's directory
```git clone https://github.com/fob413/airtech.git && cd airtech```
* Ensure you have the followign installed. Click for installation guide
    - [Python3](https://www.python.org/download/releases/3.0/)
    - [Virtualenv](https://virtualenv.pypa.io/en/latest/)
    - [Pip](https://pypi.org/project/pip/)
    - [Postgresql](https://www.postgresql.org/)
* Create a `python3` virtual environment for the project and activate it
```mkvirtualenv --python=python3 airtech && workon airtech```
* Install the projects requirements
```pip install -r requirements.txt```
* Create a `.env` file which contains the following
```
- FLASK_ENV
- DATABASE_URL
- JWT_SECRET_KEY
```
* Export the environment variables in the .env
```export $(cat .env)```
* Run the app
```python app.py```

# Contributing
Feel free to dive in. Open an issue to request for a bug fix or additional feature or submit PRs. To contribute:
- Fork this repository
- Create your feature branch on your local macine: `git checkout -b your-feature-branch`
- Commit your changes: `git commit -m'Add my feature'`
- Push your branch online: `git push origin your-feature-branch`
- Open a pull request to the develoment branch and describe how your feature works

Refer to this wiki for the preferred [GIT workflow](https://github.com/andela/bestpractices/wiki).

Ensure your code follows [PEP 8](https://www.python.org/dev/peps/pep-0008/) Style Guide.

# Author
Oluwafunso Oluyole-Balogun

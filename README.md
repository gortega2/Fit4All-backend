# Step-by-step instructions to run the project

1.) Install the latest version of Python for your system OS (https://www.python.org/downloads/) and make sure that Python is added to PATH.

2.) Make sure that pip is also added to PATH as well. (https://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command)

3.) Once pip and python are added to PATH, run in the terminal
```
pip install pipenv --user
```
4.) In the terminal, navigate to the directory of where the projects' Pipfile and Pipfile.lock are located

5.) Run the commands in sequental order
```
pipenv shell
```
```
pipenv install
```
6.) Create an .env files in accordance to the .env.sample file

7.) Make sure that the values in the .env file match the MySQL database values

8.) Once all the pipenv dependencies are installed, run the command
```
python manage.py loaddata seed.json
```
9.) To run the server, run the command
```
python manage.py runserver
```

10.) If there are any unapplied migrations, run the commands
```
python manage.py makemigrations
```
```
python manage.py migrate
```
11.) The database should be up and running with no problems


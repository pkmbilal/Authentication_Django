
# User Authentication

This is a small user authentication project based on Django. I have used builtin authenticate, login, logout modules. All views written in this project are completely my logic. I have used tailwindcss to style the html pages. Go through this project and let me know your comment via social channels. Happy Coding :)


## Authors

- [@pkmbilal](https://github.com/pkmbilal) [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pkmbilal/)


## Documentation

- Initially create a folder with any name and clone project to that folder using below command

```bash
  git clone https://github.com/pkmbilal/Authentication_Django.git
```

- If Git is not installed in your system, you can download the project folder as zip format with the below link.

```bash
  https://github.com/pkmbilal/Authentication_Django.git
```

- Create a virtual environment in the main folder(Not inside actual project folder).

```bash
pip install virtualenv
```
```bash
python<version> -m venv <virtual-environment-name>
```

- Then activate the virtual environment with the below command (Windows).

```bash
cd mainproject_folder_name/<virtual-environment-name>/Scripts
./activate
```

- Once the evnironment is activated, install the dependencies using the below command.

```bash
pip install -r requirements.txt
```

- I have used MySQL as database. Install MySQL and create a database named **authentication**.

- Change the database option in settings.py file as below. Replace the user, password with the your MySQL user & password. 

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'authentication',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost'
    }
}
```
- Once the above settings done use the below command to create necessay tables in the new database.

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
- After that create a super user to access the admin area. Choose any username, password and email for superadmin.

```bash
python manage.py createsuperuser
```
- Finally run the live server

```bash
python manage.py runserver
```
- By clicking the http://127.0.0.1:8000/ you can open the project in your browser.
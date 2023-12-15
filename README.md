# Blog App
This project is a client-server Web application built over an RDBMS. It's an application that runs on a portal site, in which different users can publish and revise daily journal entries, and these entries will be made public for others to view.


## Installation

Clone the repository
```bash
git clone https://github.com/ChetanSureka/blog-app
cd blog-app
```
## Run Locally

Install the dependencies
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Migrate the changes to database
```bash
python manage.py makemigrations
python manage.py migrate
```

Create a super user(admin)
```bash
python manage.py createsuperuser
```

Start a development web server at localhost:8000
```bash
python manage.py runserver
```
## Screenshots

![App Screenshot](https://github.com/ChetanSureka/blog-app/blob/main/img1.png)


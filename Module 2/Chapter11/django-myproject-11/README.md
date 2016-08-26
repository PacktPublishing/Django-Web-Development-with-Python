This is an example project for the chapter "Testing and Deployment" of the book "Web Development with Django Cookbook - Second Edition" by Aidas Bendoraitis.


To install requirements run:
pip install -r requirements.txt

To start, run the development server:
$ python manage.py runserver

To login to administration, use username "admin" and password "admin".

To test the recipe "Creating filterable RSS feeds", open:
http://127.0.0.1:8000/bulletin-board/

To test the recipe "Using Django REST Framework to create API", open:
http://127.0.0.1:8000/rest-api/bulletin-board/
http://127.0.0.1:8000/rest-api/bulletin-board/1/
(try with and without authentication)
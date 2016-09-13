This is an example project for the chapter "Data Import and Export" of the book "Web Development with Django Cookbook - Second Edition" by Aidas Bendoraitis.


To install requirements run:
pip install -r requirements.txt

To start, run the development server:
$ python manage.py runserver

To login to administration, use username "admin" and password "admin".

To test the recipe "Importing from local CSV file", run
$ python manage.py import_movies_from_csv data/movies.csv

To test the recipe "Importing from local XLS file", run
$ python manage.py import_movies_from_xls data/movies.xls

To test the recipe "Import from external JSON", run
$ python manage.py import_music_from_lastfm_as_json

To test the recipe "Import from external XML", run
$ python manage.py import_music_from_lastfm_as_xml

To test the recipe "Creating filterable RSS feeds", open:
http://127.0.0.1:8000/bulletin-board/

To test the recipe "Using Tastypie to provide data to third parties", open:
http://127.0.0.1:8000/api/v1/bulletins/?format=json&username=admin&api_key=3e79ed2e5acecf4843af9f7df8f0395f45733b28

To test the recipe "Using Django REST Framework to create API", open:
http://127.0.0.1:8000/rest-api/bulletin-board/
http://127.0.0.1:8000/rest-api/bulletin-board/1/
(try with and without authentication)
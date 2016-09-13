This is an example project for the chapter "Hierarchical Structures" of the book "Web Development with Django Cookbook - Second Edition" by Aidas Bendoraitis.


To install requirements run:
pip install -r requirements.txt

To login to administration, use username "admin" and password "admin".

To see recipes in action, run the development server:
$ python manage.py runserver

To test the recipes "Setting up administration for your categories with django-mptt-admin" and "Setting up administration for your categories with django-mptt-tree-editor" go to
http://127.0.0.1:8000/admin/movies/category/
To switch between the two administrations, comment out one or another administration setting in movies/admin.py

To test the recipe "Rendering categories in a template" go to
http://127.0.0.1:8000/movies/categories/

To test the recipe "Using single selection field for choosing a category in forms" go to
http://127.0.0.1:8000/movies/

To test the recipes "Using checkbox list for choosing multiple categories in forms" go to
http://127.0.0.1:8000/movies/add/
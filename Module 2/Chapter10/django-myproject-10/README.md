This is an example project for the chapter "Bells and Whistles" of the book "Web Development with Django Cookbook - Second Edition" by Aidas Bendoraitis.


To install requirements run:
pip install -r requirements.txt

To start, run the development server:
$ python manage.py runserver

To login to administration, use username "admin" and password "admin".

To test the recipe "Using database query expressions", open:
http://127.0.0.1:8000/en/viral-videos/1/

To test the recipe "Toggling debug toolbar", open any page, e.g.
http://127.0.0.1:8000/en/viral-videos/1/

To see the recipe "Using ThreadLocalMiddleware" in action, save a chosen book in administration:
http://127.0.0.1:8000/admin/books/book/
Current user will be saved as the creator of the book.

To read the code for the recipe "Detailed error reporting by email", open conf/base.py

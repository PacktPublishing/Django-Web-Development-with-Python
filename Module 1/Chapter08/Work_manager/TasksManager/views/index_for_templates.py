# -*- Coding: utf-8 -*-
from django.shortcuts import render
"""
View for index page. 
"""

def page(request):
	my_variable = "Hello World !"
	my_hello = "hello WORLD"
	years_old = 15
	nb_products = 1
	nb_diaries = 2
	variable1 = '<script type="text/javascript">alert("variable1");</script>'
	variable2 = '<script type="text/javascript">alert("variable2");</script>'
	variable3 = '<script type="text/javascript">alert("variable3");</script>'
	variable4 = '<script type="text/javascript">alert("variable4");</script>'
	variable5 = '<script type="text/javascript">alert("variable5");</script>'
	text = 'Welcome in Django'
	array_city_capitale = [ "Paris", "London", "Washington" ]
	return render(request, 'en/public/index.html', { "my_var":my_variable, "years":years_old, "array_city":array_city_capitale, "my_hello":my_hello, "nb_products":nb_products, "nb_diaries":nb_diaries, "variable1":variable1, "variable2":variable2, "variable3":variable3, "variable4":variable4, "variable5":variable5, "text":text })
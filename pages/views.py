from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
	# return HttpResponse("<h1>Hello You!</h1>")
	return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})


def social_view(request, *args, **kwargs):
	return render(request, "social.html", {})


def about_view(request, *args, **kwargs):
	my_context = {
		"title": "this is about us",
		"my_number": 123,
		"my_list": [123, 556, 478, 312],
		"my_html": "<h1>Hello There!!!</h1>"

	}
	return render(request, "about.html", my_context)
"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

"""
from pages import views - tak nie powinno sie importowac widokow (ze wzgledu
na to, ze kazda dodana apka ma swoje wlasne widoki o tej samej nazwie).
"""

# Lepiej importowac w taki sposob:
from pages.views import home_view, contact_view, social_view, about_view


urlpatterns = [
	path('', home_view, name='home'),		# zamiast views.home_view
	path('home/', home_view, name='home'),	# 'home/' odpowiada za podadres strony
    path('contact/', contact_view),
    path('social/', social_view),
    path('about/', about_view),
    path('admin/', admin.site.urls),
]

"""quote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^groups/', )
    url(r'^members/', )
    url(r'^create_group/', )
    url(r'^add_members/', )
    url(r'^delete_members/', )
    url(r'^login/', )
    url(r'^post_quote/', )
    url(r'^guess_quote/', )
    url(r'^delete_quote/', )
    url(r'^new_user/', )
    url(r'^show_guesses/', )
    url(r'^show_posts/', )
    url(r'^unguessed_quotes/', )


    
               
               
               
               
               
               
               
]

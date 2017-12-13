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
    url(r'^groups/(?P<user_id>[0-9]+/$)', views.groups, name = 'groups'),
    url(r'^members/(?P<group_id>[0-9]+/$)', views.members, name = 'members'),
    url(r'^create_group/$', views.create_group, name = 'create_group'),
    url(r'^add_members/$', views.add_members, name = 'add_members'),
    url(r'^delete_members/$', views.delete_members, name = 'delete_members'),
    url(r'^login/$', views.login, name = 'login'),
    url(r'^post_quote/$', views.post_quote, name = 'post_quote'),
    url(r'^guess_quote/(?P<post_id>[0-9]+)/$', views.guess_quote, name = 'guess_quote'),
    url(r'^delete_quote/(?P<post_id>[0-9]+)/$', views.delete_quote, name = 'delete_quote'),
    url(r'^new_user/$', views.new_user, name = 'new_user'),
    url(r'^show_guesses/(?P<user_id>[0-9]+)/$', views.show_guesses, name = 'show_guesses'),
    url(r'^show_posts/(?P<user_id>[0-9]+)/$', views.show_posts, name = 'show_posts'),
    url(r'^unguessed_quotes/(?P<user_id>[0-9]+)/$', views.unguessed_quotes, name = 'unguessed_quotes')
           
]

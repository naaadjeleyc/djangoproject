
from django.conf.urls import include, url

from todo_list import views

urlpatterns = [
    url('', views.home, name='home'),
]
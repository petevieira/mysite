# zengo/urls.py
from django.conf.urls import url
from zengo import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]
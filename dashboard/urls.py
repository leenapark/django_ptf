from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name="chart"),
    path("post/", views.post_api, name="post"),
]
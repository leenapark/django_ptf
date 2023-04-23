from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard),
    path("post/", views.post_api, name="post")
]
from django.urls import path
from . import views

# my endpoints
urlpatterns = [
    path("", views.index, name="index"),
    path("helloAccountName/", views.helloAccountName, name="helloAccountName"),
    path("addFive/<int:accountID>", views.addFive, name="addFive"),
]
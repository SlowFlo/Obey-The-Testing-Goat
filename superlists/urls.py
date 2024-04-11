from django.urls import path

from lists import views
from lists.views import home_page

urlpatterns = [
    path("", home_page, name="home"),
    path("lists/the-only-list-in-the-world/", views.view_list, name="view_list"),
]

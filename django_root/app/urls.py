from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("homepage/", views.homepage, name="homepage"),
    path("singleview/", views.singleview, name="singleview"),
    path("login/", views.login_user, name="login"),
]

urlpatterns += staticfiles_urlpatterns()

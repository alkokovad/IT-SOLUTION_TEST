from django.urls import path
from . import views


urlpatterns = [
    path('', views.StringGeneratorView.as_view(), name="string_gen"),
]
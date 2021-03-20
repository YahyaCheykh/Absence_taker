from django.urls import path
from . import views
urlpatterns = [
    path('', views.welcome_page),
    path('create_school', views.create_school),
    path('log_in', views.log_in),
    path('create_school_logic', views.create_school_logic)
]

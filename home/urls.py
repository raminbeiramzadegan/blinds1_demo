from django.urls import path,include
from . import views
app_name = 'home'
urlpatterns = [
    path('',views.homepage,name = 'home'),
]
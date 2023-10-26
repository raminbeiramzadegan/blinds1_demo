from django.urls import path
from . import views
app_name = "accounts"
urlpatterns = [

    path('sign_in/',views.SignInView.as_view(),name="sign_in"),
    path('sign_up/',views.SignUpView.as_view(),name="sign_up"),
    # path('sign_in/',views.sign_in,name="sign_in"),

    path('logout/',views.LogoutView.as_view(),name="logout"),


]
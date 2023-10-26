from django.urls import path, re_path
from . import views

app_name = 'dashboard'

urlpatterns = [

    path('<int:id>/',views.Dashboard.as_view(),name='dashboard'),
    path('profile/<int:id>/',views.profile,name='profile'),
    path('edit_profile/<int:id>/',views.UserProfileUpdate.as_view(),name="edit_profile"),
    path('addressbook/<int:id>/',views.address_book,name='address_book'),
    path('create_address/<int:id>', views.AddNewAddress.as_view(), name='create_address'),
    path('edit_address/<int:id>', views.AddressUpdate.as_view(),name = 'edit_address')

]
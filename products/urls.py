from django.urls import path,include
from . import views
app_name = 'products'
urlpatterns = [
    path('',views.ProductsList.as_view(),name = 'product_list'),
    path('<slug:slug>/',views.ProductDetailView.as_view(),name = 'product_detail'),

    
]
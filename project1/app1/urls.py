from django.urls import path
from . import views


urlpatterns = [
    path('ao/', views.addOrder, name='add_url'),
    path('so/', views.showOrder, name='show_url'),
    path('uo/<int:pk>/', views.updateOrder, name='update_url'),
    path('do/<int:pk>/', views.deleteOrder, name='delete_url'),
    path('index/', views.index, name='index_url')
]
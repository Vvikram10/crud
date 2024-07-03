# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('contact_list', views.contact_list, name='contact_list'),
    path('', views.contact_create, name='contact_create'),
    path('update/<int:id>/', views.contact_update, name='contact_update'),
    path('delete/<int:id>/', views.contact_delete, name='contact_delete'),
]

from django.urls import path
from . import views #current directory import views
from myapp_person import views #similar to the above



urlpatterns=[
    path('', views.person_list, name='person_list'),
    path('create/', views.person_create, name='person_create'),
    path('delete/<int:pk>/', views.person_delete, name='person_delete'),
]
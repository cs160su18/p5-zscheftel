from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('groups/', views.groups, name='groups'),
    # path('activity/',views.activity, name='activity'),
    path('formpage/', views.formpage, name='formpage'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_student_info/',views.add_student_info,name ='add_student_info')
    
]
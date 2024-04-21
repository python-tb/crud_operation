

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('show_student',views.show_student,name='show_student'),
    path('add_student',views.add_student,name='add_student'),
    path('update_student/<int:pk>',views.update_student,name='update_student'),
    path('delete_student/<int:pk>',views.delete_student,name='delete_student'),
]

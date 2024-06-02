from django.urls import path 
from .import views

urlpatterns = [
    path('',views.add_musician, name = 'musician'),
    path('edit/<int:id>/',views.edit_music, name = 'edit_musician'),
    path('delete/<int:id>/',views.delete_music, name = 'delete_musician'),
    

]

from django.urls import path
from . import views


app_name="notes"


urlpatterns = [
    path("", views.home, name='home'),
    path("notes/", views.note_list, name='note_list'),
    path("notes/<int:pk>/", views.note_detail, name='note_detail'),
    path("notes/new/", views.note_create, name = 'note_create'),
    path("notes/<int:pk>/edit/", views.note_update, name = 'note_update'),
    path("notes/<int:pk>/delete/", views.note_delete, name = 'note_delete')
    
]
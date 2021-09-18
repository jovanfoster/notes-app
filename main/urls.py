from django.urls import path
from .views import index, NoteCreateView, NoteUpdateView, NoteDeleteView, login_view, logout_view, register

urlpatterns = [
    path('', index, name='index'),
    path('note/add/', NoteCreateView.as_view(), name='note-create'),
    path('note/<int:pk>/', NoteUpdateView.as_view(), name='note-update'),
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
]

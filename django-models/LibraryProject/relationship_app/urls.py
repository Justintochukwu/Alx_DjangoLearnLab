from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # This is needed for views.register and views.list_books
from .views import (
    admin_view,
    librarian_view,
    member_view,
    LibraryDetailView,
)

urlpatterns = [
    # Book and library views
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Role-based views
    path('admin-area/', admin_view, name='admin_view'),
    path('librarian-area/', librarian_view, name='librarian_view'),
    path('member-area/', member_view, name='member_view'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]


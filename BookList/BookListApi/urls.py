from django.urls import path
from . import views

urlpatterns = [
    #path('books', views.books),
    path('books/', views.BookList),
    #path('category/', views.CreateCategory.as_view()),  Comment - 1, ref serializers.py file
    path('books/<int:pk>', views.SingleBook),
]
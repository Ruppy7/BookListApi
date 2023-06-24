from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('secret/', views.secret),
    #path('books', views.books),
    path('books/', views.BookList),
    #path('category/', views.CreateCategory.as_view()),  Comment - 1, ref serializers.py file
    path('books/<int:pk>', views.SingleBook),
    path('book-items/', views.BookItemsViewSet.as_view({'get':'list'})),
    path('book-items/<int:pk>', views.BookItemsViewSet.as_view({'get':'retrieve'})),
]
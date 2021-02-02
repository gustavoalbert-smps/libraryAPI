from django.urls import path, include

from booksApp import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas.openapi import SchemaGenerator

schema_view = get_swagger_view(title="LIBRARY API Documentation")

urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('api-documentation/', schema_view),
    path('api-auth/', include('rest_framework.urls')),
    path('login/token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('users/', views.UserList.as_view(), name=views.UserList.name),
    path('books/', views.BookList.as_view(), name=views.BookList.name),
    path('books/<int:pk>/', views.BookDetail.as_view(), name=views.BookDetail.name),
    path('bookscategory/', views.BooksCategoryList.as_view(), name=views.BooksCategoryList.name),
    path('bookscategory/<int:pk>/', views.BooksCategoryDetail.as_view(), name=views.BooksCategoryDetail.name),
    path('author-list/', views.AuthorList.as_view(), name=views.AuthorList.name),
    path('author/<int:pk>', views.AuthorDetail.as_view(), name=views.AuthorDetail.name),
    path('librarians/', views.LibrarianList.as_view(), name=views.LibrarianList.name),
    path('librarians/<int:pk>/', views.LibrarianDetail.as_view(), name=views.LibrarianDetail.name),
    path('client-list/', views.ClientList.as_view(), name=views.ClientList.name),
    path('client/<int:pk>/', views.ClientDetail.as_view(), name=views.ClientDetail.name),
    path('rents/', views.RentList.as_view(), name=views.RentList.name),
    path('rents/<int:pk>/', views.RentDetail.as_view(), name=views.RentDetail.name),
]

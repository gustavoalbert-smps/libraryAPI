from django.shortcuts import render
from django.contrib.auth.models import User
from django_filters import NumberFilter, DateTimeFilter, AllValuesFilter

from rest_framework.parsers import JSONParser
from rest_framework import status, generics, permissions, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.throttling import ScopedRateThrottle

from booksApp.models import BooksCategory, Book, Author, Librarian, Client, Rent
from booksApp.serializers import *

from datetime import datetime

import pytz

utc = pytz.UTC

#booksCategory
class BooksCategoryList(generics.ListCreateAPIView):
    queryset = BooksCategory.objects.all()
    serializer_class = BooksCategorySerializer
    name = 'bookscategory-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',)

class BooksCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BooksCategory.objects.all()
    serializer_class = BooksCategorySerializer
    name = 'bookscategory-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#author
class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = 'author-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = 'author-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#book
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('name','available','publication','book_author','book_category')
    search_fields = ('^name',)
    ordering_fields = ('name','publication',)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#Librarian
class LibrarianList(generics.ListCreateAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
    name = 'librarian-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_scope = 'private'
    throttle_classes = (ScopedRateThrottle,)

class LibrarianDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
    name = 'librarian-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_scope = 'private'
    throttle_classes = (ScopedRateThrottle,)

#Client
class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_scope = 'private'
    throttle_classes = (ScopedRateThrottle,)

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_scope = 'private'
    throttle_classes = (ScopedRateThrottle,)

#Rent
class RentList(generics.ListCreateAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    name = 'rent-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_scope = 'private'
    throttle_classes = (ScopedRateThrottle,)
    filter_fields = ('start_date','end_date','return_date','book','client','librarian')
    search_fields = ('^book')
    ordering_fields = ('start_date','return_date','book')

    def post(self, request, *args, **kwargs):
        book = Book.objects.get(name=self.request.data['book'])
        client = Client.objects.get(name=self.request.data['client'])
        librarian = Librarian.objects.get(name=self.request.data['librarian'])
        if book.available == False:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            data = {'end_date':self.request.data['end_date'],'return_date':self.request.data['return_date'],'book':book,'client':client,'librarian':librarian}
            book.available = False
            book.save()
            if data['return_date'] == None or data['return_date'] == '':
                e_date = str(self.request.data['end_date'])+'-0300'
                end_date = datetime.strptime(e_date,'%Y-%m-%dT%H:%M%z')
                book1 = Book.objects.get(name=self.request.data['book'])
                client1 = Client.objects.get(name=self.request.data['client'])
                librarian1 = Librarian.objects.get(name=self.request.data['librarian'])
                rent = Rent(end_date=end_date,return_date=None,book=book1,client=client1,librarian=librarian1)
                rent.save()
            else:
                e_date = str(self.request.data['end_date'])+'-0300'
                end_date = datetime.strptime(e_date,'%Y-%m-%dT%H:%M%z')
                r_date = str(self.request.data['return_date']+'-0300')
                return_date = datetime.strptime(r_date, '%Y-%m-%dT%H:%M%z')
                rent = Rent(end_date=end_date,return_date=return_date,book=book,client=client,librarian=librarian)
                rent.save()
            serializer = RentSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)

class RentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    name = 'rent-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_scope = 'private'
    throttle_classes = (ScopedRateThrottle,)

#Users
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_scope = 'private'
    throttle_classes = (ScopedRateThrottle,)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_scope = 'private'
    throttle_classes = (ScopedRateThrottle,)    

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'books': reverse(BookList.name, request=request),
            'author': reverse(AuthorList.name, request=request),
            'booksCategory': reverse(BooksCategoryList.name, request=request),
            'librarians': reverse(LibrarianList.name, request=request),
            'clients': reverse(ClientList.name, request=request),
            'users': reverse(UserList.name, request=request),
        })
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
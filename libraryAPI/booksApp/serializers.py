from django.contrib.auth.models import User

from rest_framework import serializers
from booksApp.models import BooksCategory, Book, Author, Librarian, Client, Rent

class BooksCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BooksCategory
        fields = ('url', 'pk', 'name')

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('pk', 'name','age', 'sex')

class BookSerializer(serializers.HyperlinkedModelSerializer):
    book_author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='name')
    book_category = serializers.SlugRelatedField(queryset=BooksCategory.objects.all(), slug_field='name')

    class Meta:
        model = Book
        fields = ('pk', 'name', 'available', 'publication', 'book_author', 'book_category')

class LibrarianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Librarian
        fields = ('pk', 'name', 'age', 'sex', 'phone')

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('pk', 'name', 'age', 'sex', 'phone', 'CPF')

class RentSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field='name')
    client = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='name')
    librarian = serializers.SlugRelatedField(queryset=Librarian.objects.all(), slug_field='name')
    
    class Meta:
        model = Rent
        fields = ('pk', 'start_date', 'end_date', 'return_date', 'book', 'client', 'librarian')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username','last_login')
from django.db import models

# Create your models here.
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

class BooksCategory(models.Model):
    name = models.CharField(max_length=75)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=75)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    publication = models.DateTimeField()
    book_author = models.ForeignKey(Author, related_name='authors', on_delete=models.CASCADE)
    book_category = models.ForeignKey(BooksCategory, related_name='categories', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=75)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.IntegerField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=75)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.IntegerField()
    CPF = models.IntegerField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Rent(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True)
    return_date = models.DateTimeField(null=True)
    book = models.ForeignKey(Book, related_name='books', on_delete=models.CASCADE)
    client = models.OneToOneField(Client, related_name='clients', unique=False, db_constraint=False, on_delete=models.CASCADE)
    librarian = models.OneToOneField(Librarian, related_name='librarians', unique=False, db_constraint=False, on_delete=models.CASCADE)
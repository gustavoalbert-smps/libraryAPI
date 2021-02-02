# Generated by Django 3.1.5 on 2021-01-28 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booksApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='booksApp.client'),
        ),
        migrations.AlterField(
            model_name='rent',
            name='librarian',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='librarians', to='booksApp.librarian'),
        ),
    ]

# Generated by Django 3.1.5 on 2021-02-02 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksApp', '0004_auto_20210128_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
    ]

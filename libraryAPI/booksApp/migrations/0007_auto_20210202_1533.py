# Generated by Django 3.1.5 on 2021-02-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksApp', '0006_auto_20210202_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='return_date',
            field=models.DateTimeField(null=True),
        ),
    ]

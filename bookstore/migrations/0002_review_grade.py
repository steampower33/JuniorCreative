# Generated by Django 3.0.2 on 2020-01-18 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='grade',
            field=models.IntegerField(default=5),
        ),
    ]
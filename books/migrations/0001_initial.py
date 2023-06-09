# Generated by Django 4.2 on 2023-04-18 06:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('author', models.CharField(max_length=200, verbose_name='author')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='price')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
            },
        ),
    ]

# Generated by Django 2.1.7 on 2019-06-24 18:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

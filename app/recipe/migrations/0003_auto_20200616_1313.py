# Generated by Django 3.0.7 on 2020-06-16 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20200612_1340'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ingredient',
            unique_together={('name', 'recipe')},
        ),
    ]

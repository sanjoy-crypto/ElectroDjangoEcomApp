# Generated by Django 3.2.8 on 2021-10-26 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contactmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmessage',
            name='ip',
        ),
    ]

# Generated by Django 4.2.2 on 2023-12-10 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_comment_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]

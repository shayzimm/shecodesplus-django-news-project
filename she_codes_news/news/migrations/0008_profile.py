# Generated by Django 4.2.2 on 2023-12-10 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
# Generated by Django 4.1 on 2022-10-21 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='moviesinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('image', models.CharField(max_length=122)),
                ('release_year', models.TextField()),
            ],
        ),
    ]

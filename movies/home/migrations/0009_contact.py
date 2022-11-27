# Generated by Django 4.1 on 2022-11-21 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_moviesinfo_size1080p_moviesinfo_size480p_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('decs', models.TextField(blank=True, default='#', null=True)),
            ],
        ),
    ]
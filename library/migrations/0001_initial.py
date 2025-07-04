# Generated by Django 3.0.5 on 2025-03-29 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import library.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=20, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment', models.CharField(max_length=15, unique=True)),
                ('branch', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IssuedBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('expiry_date', models.DateField(default=library.models.get_expiry)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.StudentExtra')),
            ],
        ),
        migrations.CreateModel(
            name='ToReadList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.StudentExtra')),
            ],
            options={
                'unique_together': {('student', 'book')},
            },
        ),
    ]

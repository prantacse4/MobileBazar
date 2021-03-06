# Generated by Django 3.2.3 on 2021-05-25 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('name', models.CharField(max_length=50)),
                ('location', models.TextField(default=None)),
                ('phone', models.CharField(default=None, max_length=50, unique=True)),
                ('image', models.ImageField(upload_to='uploaded_image/user')),
            ],
        ),
    ]

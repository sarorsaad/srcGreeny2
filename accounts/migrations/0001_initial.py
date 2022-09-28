# Generated by Django 3.2 on 2022-09-27 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import utlis.generate_code


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=30)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='users/')),
                ('type', models.CharField(choices=[('Home', 'Home'), ('Office', 'Office'), ('Academy', 'Academy'), ('Other', 'Other')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_phone', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=30)),
                ('note', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('street', models.CharField(max_length=80)),
                ('type', models.CharField(choices=[('Home', 'Home'), ('Office', 'Office'), ('Academy', 'Academy'), ('Other', 'Other')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='users/')),
                ('code', models.CharField(default=utlis.generate_code.generate_code, max_length=10)),
                ('code_used', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

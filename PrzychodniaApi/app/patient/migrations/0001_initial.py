# Generated by Django 5.0.1 on 2024-01-13 19:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('second_name', models.CharField(blank=True, max_length=120, null=True)),
                ('last_name', models.CharField(max_length=120)),
                ('pesel', models.CharField(max_length=12)),
                ('birth_date', models.DateField()),
                ('phone_number', models.CharField(max_length=9)),
                ('city', models.CharField(max_length=120)),
                ('street', models.CharField(max_length=120)),
                ('house_number', models.CharField(max_length=120)),
                ('zip_code', models.CharField(max_length=6)),
            ],
            options={
                'abstract': False,
            },
            bases=('user.user',),
        ),
    ]
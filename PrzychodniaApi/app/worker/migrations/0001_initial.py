# Generated by Django 5.0.1 on 2024-01-14 15:51

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
            name='Doctor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('employment_status', models.CharField(choices=[('active', 'Active'), ('on_leave', 'On Leave'), ('inactive', 'Inactive')], default='active', max_length=10)),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('phone_number', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=120)),
                ('street', models.CharField(max_length=120)),
                ('house_number', models.CharField(max_length=10)),
                ('zip_code', models.CharField(max_length=10)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='static/images/profile_images')),
                ('specialization', models.CharField(max_length=120)),
                ('room_number', models.CharField(max_length=10, verbose_name='Room Number')),
            ],
            options={
                'abstract': False,
            },
            bases=('user.user',),
        ),
    ]

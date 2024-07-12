# Generated by Django 5.0.4 on 2024-05-31 06:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        ('user_reg', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=50)),
                ('servName', models.CharField(max_length=50)),
                ('servType', models.CharField(max_length=50)),
                ('servDesc', models.CharField(max_length=50)),
                ('servPriority', models.CharField(max_length=50)),
                ('uploadfile', models.ImageField(upload_to='image/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='user_reg.user_reg')),
            ],
        ),
    ]

# Generated by Django 5.0.4 on 2024-07-10 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0003_user_reg_groups_user_reg_is_active_user_reg_is_staff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_reg',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='user_reg',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user_reg',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='user_reg',
            name='phoneNumber',
        ),
        migrations.RemoveField(
            model_name='user_reg',
            name='user_permissions',
        ),
        migrations.AddField(
            model_name='user_reg',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('CUSTOMER', 'Customer'), ('MECHANIC', 'Mechanic')], default='CUSTOMER', max_length=10),
        ),
        migrations.AlterField(
            model_name='user_reg',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user_reg',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]

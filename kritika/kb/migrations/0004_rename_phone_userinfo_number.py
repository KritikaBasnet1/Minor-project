# Generated by Django 5.0.1 on 2024-02-20 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kb', '0003_rename_confirmpassword_userinfo_confirm_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='phone',
            new_name='number',
        ),
    ]

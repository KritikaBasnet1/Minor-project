# Generated by Django 4.1.7 on 2024-01-23 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kb', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

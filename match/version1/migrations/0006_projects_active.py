# Generated by Django 3.1.3 on 2023-12-10 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('version1', '0005_auto_20231210_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]

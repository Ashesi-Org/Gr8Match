# Generated by Django 3.1.3 on 2023-12-07 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('version1', '0002_auto_20231206_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='version1.customuser'),
            preserve_default=False,
        ),
    ]

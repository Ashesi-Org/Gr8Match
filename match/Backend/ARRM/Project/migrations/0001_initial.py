# Generated by Django 4.2.7 on 2023-12-04 02:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('anulled', 'Anulled')], default='pending', max_length=20)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('visibility', models.CharField(choices=[('public', 'public'), ('private', 'private')], default='private', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectStudyArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_area', models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Algorithm', 'Algorithm'), ('Computer Engineering', 'Computer Engineering'), ('Cryptography', 'Cryptography'), ('Robotics', 'Robotics'), ('Computer Vision', 'Computer Vision'), ('Software Engineering', 'Software Engineering'), ('Computational Science', 'Computational Science'), ('Numerical Analysis', 'Numerical Analysis'), ('Market Research', 'Market Research'), ('Financial Accounting', 'Financial Accounting'), ('International Trade & Policy', 'International Trade & Policy'), ('Organisational Behaviour', 'Organisational Behaviour'), ('Managerial Behaviour', 'Managerial Behaviour'), ('Marketing', 'Marketing'), ('Operations Management', 'Operations Management'), ('International Finance', 'International Finance'), ('Supply-Chain Management', 'Supply-Chain Management'), ('Business Law', 'Business Law'), ('Competitive Strategy', 'Competitive Strategy'), ('Corporate Finance', 'Corporate Finance'), ('Product Development', 'Product Development')], max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.project')),
            ],
        ),
    ]
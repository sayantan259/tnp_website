# Generated by Django 5.0.2 on 2024-04-13 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_userdetails_linkedin_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shared_company',
            old_name='student_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='shared_hr_contact',
            old_name='student_id',
            new_name='user',
        ),
    ]

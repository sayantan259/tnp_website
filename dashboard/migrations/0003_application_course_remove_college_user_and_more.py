# Generated by Django 5.0.2 on 2024-02-29 18:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_college_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predicted_visit_date', models.DateField(blank=True, null=True)),
                ('twelfth_marks_eligibility', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('tenth_marks_eligibility', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('job_description', models.TextField(blank=True, null=True)),
                ('is_spp', models.BooleanField(blank=True, null=True)),
                ('is_sip', models.BooleanField(blank=True, null=True)),
                ('twelfth_gap', models.IntegerField(blank=True, null=True)),
                ('graduation_gap', models.IntegerField(blank=True, null=True)),
                ('backlogs', models.IntegerField(blank=True, null=True)),
                ('graduation_marks', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('current_cgpa', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(choices=[('B.Tech', 'Bachelor of Technology'), ('B.E', 'Bachelor of Engineering'), ('M.Tech', 'Master of Technology'), ('M.E', 'Master of Engineering'), ('BCA', 'Bachelor of Computer Applications'), ('MCA', 'Master of Computer Applications'), ('B.Sc', 'Bachelor of Science'), ('M.Sc', 'Master of Science')], max_length=20)),
                ('specialization', models.CharField(max_length=100)),
                ('course_duration', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='college',
            name='user',
        ),
        migrations.CreateModel(
            name='AppliedCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_selected', models.CharField(choices=[('applied', 'Applied'), ('rejected', 'Rejected')], default='applied', max_length=10)),
                ('comment', models.TextField(blank=True, null=True)),
                ('application_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.application')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CollegeCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.college')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.course')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='college_branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.collegecourse'),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_intern', models.BooleanField(blank=True, null=True)),
                ('is_ppo', models.BooleanField(blank=True, null=True)),
                ('is_fte', models.BooleanField(blank=True, null=True)),
                ('general_ctc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('college_ctc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('time_of_visit', models.DateField(blank=True, null=True)),
                ('history', models.JSONField(blank=True, null=True)),
                ('college_branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='dashboard.collegecourse')),
                ('poc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='poc_company', to='dashboard.collegecourse')),
                ('allowed_courses', models.ManyToManyField(blank=True, to='dashboard.course')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='company_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.company'),
        ),
        migrations.AddField(
            model_name='application',
            name='allowed_branch',
            field=models.ManyToManyField(blank=True, to='dashboard.course'),
        ),
        migrations.CreateModel(
            name='HRContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('mail_id', models.EmailField(blank=True, max_length=254, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('date_of_contact', models.DateField(blank=True, null=True)),
                ('assigned', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_hr', to=settings.AUTH_USER_MODEL)),
                ('college_branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.collegecourse')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.company')),
                ('reassigned', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reassigned_hr', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CallHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('colour', models.CharField(blank=True, choices=[('red', 'Red'), ('blue', 'Blue'), ('yellow', 'Yellow'), ('green', 'Green')], max_length=10, null=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('college_branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.collegecourse')),
                ('hr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.hrcontact')),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='user_resumes/')),
                ('photo', models.ImageField(upload_to='user_photos/')),
                ('backlogs', models.IntegerField()),
                ('graduation_marksheet', models.FileField(upload_to='user_marksheets/')),
                ('graduation_cgpa', models.DecimalField(decimal_places=2, max_digits=4)),
                ('twelfth_marksheet', models.FileField(upload_to='user_marksheets/')),
                ('twelfth_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tenth_marksheet', models.FileField(upload_to='user_marksheets/')),
                ('tenth_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('current_cgpa', models.DecimalField(decimal_places=2, max_digits=4)),
                ('other_website_link', models.TextField()),
                ('leetcode_profile', models.URLField()),
                ('codechef_profile', models.URLField()),
                ('codeforces_profile', models.URLField()),
                ('github_profile', models.URLField()),
                ('portfolio_link', models.URLField()),
                ('department', models.CharField(max_length=100)),
                ('gap_after_twelfth', models.IntegerField(default=0)),
                ('gap_after_graduation', models.IntegerField(default=0)),
                ('mobile', models.CharField(max_length=15)),
                ('is_placed', models.BooleanField(default=False)),
                ('college_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.collegecourse')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

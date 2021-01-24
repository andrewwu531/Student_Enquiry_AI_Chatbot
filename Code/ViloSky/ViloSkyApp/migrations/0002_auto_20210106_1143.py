# Generated by Django 3.1.4 on 2021-01-06 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ViloSkyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('static_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_vilosky_admin', models.BooleanField(default=False)),
                ('is_hr_representative', models.BooleanField(default=False)),
                ('date_of_birth', models.DateField(null=True)),
                ('company', models.CharField(max_length=255, null=True)),
                ('employment_sector', models.CharField(max_length=255, null=True)),
                ('employment_status', models.CharField(max_length=255, null=True)),
                ('time_worked_in_industry', models.DurationField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=255)),
                ('time_spent_on_page', models.DurationField()),
                ('clicks_on_page', models.PositiveIntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraphs', models.ManyToManyField(related_name='reports_included_in', to='ViloSkyApp.Paragraph')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports_assigned', to='ViloSkyApp.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=255)),
                ('subjects', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qualifications', to='ViloSkyApp.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='paragraph',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paragraphs_created', to='ViloSkyApp.userprofile'),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('paragraph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='ViloSkyApp.paragraph')),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('score', models.IntegerField()),
                ('paragraph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keywords', to='ViloSkyApp.paragraph')),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('is_completed', models.BooleanField(default=False)),
                ('paragraph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='ViloSkyApp.paragraph')),
            ],
        ),
    ]

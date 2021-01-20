# Generated by Django 3.1.4 on 2021-01-20 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ViloSkyApp', '0003_auto_20210118_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='is_completed',
        ),
        migrations.CreateModel(
            name='UserAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('is_completed', models.BooleanField(default=False)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_actions', to='ViloSkyApp.report')),
            ],
        ),
    ]

# Generated by Django 3.0.8 on 2020-07-18 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduleclassmodel',
            name='id',
        ),
        migrations.AddField(
            model_name='scheduleclassmodel',
            name='course_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]
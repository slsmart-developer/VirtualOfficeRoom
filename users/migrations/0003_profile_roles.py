# Generated by Django 4.0.5 on 2022-07-01 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='roles',
            field=models.CharField(choices=[('CEO', 'CEO'), ('Director', 'Director'), ('Manager', 'Project Manager'), ('Tech_lead', 'Tech Lead'), ('Senior_developer', 'Senior Developer'), ('Developer', 'Developer')], max_length=50, null=True),
        ),
    ]

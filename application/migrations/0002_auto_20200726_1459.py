# Generated by Django 3.0.8 on 2020-07-26 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Message',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Subject',
            new_name='subject',
        ),
    ]

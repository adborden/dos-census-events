# Generated by Django 2.2.1 on 2019-05-11 20:04

import census.constants
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title or short description of the event', max_length=100)),
                ('description', models.TextField(help_text='Full description of the event')),
                ('start_datetime', models.DateTimeField(help_text='When does this event start?')),
                ('end_datetime', models.DateTimeField(help_text='When does the event end?')),
                ('organization_name', models.CharField(help_text='Name of the hosting organization', max_length=100)),
                ('event_type', models.CharField(choices=[(census.constants.EventType('Workshop'), 'Workshop'), (census.constants.EventType('Tabling'), 'Tabling'), (census.constants.EventType('Celebration'), 'Celebration'), (census.constants.EventType('Drop-in center'), 'Drop-in center'), (census.constants.EventType('Other'), 'Other')], max_length=2)),
                ('location', models.CharField(help_text='Location where the event will take place', max_length=100)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('is_census_equipped', models.BooleanField(help_text='Is this event technologically equipped to allow people to take the census?')),
                ('approval_status', models.CharField(choices=[(census.constants.EventApprovalStatus('Pending'), 'Pending'), (census.constants.EventApprovalStatus('Approved'), 'Approved')], max_length=2)),
            ],
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-10 20:51

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0008_auto_20191110_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='languages',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('ENGLISH', 'English'), ('SPANISH', 'Spanish'), ('VIETNAMESE', 'Vietnamese'), ('CHINESE', 'Chinese'), ('TAGALOG', 'Tagalog')], help_text='Add languages supported at the event', max_length=42),
        ),
    ]

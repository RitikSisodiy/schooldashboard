# Generated by Django 3.2 on 2021-04-26 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmain', '0002_schoocontact'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolifo',
            name='Name',
            field=models.CharField(default='school name', max_length=500),
            preserve_default=False,
        ),
    ]

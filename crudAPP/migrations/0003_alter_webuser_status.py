# Generated by Django 3.2.3 on 2021-07-29 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudAPP', '0002_webuser_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webuser',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 3.2.3 on 2021-08-04 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudAPP', '0010_auto_20210804_0340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webuser',
            name='key',
        ),
        migrations.AddField(
            model_name='webuser',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
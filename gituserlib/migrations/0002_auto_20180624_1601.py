# Generated by Django 2.0.6 on 2018-06-24 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gituserlib', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
    ]
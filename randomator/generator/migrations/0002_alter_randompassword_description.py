# Generated by Django 4.0.6 on 2022-07-31 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='randompassword',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
# Generated by Django 2.1.5 on 2019-02-22 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdetailss',
            name='modified_at',
            field=models.DateTimeField(),
        ),
    ]

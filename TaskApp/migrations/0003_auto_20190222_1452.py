# Generated by Django 2.1.5 on 2019-02-22 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApp', '0002_auto_20190222_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdetailss',
            name='modified_at',
            field=models.DateTimeField(null=True),
        ),
    ]
# Generated by Django 3.2.13 on 2022-11-19 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_auto_20221120_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='qna',
            name='hits',
            field=models.PositiveIntegerField(default=0, verbose_name='조회수'),
        ),
    ]
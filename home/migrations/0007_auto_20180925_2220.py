# Generated by Django 2.1.1 on 2018-09-25 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_nyc311record_community_board_relation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityboard',
            name='name',
            field=models.TextField(),
        ),
    ]

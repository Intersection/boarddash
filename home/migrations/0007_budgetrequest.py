# Generated by Django 2.1.1 on 2018-09-25 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_nyc311record_community_board_relation'),
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.CharField(max_length=255)),
                ('boro', models.CharField(max_length=255)),
                ('explanation', models.TextField()),
                ('priority', models.CharField(max_length=255)),
                ('request', models.CharField(max_length=255)),
                ('responded_by', models.CharField(max_length=255)),
                ('response', models.TextField()),
                ('responsible_agency', models.CharField(max_length=255)),
                ('tracking_code', models.CharField(max_length=255)),
            ],
        ),
    ]

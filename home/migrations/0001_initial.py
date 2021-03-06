# Generated by Django 2.1.1 on 2018-09-25 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NYC311Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(max_length=255)),
                ('agency', models.CharField(max_length=255)),
                ('agency_name', models.CharField(max_length=255)),
                ('borough', models.CharField(choices=[('MANHATTAN', 'Manhattan'), ('BROOKLYN', 'Brooklyn'), ('BRONX', 'Bronx'), ('STATEN ISLAND', 'Staten Island'), ('QUEENS', 'Queens')], max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('community_board', models.CharField(max_length=255)),
                ('complaint_type', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField()),
                ('cross_street_1', models.CharField(max_length=255)),
                ('cross_street_2', models.CharField(max_length=255)),
                ('descriptor', models.CharField(max_length=255)),
                ('facility_type', models.CharField(max_length=255)),
                ('incident_address', models.CharField(max_length=255)),
                ('incident_zip', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('location_type', models.CharField(max_length=255)),
                ('open_data_channel_type', models.CharField(max_length=255)),
                ('resolution_description', models.TextField()),
                ('status', models.CharField(max_length=255)),
                ('street_name', models.CharField(max_length=255)),
                ('unique_key', models.CharField(max_length=255)),
            ],
        ),
    ]

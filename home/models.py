from django.db import models
from django.template.defaultfilters import slugify


class CommunityBoard(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    chair = models.TextField(null=True)
    district_manager = models.TextField(null=True)
    address = models.TextField(null=True)
    phone_number = models.TextField(null=True)
    email_address = models.TextField(null=True)
    website = models.TextField(null=True)
    board_meeting = models.TextField(null=True)
    cabinet_meeting = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug

class NYC311Record(models.Model):
    BOROUGHS = (
        ('MANHATTAN', 'Manhattan'),
        ('BROOKLYN', 'Brooklyn'),
        ('BRONX', 'Bronx'),
        ('STATEN ISLAND', 'Staten Island'),
        ('QUEENS', 'Queens'),
    )

    address_type = models.CharField(max_length=255)
    agency = models.CharField(max_length=255)
    agency_name = models.CharField(max_length=255)
    borough = models.CharField(max_length=255, choices=BOROUGHS)
    city = models.CharField(max_length=255)
    community_board = models.CharField(max_length=255)
    community_board_relation = models.ForeignKey(CommunityBoard, null=True, on_delete=models.SET_NULL)
    complaint_type = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    cross_street_1 = models.CharField(max_length=255)
    cross_street_2 = models.CharField(max_length=255)
    descriptor = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=255)
    incident_address = models.CharField(max_length=255)
    incident_zip = models.CharField(max_length=255)
    latitude = models.DecimalField(decimal_places=6, max_digits=10, null=True)
    longitude = models.DecimalField(decimal_places=6, max_digits=10, null=True)
    location_type = models.CharField(max_length=255)
    open_data_channel_type = models.CharField(max_length=255)
    resolution_description = models.TextField()
    status = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    unique_key = models.CharField(max_length=255)

    def __str__(self):
        return '%s: %s' % (self.unique_key, self.descriptor)

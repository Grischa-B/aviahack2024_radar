# stats/urls.py

from django.urls import path
from .influxdb_client import create_record, read_records_by_date, update_record

urlpatterns = [
    path('create/', create_record, name='create_record'),
    path('read_by_date/', read_records_by_date, name='read_records_by_date'),
    path('update/', update_record, name='update_record'),
]

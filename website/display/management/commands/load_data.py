import os
import requests
import csv
from ...models import unsplash_photos
from ...serializers import UnsplashPhotosSerializer

from django.core.management.base import BaseCommand

#names of files to read from

photos_tsv='/website/display/management/commands/photos.tsv000'

class Command(BaseCommand):
    load_data = 'Loads data to unsplash db'

    #read and save collections data
    def handle(self, *args, **options):
        with open(photos_tsv, 'r') as tsv_in:
            tsv_reader = csv.reader(tsv_in, delimiter='\t')
            next(tsv_reader)
            for data in tsv_reader:
                try:
                    self.stdout.write('{} by {} added to db succesfully :-)'.format(data[0], data[9]))
                    unsplash_photos.objects.get_or_create(
                                                            photo_id=data[0],
                                                            photo_url=data[1], 
                                                            photo_image_url=data[2], 
                                                            photo_width=data[5],
                                                            photo_height=data[6],
                                                            photo_aspect_ratio=data[7],
                                                            photo_description=data[8],
                                                            photographer_first_name=data[10],
                                                            photographer_last_name=data[11],
                                                            photo_location_country=data[21],	
                                                            photo_location_city=data[22],
                                                            tagged=False
                                                            )

                except:
                    self.stdout.write('{} by {} already exists in the DB :-)'.format(data[0], data[9]))
                    

import json
import pandas as pd
from django.core.management.base import BaseCommand
from star.models import Restaurant, Item


class Command(BaseCommand):
    help = 'Load restaurant data from CSV file'

    def handle(self, *args, **kwargs):
        file_path = 'restaurants_small.csv'
        data = pd.read_csv(file_path)

        for _, row in data.iterrows():
            restaurant = Restaurant(
                id=row['id'],
                name=row['name'],
                location=row['location'],
                lat_long=row['lat_long'],
                full_details=row['full_details']
            )
            restaurant.save()

            items = json.loads(row['items'])
            for item_name, item_price in items.items():
                item = Item(
                    restaurant=restaurant,
                    name=item_name,
                    price=str(item_price.strip())
                )
                item.save()
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded restaurant data'))

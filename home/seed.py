from faker import Faker
fake = Faker()
import random
from .models import *

def seed_db(n=10) -> None:
    try:
        for i in range(0,n):
            hotel_name = fake.name()
            hotel_price = random.randint(5000, 10000)
            description = fake.text()
            hotel_place = fake.city()
            room_count = 10
            
            hotel_obj = Hotel.objects.create(
                hotel_name = hotel_name,
                hotel_price = hotel_price,
                description = description,
                hotel_place = hotel_place,
                room_count = room_count
               
            )

    except Exception as e:
        print(e)
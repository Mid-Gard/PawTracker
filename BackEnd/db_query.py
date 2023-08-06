# https://docs.djangoproject.com/en/3.0/topics/migrations/#data-migrations
# https://www.edureka.co/community/73739/django-script-access-model-objects-without-using-manage-shell 
import os
import django
#setting up django env
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

# importing models
from location.models import Bus1_data,Bus2_data,Bus3_data,Bus4_data

#api format for bus_location
# [{"id": 1, "lat": 12.9771191896563, "lng": 77.5857120256672, "bearing": 0.0, "status": "out campus"}, {"id": 2, "lat": 12.9771191896563, "lng": 77.5857120256672, "bearing": 0.0, "status": "out campus"}, {"id": 3, "lat": 12.9771191896563, "lng": 77.5857120256672, "bearing": 0.0, "status": "out campus"}, {"id": 4, "lat": 12.9771191896563, "lng": 77.5857120256672, "bearing": 0.0, "status": "out campus"}]


def save_in_db(data):
    print('inside save db')
    bus_data = []
    for i in data: 
        bus_data.append(list(i.values()))

    print(f'****************************{bus_data[0][2]}')
    #putting data in tables(models)    
    b_tables = []
    
    b_tables.append(Bus1_data(bus1_lat= bus_data[0][1], bus1_lng = bus_data[0][2],bus1_time='null', bus1_date = 'null',bus1_speed = 0 ))
    b_tables.append(Bus2_data(bus2_lat= bus_data[1][1], bus2_lng = bus_data[1][2], bus2_time='null',bus2_date = 'null', bus2_speed = 0 ))
    b_tables.append(Bus3_data(bus3_lat= bus_data[2][1], bus3_lng = bus_data[2][2], bus3_time='null',bus3_date = 'null', bus3_speed = 0 ))
    b_tables.append(Bus4_data(bus4_lat= bus_data[3][1], bus4_lng = bus_data[3][2], bus4_time='null',bus4_date = 'null', bus4_speed = 0 ))

    #saving changes to the database
    for table in b_tables:
        table.save()


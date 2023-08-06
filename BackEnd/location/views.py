from db_query import *
from django.shortcuts import render
import json
import math
from django.http import HttpResponse, JsonResponse
import random
import requests
import time
from geopy.distance import geodesic

# this module is for importing the bus id
#from driver_details.models import bus_details

# Global CONSTANT
API_KEY = ["api key1", "api key2", "api key3", "api key4"]
# from ..location.models import LocationData
# this module is for importing the bus id
#from driver_details.models import bus_details

# ----------for pushing data to database---------------------
# import os
# import django
# import sys
# sys
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
# django.setup()

# from ..location.models import LocationData

# ---------------------------------------------------------------------
# Global CONSTANT
API_KEY = ["api key1", "api key2", "api key3", "api key4"]
API_URL = "https://61a4a0604c822c0017041d33.mockapi.io/shuttle/v1/path"



def bus_incampus(request):
    # -------------------------------Testing---------------------------------
    # generating random data
    #  adding bus status
    Gec_clk_coordinates = (15.422249402831747, 73.98014018286432)
    coordnew = getloc()
    for i in range(4):
        status=[]
        if (geodesic(Gec_clk_coordinates,(coordnew[i][0],coordnew[i][1]) ).meters <= 235):
            status = "In campus"
            
        else:
            status = "out campus"
    data = [
        {
            "id": 1,
            "busNumber": f"ABC{random.randint(100,999)}",
            "departureTime": f"({random.uniform(1.0000, 12.0000):.4f}, {random.uniform(1.0000, 12.0000):.4f})",
            "arrivalTime": f"{random.randint(1,12)},{random.randint(10,59)} {random.choice(['AM', 'PM'])}",
            "Status":status
        },
        {
            "id": 2,
            "busNumber": f"XYZ{random.randint(100,999)}",
"departureTime": f"({random.uniform(1.0000, 12.0000):.4f}, {random.uniform(1.0000, 12.0000):.4f})",
            "arrivalTime": f"{random.randint(1,12)}:{random.randint(10,59)} {random.choice(['AM', 'PM'])}",
            "Status":status
        }
    ]
    # -------------------------------Testing---------------------------------
    return HttpResponse(json.dumps(data), content_type="application/json")


def bus_outcampus(request):
    # -------------------------------Testing---------------------------------
    return HttpResponse("GA 02 G 7455")


# this function will call the api, rn it calls dummy api
def getloc():
    coord = []
    global API_KEY, API_URL
    for key in API_KEY:
        response = requests.get(API_URL, params={"key": key})
        if response.status_code == 200:
            data = response.json()
            new = data[-1]
            latnew = new["lat"]
            lngnew = new["lng"]
            coord.append((latnew, lngnew))
        else:
            raise TypeError("Failed to get location data from API")

    return coord


def bus_location(request):

    coordinate = []
    #  adding bus status
    Gec_clk_coordinates = (15.422249402831747, 73.98014018286432)

    try:     
        coordprev = getloc()
    except TypeError:
        return JsonResponse({"message": "Failed to get location data from API prev"}, status=500)
    try:
        coordnew = getloc()
        for i in range(4):
            status=[]
            if (geodesic(Gec_clk_coordinates,(coordnew[i][0],coordnew[i][1]) ).meters <= 235):
                status = "in campus"
                
            else:
                status = "out campus"
                  
            temp = {"id":i+1,"lat":coordnew[i][0], "lng":coordnew[i][1], "bearing":calc_bear(coordprev[i][0],coordprev[i][1],coordnew[i][0],coordnew[i][1]),"status":status}
            coordinate.append(temp)
        coordprev = coordnew 
        
        #pushing the api data in database
        save_in_db(coordinate)

        return JsonResponse(coordinate, safe=False)
    except TypeError:
        return JsonResponse({"message": "Failed to get location data from API next"}, status=500)



# Function to calculate bearing
def calc_bear(lat1, long1, lat2, long2):
    # Convert latitude and longitude to radians
    lat1 = math.radians(lat1)
    long1 = math.radians(long1)
    lat2 = math.radians(lat2)
    long2 = math.radians(long2)

    # Calculate the bearing
    bearing = math.atan2(
        math.sin(long2 - long1) * math.cos(lat2),
        math.cos(lat1) * math.sin(lat2) - math.sin(lat1) *
        math.cos(lat2) * math.cos(long2 - long1)
    )

    # Convert the bearing to degrees
    bearing = math.degrees(bearing)

    # Make bearing positive
    bearing = (bearing + 360) % 360

    return bearing


#---------------------------------------------simulation of api--------------------------------------
# global flags for generating dummy coordinates
coordinates = [(15.422150, 73.980159), (15.422426, 73.980437), (15.422421, 73.980902),
               (15.422135, 73.981456), (15.421474,
                                        73.981658), (15.421093, 73.981746),
               (15.420736, 73.982128), (15.420329,
                                        73.982651), (15.419963, 73.983093),
               (15.419638, 73.983493), (15.419314,
                                        73.983908), (15.418834, 73.984404),
               (15.418394, 73.984649), (15.417888,
                                        73.984925), (15.417256, 73.985324),
               (15.416627, 73.985713), (15.416124,
                                        73.986225), (15.415614, 73.986710),
               (15.415003, 73.987173), (15.414231,
                                        73.987775), (15.413747, 73.988233),
               (15.412976, 73.988708), (15.412377,
                                        73.989152), (15.411892, 73.989623),
               (15.411187, 73.990346), (15.410493,
                                        73.991151), (15.410566, 73.991000),
               (15.409335, 73.992113), (15.408499,
                                        73.992798), (15.408247, 73.993479),
               (15.408049, 73.994310), (15.408469,
                                        73.995139), (15.408303, 73.995845),
               (15.407900, 73.996186), (15.407402,
                                        73.996563), (15.406862, 73.996872),
               (15.406571, 73.996970)]

# putting all cordinates in api format
locations = []
for i in range(1, 5):
    temp = []
    for tup in coordinates:
        dict_item = {'id': i, 'lat': tup[0], 'lng': tup[1], 'bearing': 0}
        temp.append(dict_item)
    # print(temp)
    locations.append(temp)

#flags for iterating in the lists 
indices = [0, 6, 8, 15]
flags = [1, -1, 1, -1]



#returns 4 coordinates
def bus_location_dummy(request):
    global indices, flags
    for i in range(4):
        if (indices[i] > 35) and (flags[i] == 1):
            flags[i] = -1
        elif (indices[i] < 0) and (flags[i] == -1):
            flags[i] = 1
        indices[i] += flags[i]

    locations_dummy = [locations[0][indices[0]], locations[1]
                       [indices[1]], locations[2][indices[2]], locations[3][indices[3]]]

    locations_dummy = [locations[0][indices[0]], locations[1]
                       [indices[1]], locations[2][indices[2]], locations[3][indices[3]]]
    
    #pushing data in database
    save_in_db(locations_dummy)
    
    return HttpResponse(json.dumps(locations_dummy), content_type="application/json")




# #returns only one coordinate
# def bus_location_dummy_old(request):
#     global location_flag, l_index
#    # -------------------------------Testing---------------------------------
#     # reversing index algorithm ( gec to ponda bustand, bustand to gec)
#     if (l_index > 19) and (location_flag == 1):
#         location_flag = -1
#     elif (l_index < 0) and (location_flag == -1):
#         location_flag = 1
#     l_index += location_flag
#     # -------------------------------Testing---------------------------------

#     return HttpResponse(json.dumps({locations[l_index]}), content_type="application/json")

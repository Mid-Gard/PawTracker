

# COde to test gmplot

# NOTE : THere is no use of using gmplot also becoz gmplot also uses google API so it is not a good option to go with unless we are going with, billing.


from django.shortcuts import render
import json
import math
from django.http import HttpResponse, JsonResponse
import random
import requests
import time

from gmplot import gmplot
import random
from gmplot import GoogleMapPlotter
# import tempfile
# import random
# from gmplot import GoogleMapPlotter
# from django.http import HttpResponse
import tempfile


API_KEY = ["api key1", "api key2", "api key3", "api key4"]
API_URL = "https://61a4a0604c822c0017041d33.mockapi.io/shuttle/v1/path"


location_flag = 1
l_index = 0
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
print(len(coordinates))

locations = []
for i in range(1, 5):
    temp = []
    for tup in coordinates:
        dict_item = {'id': i, 'lat': tup[0], 'lng': tup[1], 'bearing': 0}
        temp.append(dict_item)
    # print(temp)
    locations.append(temp)
indices = [0, 6, 8, 15]
flags = [1, -1, 1, -1]


def bus_incampus(request):
    pass


def bus_outcampus(request):
    # -------------------------------Testing---------------------------------
    return HttpResponse("GA 02 G 7455")


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
    coordinate = "["
    try:
        coordprev = getloc()
    except TypeError:
        return JsonResponse({"message": "Failed to get location data from API"}, status=500)
    try:
        coordnew = getloc()
        for i in range(4):
            temp = {"id": i+1, "lat": coordnew[i][0], "lng": coordnew[i][1], "bearing": calc_bear(
                coordprev[i][0], coordprev[i][1], coordnew[i][0], coordnew[i][1])}
            coordinate += f'{temp}'
            if i < 3:
                coordinate += ","
        coordprev = coordnew
        coordinate += "]"
        return HttpResponse(coordinate, content_type="application/json")
    except TypeError:
        return JsonResponse({"message": "Failed to get location data from API"}, status=500)


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


def bus_location_dummy(request):
    coordinates = {
        "A": {"lat": 23.819036, "lng": 90.357689},
        "B": {"lat": 23.829545, "lng": 90.368972},
        "C": {"lat": 23.838463, "lng": 90.373697},
        "D": {"lat": 23.845505, "lng": 90.378101}
    }

    # Select random latitudes and longitudes
    lats = [coordinates[coord]["lat"] for coord in coordinates]
    lngs = [coordinates[coord]["lng"] for coord in coordinates]
    random.shuffle(lats)
    random.shuffle(lngs)

    # Initialize the GoogleMapPlotter object
    gmap = GoogleMapPlotter(lats[0], lngs[0], 16)

    # Plot the route on the map
    gmap.plot(lats, lngs, 'blue', edge_width=5)

    gmap.apikey = 'AIzaSyA5Lt3E5gYb-lfogvaSpCrvCpocLqHwNOI'
    # Generate the HTML data for the map
    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        gmap.draw(tmpfile.name)
        with open(tmpfile.name) as f:
            html = f.read()

    # Return the HTML data as the HTTP response
    return HttpResponse(html)


# Code to Generate random data


# import tempfile
# import random
# from gmplot import GoogleMapPlotter
# from django.http import HttpResponse
# -------------------------------Testing---------------------------------
# global flags for generating dummy coordinates
location_flag = 1
l_index = 0
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

locations = []
for tup in coordinates:
    dict_item = {'lat': tup[0], 'lng': tup[1], 'bearing': -60.88}
    locations.append(dict_item)


def bus_incampus(request):
    # -------------------------------Testing---------------------------------
    # generating random data
    data = [
        {
            "id": 1,
            "busNumber": f"ABC{random.randint(100,999)}",
            "departureTime": f"{random.randint(1,12)}:{random.randint(10,59)} {random.choice(['AM', 'PM'])}",
            "arrivalTime": f"{random.randint(1,12)}:{random.randint(10,59)} {random.choice(['AM', 'PM'])}"
        },
        {
            "id": 2,
            "busNumber": f"XYZ{random.randint(100,999)}",
            "departureTime": f"{random.randint(1,12)}:{random.randint(10,59)} {random.choice(['AM', 'PM'])}",
            "arrivalTime": f"{random.randint(1,12)}:{random.randint(10,59)} {random.choice(['AM', 'PM'])}"
        }
    ]
    # -------------------------------Testing---------------------------------
    return HttpResponse(json.dumps(data), content_type="application/json")


def bus_outcampus(request):
    # -------------------------------Testing---------------------------------
    return HttpResponse("GA 02 G 7455")


# Function to generate the HTML with the Google Map


def generate_map_html(locations):
    # Center of the map is the first location
    gmap = gmplot.GoogleMapPlotter(
        locations[0]['lat'], locations[0]['lng'], 18)

    # Add a marker for each location
    for location in locations:
        gmap.marker(location['lat'], location['lng'])

    # Draw the map and save it to a file
    gmap.draw('map.html')

    # Open the file and read the content to return it as HTML
    with open('map.html', 'r') as f:
        html = f.read()
    return html

# this function will give dummmy data starting from gec to ponda bustand


def bus_location(request):
    global location_flag, l_index

    # -------------------------------Testing---------------------------------
    # reversing index algorithm ( gec to ponda bustand, bustand to gec)
    if (l_index > 19) and (location_flag == 1):
        location_flag = -1
    elif (l_index < 0) and (location_flag == -1):
        location_flag = 1
    l_index += location_flag
    # -------------------------------Testing---------------------------------

    # Add the marker for the current location
    marker = Marker(locations[l_index]['lat'], locations[l_index]['lng'])
    gmplot.marker(marker.lat, marker.lng, color='cornflowerblue')

    # Generate the map HTML with the marker
    html = gmplot.get_html()

    # Return the response with the map HTML and the current location
    response_data = {'html': html, 'location': locations[l_index]}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

from django.http import HttpResponse
from .models import Driver_Details
from django.shortcuts import render
import json
# import seri
from django.http import JsonResponse

# testing views of drivers
# def driver_details(request):

#         #added 6 random data on display
#     data = [
#         {
#             "id": Driver_Details.objects.get(id=1),
#             "Driver_Name": Driver_Details.objects.get(Name=1),
#             "Driver_Phone": Driver_Details.objects.get(Phone_Number=1)
#         },
# #         {
# #             "id": 2,
# #             "Driver_Name": f"John Smith",
# #             "Driver_Phone": f"369871425"
# #         },
# #         {
# #             "id": 3,
# #             "Driver_Name": f"John Wick",
# #             "Driver_Phone": f"258963147"
# #         },
# #         {
# #             "id": 4,
# #             "Driver_Name": f"D 4",
# #             "Driver_Phone": f"147896325"
# #         },
# #         {
# #             "id": 5,
# #             "Driver_Name": f"D 5",
# #             "Driver_Phone": f"369871425"
# #         },
# #         {
# #             "id": 6,
# #             "Driver_Name": f"D 6",
# #             "Driver_Phone": f"258963147"
# #         },

#     ]
#     return JsonResponse({'data': data})
# return HttpResponse(json.dumps(data), content_type="application/json")

# def driver_details(request):
#     context ={}

#     # add the dictionary during initialization
#     context[Driver_Details.Name, "Phone_Number"] = Driver_Details.objects.get(id=1)
#     return HttpResponse(context) #under developement

# def driver_details(request):
#     # data = Driver_Details.objects.all
#     data = (Driver_Details.objects.values('id', 'Name', 'Phone_Number'))
#     print(data)
#     return render(request, json.dumps(data), content_type="application/json")


def driver_details(request):
    data = list(Driver_Details.objects.values(
        'id', 'Name', 'Phone_Number', 'Driver_Pic'))
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json')

# Dynamic change of data as per the database updates.
# made some changes

![backend.png](https://github.com/tu2-atmanand/GEC_Bus_Tracking/blob/main/GEC_Bus_App/src/Backend/backend.png)

**<big><big>DISCLAIMER </big></big>**
This is a rough backend design since we don't know how to use django. The design might change when we actually start writing the code. New problems, ideas might be encountered in future.

The entire backend will be designed using django . Local API's will be created which will have all the necessay information for fronted.
Overview of Backend

1) Take information from GPS and Biometric sensor
2) Manage the database
3) Provide information to frontend in the form of APIs

Right now the structure is divided into 4 classes

1) Location
2) Driver info
3) Bus info
4) Login Details

<big>Example of a jason file given by API</big>
{ " VehicleNo ":"DL1LY5703", " DeviceImei ":"326532658965235", "TimeRecorded":"15-09-2017 20:00", "LocationAddress":"Sahara Mall, Gurgaon, Haryana - 122001", "Latitude":"28.586789", "Longitude":"76.953216", "Speed":"0", "Ignition":"OFF" }

<big>Location Class</big>

- Get location from main
- Check is the balrath is there in GEC or not (logic already explained during meet)
- Create an API which will have the coordinates and whether it's in GEC or not

<big>Driver class</big>

- Manage driver details database , provide a function to easily edit the database
- Get driver status from main
- Create an API which will have the driver info and  status

<big>Bus Class</big>

- Manage driver details , provide a function to easily edit the database
- Get bus status from main
- Create an API which will have the bus info and status

<big>Login class</big>
we won't need this class, since django provides user administration tools
![image](https://user-images.githubusercontent.com/112399179/227704606-812237ab-5513-454d-82ec-244416c3953c.png)

- Manage user details, provide a funtion to easily edit the database
- Create an Api which will have the user info ( need to discuss this with the frontend group)

**<big>Tutorials/sources</big>**

- Put the tutorial links here
- <https://youtu.be/_uQrJ0TkZlc>  04:59:00 onwards

Work assigned

1) Location Class :- Amogha
2) Driver class :- Steven
3) Bus class :-
4) Login class :-  (django provides user administration panel)  

**If you have any suggestion or any idea, directly text in the wa group or you can create an issue in the github(ask atma how to do that)**

## BackEnd TODO

NOTE : Just keeping this data here, we might implement this in future, not compulsory.

- **Student Database** : This can be done either by:
  - creating actaul database by first circulating a google form who wants to use this service, will get their rollno and add them in database and provide them the credential to login.
  - We can create a single username and password and give them, this will reduce the verification process of roll no. from academics. for now atleast.
- Need to get the type of data send by fingerprint sensor, and comparing it with the database of bus drivers. To add new bus drivers in future can automate it somehow or ...

Eg of Rest API available for gps tracking the vehicle and the data we can except to get from API:

<https://gpsgateway.in/docs/rest-api.html>

<https://www.trackmyride.com.au/app/api/>

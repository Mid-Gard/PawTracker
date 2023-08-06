# Paw Tracker

Code submission for Technofest Hackathon

# Our Approach

For convinience and to be avalable to most of the people we have used React which will create a React Web App which can be used by anyone across platform, and which further can be convrted to native React App. For backend we used Django.

Assuming this is a solution for the government of the Urban region to monitor the movement and health of the stray animals (which will consist of Dogs, Cows, cat maybe). So the government will install this devices on this stray animals, and now the webapp will provide the status of all the stray animals in that region. The access to this webapp can be provided to the urban local to access and know the status of theier neighbouring animal and can take according descisions, if they want to adopt any of that anymal they can do so, by looking at what kind of animal is it, what breed, its health, etc. They can even then register on the same app, that they have adopted this animal.

This approach uses GPS technology to get like almost the precise details of the animals and also their health on the basis of the sensors attached on their body.
>But this doesnt look like a feasible approach if its to be implemented on a large scale of animals as lot of GPS and sensor devices will be required. This approach looks like a futuristic approach. Hence we suggest the following approach.

### Second Approach

This approach of monitoring through CCTV camera and openCV for tracking and Thermal cameras can be used for getting like little bit information about their health. Now this wont give very accurate data like GPS approach, but it can solve quite few problems, like tracking the animals in a specific area, if any animal is dead from thermal cameras, etc.



## TODO : Features to Add

Besides the map, the following features needs to be added in the app :

- The map should auto resize when even a single animal goes out of the screen.
- There should be an autoscroll animation for sidebar, for usable on any resolution screen.


## How to use

1. Clone the project : ```git clone https:\\```
2. Go into the backend folder : ```cd BackEnd```
3. Install the packages : ```npm i```
4. Run the server to collect and process the data : ```python manage.py runserver```
4. Open another terminal and go in the Frontend folder : ```cd FrontEnd```.
5. Install the python packages : ```pip install -r requirements.txt```
6. Run the frontend server : ```npm start```
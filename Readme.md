# Paw Tracker

## Introduction

Paw Tracker is a comprehensive software solution designed for the Technofest Hackathon, addressing the pressing issue of managing and tracking stray animals in urban settlements. The aim of this project is to develop an efficient and user-friendly application that utilizes modern technologies to analyze the behavior of stray animals, facilitate adoptions, handle public reports, send emergency alerts, and provide valuable data insights.

## Our Approach

To ensure widespread accessibility and ease of use, we have chosen to implement a React.js frontend, creating a versatile web application that can be utilized across different platforms. Additionally, the application can be further converted into a native React app for seamless usage. For the backend, we have employed Django, a robust and scalable framework.

So based on the problem statement, and what we have understood from it, we have assumed that this solution will be used by goverment as otherwise, no one else will be track stray animals. Secondly we have assumed that the sensors is used to track the health of the animals for their wellbeing. On the basis of this we have proposed following appraches to  solve this problem, out of which only one first one is implemented due to time constraints but the second approach is within our reach to implement : 

### First Approach : GPS and Sensors
We envision this solution as a valuable tool for local governments to monitor the movement and health of stray animals, which may include dogs, cows, and cats. The government can install tracking devices on these animals, and the web application will then provide real-time status updates for all the stray animals in the region. The public can access this web application to check the status of animals in their vicinity, make informed decisions regarding any injured animals nearby, and even consider adopting these animals based on crucial information such as breed and health. Furthermore, individuals can register on the app to notify others about the animals they have adopted.

>But this approach looks like a futuristic. While the GPS technology-based approach can offer precise details about the animals' movements and health, it may not be feasible for large-scale implementation due to the need for numerous GPS and sensor devices. Hence, we propose an alternative approach:

### Second Approach : OpenCV and Sensors

In this approach, we leverage CCTV cameras and OpenCV for tracking, as well as thermal cameras to gather some information about the animals' health. While this approach may not provide the same level of accuracy as the GPS-based approach, it can still address several key challenges, including tracking animals in specific areas and detecting deceased animals using thermal cameras.

## How to Use

1. Clone the project: `git clone https:\\`
2. Navigate to the backend folder: `cd BackEnd`
3. Install the required packages: `npm i`
4. Run the server to collect and process data: `python manage.py runserver`
5. Open another terminal and go to the Frontend folder: `cd FrontEnd`.
6. Install the necessary Python packages: `pip install -r requirements.txt`
7. Run the frontend server: `npm start`

## TODO: Features to Add

In addition to the map, several important features need to be incorporated into the application:

- Implement auto-resize functionality for the map to ensure seamless display even when animals move out of the visible screen area.
- Add an autoscroll animation for the sidebar to optimize the user experience on various screen resolutions.
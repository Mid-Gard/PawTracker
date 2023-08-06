### Installing Django on your system

- open the terminal in your code editor or use any other terminal and execute the following command :

   pip install django (install pip if required)

After this step just pull the repository and then perform step 2

1) Creating a django project

   django-admin startproject project_name .
   first create a project using your ide and then execute the above command
2) Setting up the local Server

  python3(linux)/python(win)  manage.py runserver
 a link will be given in the terminal which can be accessed from the browser
 
3) Creating apps ( analogous to python package)

   python3 manage.py startapp app_name 
 ( eg. location, driver details, so on )
 
4) Creating http request for an app
 - functions should be defined in views.py
  eg
 
   from django.http import HttpResponse
    def index(request): //can be any name instead of index
    return HttpResponse('hello world')
    
 - create a new file called urls.py , this file will have all the urls related to your app

   from django.urls import path 
   from . import views //file used in step 4
   urlpatterns = [ path('', views.index)]
 - after creating urls , the main url.py of the project has to be updated

   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [path("admin/", admin.site.urls),
   path( 'app_name/', include ('app_name.urls'))

5) Saving changes in django 
      python3 manage.py migrate 

   this will make all migrations 

6) Creating superuser 
      python3 manage.py createsuperuser

**<big>Creating models</big>**
- make models in model.py
      python3 manage.py makemigrations
      python3 manage.py migrate

The above commands create the model , the result can be seen by opening dg.sqlite3 file using a db browser.

**<big>Puting model in admin console</big>**
- open the admin.py in the respective app
      from .models import class_name
      admin.site.register(class_name)


**<big>Querying Data from database</big>**
      eg.
      python3 manage.py runserver
      from app_name.model import class/model_name
      temp = model_name.objects.all()
      #getting specific entery
      entry1 = model_name.objects.get(Name="John Wick") #everything is case sensitive 
      print(entry1.Phone_Number)

# Adding imageField:

---
* In models.py, add another field called imageField, part of the library functions, this will add the "choose file" button to the page where the views are being handles.
* In the settings file of the main foolder, add a static files folder and under that folder create one more folder called images, ehrer the images will be stored.
* Add the relative path of that folder as MEDIA_URL.
* Add another line of code which will tell Django where the image is to be stored: MEDIA_ROOT line in the file, which takes the base directory and the specified path as the storage location.
---



I have created 4 apps

- location
- driver_details
- animal_details
- login_details
Follow the tutorials and write the logic in these apps

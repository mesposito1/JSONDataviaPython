#1)Website retrievel code
import urllib.request
def func1():
    weburl=urllib.request.urlopen("http://www.facebook.com")
    if(str(weburl.getcode()))=="200":
        print(weburl.read())
    else:
        print("Website is not answering")
func1()

#Import the urllib.request so we can work with the website date
#We defined what the weburl would be in this case facebook. we did this by writing a variable
#then we said if the website responds which is symbolized by 200 and not respond is symbolized by 400. We used getcode()
#then if the website responded we read the data 
#if the website did not respond we returned "website is not answering"


##JavaScript Object Notation (JSON) code for websites
#For JSON we are going to be using USGS earthquake data http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php

#2)Code to read JSON data from a webapge
import urllib.request
import json
def func2():
    urldata="http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    weburl2=urllib.request.urlopen(urldata)
    if(str(weburl2.getcode()))=="200":
        print(weburl2.read())
    else:
        print("400")
func2()

#First, then is import urllib and json so that you can work with the webpage and the json data on the webpage
#then created a variable to define the data on the webpage we want to view
#then created a variable to open the webpage and the data
#then said if the website responds, 200, to give us the data otherwise say it is 400 meaning not responding.

#3)Code to read out features from every instance of JSON data on a webpage
import urllib.request
import json
def func3():
    urldata="http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    weburl2=urllib.request.urlopen(urldata)
    Quakedata=weburl2.read()
    theJSON=json.loads(Quakedata)
    for i in theJSON   ["features"]:
        print(i["properties"]["mag"],i["properties"]["place"],i["properties"]["felt"])
func3()

#First, then is import urllib and json so that you can work with the webpage and the json data on the webpage
#then created a variable to define webpage. the urldata!
#then created a variable to open the webpage and the data. the weburl2!
#then created a variable to represent the data read when the website was open. the Quakedata
#then created a variable that takes the JSON data found on the webpage and parses into a native python object so we can access it like any other python object. the JSON!
#then wrote code for I, which means every instance in the JSON data, look under the features array. for i in JSON ["features"]:
#then return the mag, place, and # of people who felt the earthquake for every instance of data. mag, place, felt are all listed under the features array


#4)Code to read out features from every instance of JSON data on a webpage where the earthquake was greater than 4.0 
import urllib.request
import json
def func4():
    urldata="http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    weburl2=urllib.request.urlopen(urldata)
    Quakedata=weburl2.read()
    theJSON=json.loads(Quakedata)
    for i in theJSON   ["features"]:
      if i["properties"]["mag"]>= 4.0:
       print(i["properties"]["mag"],i["properties"]["place"],i["properties"]["felt"])
func4()

#First, then is import urllib and json so that you can work with the webpage and the json data on the webpage
#then created a variable to define webpage. the urldata!
#then created a variable to open the webpage and the data. the weburl2!
#then created a variable to represent the data read when the website was open. the Quakedata
#then created a variable that takes the JSON data found on the webpage and parses into a native python object so we can access it like any other python object. the JSON!
#then wrote code for I, which means every instance in the JSON data, look under the features array. for i in JSON ["features"]:
#then wrote an if statement to tell python that for every instances where under properties the listed magnitude is greater than 4.0
#then return the mag, place, and # of people who felt the earthquake for every instance of data. mag, place, felt are all listed under the features array





# ZipToTime
Micro service which takes a zipcode in JSON and returns a JSON containing the time for the given zip code. 
Microservice hosted by pythonanywhere.
To request data you can encode the required zipcode into the URL, for example:
http://ecarmona235.pythonanywhere.com/ZipToTime?zipcode=98052
or 
http://127.0.0.1:5000/ZipToTime?zipcode=98052 if running microservice file in local environment.
This call will return the current time in Redmond (98052 = Redmon zip code).
The microservice will reply to the request by sending back a JSON file under the header "time". 
For example at the time of writing this the return would be {"time":"14:36}. 

![UML Diagram](https://user-images.githubusercontent.com/64918389/180583351-f78dfa1d-2f3e-4f8f-ab4b-cd159a03bc32.png)





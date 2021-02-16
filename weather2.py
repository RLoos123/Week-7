import requests

api_key = "15dc19efb6f587aae0b38b158c40253c"
api_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + api_key + "&units=metric&"

# Display a menu for the user
print("Welcome to Weather Map Station!")
while True:
    option = input("You may search by City or Zip Code to see the weather in the area.\n"
                   "Enter 'C' to enter a City, 'Z' to enter a Zip Code, or 'Q' to Quit: ").lower()

    if option == "z" or option == "c":
        # Get input
        if option == "z":
            request_api_url = api_url + "zip=" + input("Enter a zip code: ")
        elif option == "c":
            request_api_url = api_url + "q=" + input("Enter city: ")

        request_api_url += ",us"

        # Call webservice
        try:
            json_response = requests.get(request_api_url).json()

            if "weather" not in json_response:
                print("Location not found")
            else:
                print("Weather Status   = " + json_response["weather"][0]["description"])
                print("Temp (Celsius)   = " + str(json_response["main"]["temp"]) + " degrees")
                print("Humidity         = " + str(json_response["main"]["humidity"]) + "%")
                print("Visibility       = " + str(json_response["visibility"]) + " Meters")
                print("Wind Speed       = " + str(json_response["wind"]["speed"]) + " m/s")
                print("Wind Direction   = " + str(json_response["wind"]["deg"]) + " degrees")
        except requests.exceptions.HTTPError as e:
            print("Network error = ", e)
        except requests.exceptions.ConnectionError as e:
            print("Connection error = ", e)
        except requests.exceptions.Timeout as e:
            print("Connection timed out =", e)
        except requests.exceptions.RequestException as e:
            print("Invalid request = ", e)
    elif option == "q":
        break

    print()

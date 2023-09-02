import sys
import requests
import os
from dotenv import find_dotenv, load_dotenv

# Load environment variables from .env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path=dotenv_path)

# Retrieve API endpoints from environment variables
current = os.getenv('current')
forecast = os.getenv('forecast')

def weather():
    """
    Function to fetch and display weather information based on user input.
    """
    try:
        # Prompt user for city and weather type selection
        city = input("Enter City Name: ")
        check = int(input("Press 1 to get Current Weather\nPress 2 to get Forecast:\n"))

        if check == 1:
            # Construct the URL for current weather
            url = current + city + "&aqi=yes"
            request = requests.get(url)
            r = request.json()

            print("\nShowing Search Result for:\n")

            # Display location information
            for key, value in r["location"].items():
                if key == "localtime_epoch":
                    continue
                print(key, ":", value)

            print("\nHere is your Current Weather Information:\n")
            for list, val in r["current"].items():
                # Exclude specific keys from display
                if list in ["last_updated_epoch", "temp_f", "is_day", "condition", "wind_mph", "pressure_mb", "pressure_in",
                            "precip_in", "cloud", "feelslike_f", "vis_km", "vis_miles", "gust_mph", "gust_kph", "air_quality"]:
                    continue
                print(list, ":", val)

        elif check == 2:
            # Prompt user for the number of days for the forecast
            days = input("Enter the Number of Days you want the Forecast: ")
            # Construct the URL for weather forecast
            url = forecast + city + "&days=" + days + "&aqi=no&alerts=no"
            request = requests.get(url)
            r = request.json()

            print("\nShowing Search Result for:\n")

            # Display location information
            for key, value in r["location"].items():
                print(key, ":", value)

            print("\nHere is your Forecast Weather:\n")
            for key, value in r["forecast"].items():
                daycounter = 1
                for list in value:
                    print(f"\nPrinting Forecast of Day {daycounter}\n")
                    daycounter += 1
                    print("date:", list["date"])
                    for k, v in list["day"].items():
                        # Exclude specific keys from display
                        if k in ["maxwind_mph", "totalprecip_in", "avgvis_km", "avgvis_miles", "daily_will_it_rain",
                                 "daily_will_it_snow", "condition"]:
                            continue
                        print(k, ":", v)

        else:
            print("Incorrect input")
            sys.exit()
    except Exception as e:
        print("An error occurred:", str(e))

def main():
    weather()

if __name__ == "__main__":
    main()

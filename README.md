# Project Overview

A Python script to fetch and display current weather or forecast information for a specified city using environment variables for API endpoints.

## Features

- Retrieve current weather information for a city
- Retrieve weather forecast for a specified number of days
- Display relevant weather and location information

## Prerequisites

- Python 3.x
- `requests` library
- `python-dotenv` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Ahmad1015/Weather-Forecast-Python-API-Project.git
    cd Weather-Forecast-Python-API-Project
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required libraries:
   - requests
   - python-dotenv

4. Create a `.env` file in the project directory and add your API endpoints:
    ```env
    current=<Your_Current_Weather_API_Endpoint>
    forecast=<Your_Forecast_Weather_API_Endpoint>
    ```

## Usage

1. Run the script:
    ```bash
    python weather_fetcher.py
    ```

2. Enter the city name and select the type of weather information:
    - Press 1 for current weather
    - Press 2 for weather forecast


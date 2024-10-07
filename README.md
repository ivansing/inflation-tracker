# U.S. Inflation Tracker

## Overview

This project is a web application that visualizes U.S. inflation data from the Federal Reserve Economic Data (FRED) API. The user can view inflation trends over a custom period of time (e.g., 2020 to 2024) and see normalized inflation rates.

## Features

- Fetches U.S. inflation data from FRED API.
- Allows users to select a custom date range to visualize inflation.
- Plots the normalized inflation data (relative to the selected time period).
- Interactive and dynamic visuals generated with Matplotlib.
- Environment variables for API key management.

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Getting Your API Key](#getting-your-api-key)
3. [Running the Application](#running-the-application)
4. [Testing](#testing)
5. [Screenshots](#screenshots)
6. [License](#license)

## Requirements

- Python 3.8+
- Flask
- Matplotlib
- Pandas
- Requests
- Dotenv

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/ivansing/inflation-tracker.git
   cd inflation-tracker
   ```
2. Create a virtual environment

   ```bash
   python3 -m venv venv
   source venv/bin/activate # on Windows use: venv\Scripts\activate
   ```
3. Install -r requirements.txt

## Getting Your API Key

To access U.S. inflation data, you need a FRED API key. Follow the steps to get yours:

    1. Go to [FRED website](https://fred.stlouisfed.org/)
    2. Create a free account or sign in if you already have one.
    3. Navigate to My Account > API Keys.
    4. Click on Reuqests API Key and follow the instructions to generate your key.
    5. Once you have the API key, copy it into the `.env` file as shown below.

## Running the Application


1. Set up the `.env` file in the root directory with your FRED API key:

    ```bash
    API_KEY=your_fred_api_key_here
    ```
2. Run the Flask application:

    ```bash
    python3 app.py
    ```
3. Visit the app in your browser at `http://127.0.0.1:5000`.
4. Enter the desired start and end years in integer values on the UI to see inflation trends.

## Testing

You can test the application by running it locally and entering a custom date range (for example, 1990 to 2024) in the web interface to see how the inflation data is plotted.

    
## Screenshots

![Inflation Image US range](static/inflation_plot.png?raw=true "Inflation Image")

## License

This project is licensed under the MIT license. See the LICENSE file for more information.


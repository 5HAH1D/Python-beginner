import customtkinter as ctk
from tkinter import messagebox
import requests
import json


# Define functions
def get_weather():
    """ Retrieve weather data for a specified location using the OpenWeatherMap API.
    This function retrieves the user input for the location from the global variable `location_entry`.
    It then constructs an API request URL using the input location and the OpenWeatherMap API key.
    If the API request is successful, the response is parsed using the `parse_response` function,
    and the weather data is displayed using the `display_weather` function.
    If the API request is unsuccessful, an error message is displayed to the user.

    Returns: None """

    # Get the user input for the location from the global variable `location_entry`
    location = location_entry.get()

    # API request URL constructed using the input location and the OpenWeatherMap API key
    api_key = "your_api_key_here"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    # Send the API request and get the response
    response = requests.get(url)

    # If the API request is successful, parse the response and display the weather data
    if response.status_code == 200:
        data = json.loads(response.text)
        weather_data = parse_response(data)
        display_weather(weather_data)
    else:
        # If the API request is unsuccessful, show an error message to the user
        error_message = f"Error retrieving weather data for {location}. Please check your input and try again."
        messagebox.showerror('Error', error_message)


def parse_response(response):
    """ Parse the response from an API request and extract the relevant weather data.
    Args: response (dict): A dictionary object containing the weather data.
    Returns: dict: A dictionary object containing the parsed weather data."""

    # Create a new dictionary object to store the weather data
    weather_data = {
        "Location": f"{response['name']}, {response['sys']['country']}",
        # Location string constructed using the city name and country code from the response dictionary
        "Description": response["weather"][0]["description"],  # Weather condition description
        "Temperature": f"{response['main']['temp']}°C",  # Temperature in Celsius with a degree symbol
        "Visibility": f"{response['visibility']/1000} km",  # Visibility in Kilometers
        "Humidity": f"{response['main']['humidity']}%",  # Humidity percentage
        "Wind_speed": f"{response['wind']['speed']}m/s"  # Wind speed in meters per second

    }
    # Return the weather data dictionary object
    return weather_data


def display_weather(weather_data):
    """A function that takes weather data as input and displays it in a GUI.
    Args: weather_data (dict): A dictionary containing weather information.
    Returns: None"""

    # Clear any previous weather information from the GUI
    for widget in root.winfo_children():
        if isinstance(widget, ctk.CTkFrame):
            widget.destroy()

    # Create a new frame to display the weather information
    frame = ctk.CTkFrame(root, corner_radius=15, bg_color='#444654')

    i = 0
    for key, value in weather_data.items():
        # Create a label to display the weather information
        key_label = ctk.CTkLabel(frame, text=key, font=('cambria', 15, 'bold'),
                                 width=150, anchor='w')
        key_label.grid(row=i, column=0, padx=10)

        value_label = ctk.CTkLabel(frame, text=value, font=('cambria', 15, 'bold'),
                                   width=100, anchor='center')
        value_label.grid(row=i, column=1, padx=10)

        i += 1

    # Place the frame on the GUI
    frame.place(rely=0.6, relx=0.5, anchor='center')


if __name__ == '__main__':
    # Set the appearance mode to dark and the color theme to blue
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('blue')

    # Create a new GUI window
    root = ctk.CTk()

    # Set the window properties
    root.resizable(False, False)
    root.title("Weather App")
    # Add your icon here
    # root.iconbitmap('weather.ico')
    app_width = 400
    app_height = 300
    x = (root.winfo_screenwidth() / 2) - (app_width / 2)
    y = (root.winfo_screenheight() / 2) - (app_height / 2)
    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    # Create a label and an entry widget to get user input for location
    location_label = ctk.CTkLabel(root, text="Location:", font=('lucid', 20, 'bold'))
    location_label.grid(row=1, column=0, pady=10, padx=10)

    location_entry = ctk.CTkEntry(root, width=150)
    location_entry.grid(row=1, column=1, pady=10)

    # Create a button to get the weather information for the entered location
    get_weather_button = ctk.CTkButton(root, text="Get Weather", width=50, command=get_weather)
    get_weather_button.grid(row=2, column=1, pady=10)

    # Start the main event loop for the GUI
    root.mainloop()

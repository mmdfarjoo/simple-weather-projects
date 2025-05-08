import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime, timedelta

API_KEY = "4da73916902634f6658898a253155e08" # اینجا کلید API را وارد کن
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

def get_weather(city_name):
    params = {
        'q': city_name + ',IR',
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'fa'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            raise ValueError(data.get("message", "Error in receiving information")) #خطا در دریافت اطلاعات

        forecasts = {}
        for item in data['list']:
            date_str = item['dt_txt'].split()[0]
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

            today = datetime.today().date()
            if date_obj in [today, today + timedelta(days=2)]:
                forecasts[date_obj] = item['weather'][0]['description'] + ", temperature: " + str(item['main']['temp']) + "°C"

        return forecasts

    except Exception as e:
        messagebox.showerror("error", str(e))
        return None

def show_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("warning", "Enter the name of the province.") #نام استان را وارد کنید
        return

    weather = get_weather(city)
    if weather:
        output = ""
        for date, info in weather.items():
            output += f"{date.strftime('%Y-%m-%d')} : {info}\n"
        result_label.config(text=output)

# رابط گرافیکی
root = tk.Tk()
root.title("Meteorology of Iran")

tk.Label(root, text="The name of the province:").pack(pady=5)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

tk.Button(root, text="Weather display :", command=show_weather).pack(pady=5)

result_label = tk.Label(root, text="", justify='right')
result_label.pack(pady=10)

root.mainloop()

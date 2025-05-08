import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime, timedelta
import arabic_reshaper
from bidi.algorithm import get_display

API_KEY = '4da73916902634f6658898a253155e08'
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

def fix_text(text):
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)

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
            raise ValueError(data.get("message", "خطا در دریافت اطلاعات"))

        forecasts = {}
        for item in data['list']:
            date_str = item['dt_txt'].split()[0]
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
            today = datetime.today().date()

            if date_obj in [today, today + timedelta(days=2)] and date_obj not in forecasts:
                desc = item['weather'][0]['description']
                temp = item['main']['temp']
                forecasts[date_obj] = f"{desc} - دما: {temp}°C"

        return forecasts

    except Exception as e:
        messagebox.showerror("خطا", str(e))
        return None

def show_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("هشدار", "نام استان را وارد کنید")
        return

    weather = get_weather(city)
    if weather:
        output = ""
        for date, info in sorted(weather.items()):
            f_date = fix_text(date.strftime('%Y-%m-%d'))
            f_info = fix_text(info)
            output += f"{f_date} : {f_info}\n"
        result_label.config(text=output)
    else:
        result_label.config(text=fix_text("اطلاعاتی یافت نشد."))

# رابط گرافیکی
root = tk.Tk()
root.title("پیش‌بینی وضعیت هوا")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text=fix_text("پیش‌بینی وضعیت هوا در استان‌های ایران"),
                       font=("Tahoma", 14, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=5)

tk.Label(input_frame, text=fix_text("نام استان (به انگلیسی):"),
         font=("Tahoma", 12), bg="#f0f0f0").pack(side=tk.RIGHT)

city_entry = tk.Entry(input_frame, font=("Tahoma", 12), width=20, justify='right')
city_entry.pack(side=tk.RIGHT, padx=10)

tk.Button(root, text=fix_text("نمایش وضعیت هوا"), font=("Tahoma", 12),
          bg="#4CAF50", fg="white", command=show_weather).pack(pady=10)

result_label = tk.Label(root, text="", justify='right',
                        font=("Tahoma", 11), bg="#f0f0f0", fg="#000")
result_label.pack(pady=10)

root.mainloop()
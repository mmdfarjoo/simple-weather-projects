import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
from io import BytesIO
import arabic_reshaper
from bidi.algorithm import get_display
import jdatetime
from datetime import datetime, timedelta

API_KEY = '4da73916902634f6658898a253155e08'
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

def fix_text(text):
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)

def to_persian_date(gregorian_date):
    date_obj = jdatetime.date.fromgregorian(date=gregorian_date)
    return date_obj.strftime("%Y/%m/%d")

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
                icon_code = item['weather'][0]['icon']
                forecasts[date_obj] = {
                    'desc': desc,
                    'temp': temp,
                    'icon': icon_code
                }

        return forecasts

    except Exception as e:
        messagebox.showerror("خطا", str(e))
        return None

def show_weather():
    for widget in result_frame.winfo_children():
        widget.destroy()

    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("هشدار", "نام استان را وارد کنید")
        return

    weather = get_weather(city)
    if weather:
        for date, info in sorted(weather.items()):
            # دانلود آیکن
            icon_url = f"http://openweathermap.org/img/wn/{info['icon']}@2x.png"
            icon_data = requests.get(icon_url).content
            icon_image = Image.open(BytesIO(icon_data)).resize((50, 50))
            photo = ImageTk.PhotoImage(icon_image)

            frame = tk.Frame(result_frame, bg="#f9f9f9")
            frame.pack(fill=tk.X, padx=10, pady=5)

            icon_label = tk.Label(frame, image=photo, bg="#f9f9f9")
            icon_label.image = photo  # جلوگیری از حذف تصویر
            icon_label.pack(side=tk.RIGHT, padx=5)

            date_label = tk.Label(frame, text=fix_text(to_persian_date(date)),
                                  font=("Tahoma", 12, "bold"), bg="#f9f9f9", fg="#333")
            date_label.pack(anchor="e")

            desc_label = tk.Label(frame, text=fix_text(info['desc']),
                                  font=("Tahoma", 11), bg="#f9f9f9", fg="#000")
            desc_label.pack(anchor="e")

            temp_label = tk.Label(frame, text=fix_text(f"دما: {info['temp']}°C"),
                                  font=("Tahoma", 11), bg="#f9f9f9", fg="#000")
            temp_label.pack(anchor="e")
    else:
        tk.Label(result_frame, text=fix_text("اطلاعاتی یافت نشد."),
                 font=("Tahoma", 12), bg="#f9f9f9", fg="red").pack(pady=10)

# رابط گرافیکی
root = tk.Tk()
root.title("پیش‌بینی وضعیت هوا")
root.geometry("420x500")
root.configure(bg="#f9f9f9")

tk.Label(root, text=fix_text("پیش‌بینی وضعیت هوا در استان‌های ایران"),
         font=("Tahoma", 14, "bold"), bg="#f9f9f9", fg="#333").pack(pady=10)

input_frame = tk.Frame(root, bg="#f9f9f9")
input_frame.pack(pady=5)

tk.Label(input_frame, text=fix_text("نام استان (به انگلیسی):"),
         font=("Tahoma", 12), bg="#f9f9f9").pack(side=tk.RIGHT)

city_entry = tk.Entry(input_frame, font=("Tahoma", 12), width=20, justify='right')
city_entry.pack(side=tk.RIGHT, padx=10)
tk.Button(root, text=fix_text("نمایش وضعیت هوا"), font=("Tahoma", 12),
          bg="#2196F3", fg="white", command=show_weather).pack(pady=10)

result_frame = tk.Frame(root, bg="#f9f9f9")
result_frame.pack(fill=tk.BOTH, expand=True)

root.mainloop()
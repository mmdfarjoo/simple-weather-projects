import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import requests
from io import BytesIO
import arabic_reshaper
from bidi.algorithm import get_display
import jdatetime
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

API_KEY = '4da73916902634f6658898a253155e08'
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

iran_cities = [
    "Tehran", "Isfahan", "Mashhad", "Tabriz", "Shiraz", "Qom",
    "Kerman", "Ahvaz", "Yazd", "Sanandaj", "Rasht", "Hamedan",
    "Arak", "Bandar Abbas", "Zanjan", "Bushehr", "Gorgan", "Ilam",
    "Khorramabad", "Urmia", "Kermanshah", "Birjand", "Bojnurd"
]

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

            if date_obj in [today, today + timedelta(days=1), today + timedelta(days=2)] and date_obj not in forecasts:
                weather = item['weather'][0]
                main = item['main']
                wind = item['wind']
                forecasts[date_obj] = {
                    'desc': weather['description'],
                    'temp': main['temp'],
                    'humidity': main['humidity'],
                    'wind_speed': wind['speed'],
                    'icon': weather['icon']
                }

        return forecasts

    except Exception as e:
        messagebox.showerror("خطا", str(e))
        return None

def show_weather():
    for widget in result_frame.winfo_children():
        widget.destroy()

    city = city_var.get().strip()
    if not city:
        messagebox.showwarning("هشدار", "لطفاً یک استان را انتخاب کنید")
        return

    weather = get_weather(city)
    if weather:
        humidities = []
        dates = []

        for date, info in sorted(weather.items()):
            humidities.append(info['humidity'])
            dates.append(to_persian_date(date))

            icon_url = f"http://openweathermap.org/img/wn/{info['icon']}@2x.png"
            icon_data = requests.get(icon_url).content
            icon_image = Image.open(BytesIO(icon_data)).resize((50, 50))
            photo = ImageTk.PhotoImage(icon_image)

            frame = tk.Frame(result_frame, bg="#f1f1f1", bd=1, relief="solid")
            frame.pack(fill=tk.X, padx=10, pady=5)

            icon_label = tk.Label(frame, image=photo, bg="#f1f1f1")
            icon_label.image = photo
            icon_label.pack(side=tk.RIGHT, padx=5)

            info_frame = tk.Frame(frame, bg="#f1f1f1")
            info_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

            tk.Label(info_frame, text=fix_text(to_persian_date(date)),
                     font=("Tahoma", 12, "bold"), bg="#f1f1f1", anchor='e').pack(anchor="e")
            tk.Label(info_frame, text=fix_text(f"وضعیت: {info['desc']}"),
                     font=("Tahoma", 11), bg="#f1f1f1", anchor='e').pack(anchor="e")
            tk.Label(info_frame, text=fix_text(f"دما: {info['temp']}°C"),
                     font=("Tahoma", 11), bg="#f1f1f1", anchor='e').pack(anchor="e")
            tk.Label(info_frame, text=fix_text(f"رطوبت: {info['humidity']}%"),
                     font=("Tahoma", 11), bg="#f1f1f1", anchor='e').pack(anchor="e")
            tk.Label(info_frame, text=fix_text(f"سرعت باد: {info['wind_speed']} m/s"),
                     font=("Tahoma", 11), bg="#f1f1f1", anchor='e').pack(anchor="e")

        draw_humidity_chart(dates, humidities)
    else:
        tk.Label(result_frame, text=fix_text("اطلاعاتی یافت نشد."),
                 font=("Tahoma", 12), bg="#f9f9f9", fg="red").pack(pady=10)

def draw_humidity_chart(dates, humidities):
    fig, ax = plt.subplots(figsize=(4.5, 2.8), dpi=100)
    ax.plot(dates, humidities, marker='o', color='blue')
    ax.set_title("نمودار رطوبت")
    ax.set_ylabel("درصد")
    ax.set_xlabel("تاریخ")
    ax.grid(True)

    # حذف نمودار قبلی
    for widget in chart_frame.winfo_children():
        widget.destroy()

    chart = FigureCanvasTkAgg(fig, master=chart_frame)
    chart.draw()
    chart.get_tk_widget().pack()

# رابط گرافیکی
root = tk.Tk()
root.title("پیش‌بینی وضعیت هوا")
root.geometry("500x700")
root.configure(bg="#f9f9f9")

tk.Label(root, text=fix_text("پیش‌بینی وضعیت هوا (۳ روز آینده)"),
         font=("Tahoma", 14, "bold"), bg="#f9f9f9", fg="#333").pack(pady=10)

input_frame = tk.Frame(root, bg="#f9f9f9")
input_frame.pack(pady=5)

tk.Label(input_frame, text=fix_text("انتخاب استان:"),
         font=("Tahoma", 12), bg="#f9f9f9").pack(side=tk.RIGHT, padx=5)

city_var = tk.StringVar()
city_menu = ttk.Combobox(input_frame, textvariable=city_var,
                         values=iran_cities, font=("Tahoma", 12), width=20, justify="right")
city_menu.pack(side=tk.RIGHT)

tk.Button(root, text=fix_text("نمایش وضعیت هوا"), font=("Tahoma", 12),
          bg="#2196F3", fg="white", command=show_weather).pack(pady=10)

chart_frame = tk.Frame(root, bg="#f9f9f9")
chart_frame.pack()

result_frame = tk.Frame(root, bg="#f9f9f9")
result_frame.pack(fill=tk.BOTH, expand=True)

root.mainloop()
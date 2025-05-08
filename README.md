# simple-weather-projects


پروژه: اپلیکیشن هواشناسی ایران با Tkinter

هدف:

ساخت یک اپلیکیشن دسکتاپ با رابط گرافیکی برای نمایش وضعیت آب‌وهوا در استان‌های ایران با استفاده از OpenWeatherMap API.


کلید api :
"4da73916902634f6658898a253155e08"
این کلید از نسخه رایگان open weather map  استفاده میکند


---
![1](https://github.com/user-attachments/assets/a3cb816e-c6f7-4d51-b430-bdebce4223e4)


نسخه 1: ساختار اولیه با Tkinter

امکانات:

دریافت نام استان به صورت متنی

نمایش وضعیت آب‌وهوا برای امروز و دو روز بعد

استفاده از API سایت OpenWeatherMap


----
در نسخه اول به دلیل سازگار نبودن زبان فارسی با tkinter حروف به صورت برعکس خوانده می شوند . اما میتوان متوجه شد که جه نوشته شده است.

----




کتابخانه‌های مورد استفاده:

tkinter (پیش‌فرض در پایتون)

requests


نصب:

pip install requests

اگر بر روی سیستم های لینوکسی هستید نیاز به نصب کتابخانه tkinter  است

pip install python3-tk


---
![2](https://github.com/user-attachments/assets/26d93023-0b50-457c-a0e0-9cbdb5ea5e45)



نسخه 2: رفع مشکل نمایش فارسی

تغییرات:

استفاده از arabic_reshaper و python-bidi برای درست نشان دادن متن فارسی در Tkinter


کتابخانه‌های نصب‌شده:

pip install arabic-reshaper
pip install python-bidi


---

![3](https://github.com/user-attachments/assets/1bfd7932-6d83-40c4-bb01-0e7d7f8b7341)


نسخه 3: طراحی رابط کاربری زیباتر

تغییرات:

طراحی بصری بهتر با رنگ‌بندی و قاب‌بندی (Frame)

نمایش آیکن وضعیت آب‌وهوا (با استفاده از PIL)


کتابخانه‌های اضافه:

pip install pillow


---
![4](https://github.com/user-attachments/assets/9b1b5a39-668b-4e3e-9b35-22f73f8dceeb)



نسخه 4: نمایش تاریخ شمسی

تغییرات:

تبدیل تاریخ میلادی به شمسی با استفاده از jdatetime


نصب:

pip install jdatetime


---
![5](https://github.com/user-attachments/assets/6ee5d876-41e6-40fa-9ad2-1a5c1cc4d40d)



نسخه 5: منوی کشویی و نمودار

تغییرات مهم:

جایگزینی فیلد متنی با منوی کشویی (ComboBox) برای انتخاب استان

نمایش نمودار رطوبت ۳ روز آینده با استفاده از matplotlib


کتابخانه‌های جدید:

pip install matplotlib


---

لیست کامل کتابخانه‌های مورد نیاز:

pip install requests <br>
pip install pillow <br>
pip install arabic-reshaper <br>
pip install python-bidi <br>
pip install jdatetime <br>
pip install matplotlib <br>




پروژه: اپلیکیشن هواشناسی ایران با Tkinter

هدف:

ساخت یک اپلیکیشن دسکتاپ با رابط گرافیکی برای نمایش وضعیت آب‌وهوا در استان‌های ایران با استفاده از OpenWeatherMap API.


کلید api :
"4da73916902634f6658898a253155e08"
این کلید از نسخه رایگان open weather map  استفاده میکند


---

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

نسخه 2: رفع مشکل نمایش فارسی

تغییرات:

استفاده از arabic_reshaper و python-bidi برای درست نشان دادن متن فارسی در Tkinter


کتابخانه‌های نصب‌شده:

pip install arabic-reshaper
pip install python-bidi


---

نسخه 3: طراحی رابط کاربری زیباتر

تغییرات:

طراحی بصری بهتر با رنگ‌بندی و قاب‌بندی (Frame)

نمایش آیکن وضعیت آب‌وهوا (با استفاده از PIL)


کتابخانه‌های اضافه:

pip install pillow


---

نسخه 4: نمایش تاریخ شمسی

تغییرات:

تبدیل تاریخ میلادی به شمسی با استفاده از jdatetime


نصب:

pip install jdatetime


---

نسخه 5: منوی کشویی و نمودار

تغییرات مهم:

جایگزینی فیلد متنی با منوی کشویی (ComboBox) برای انتخاب استان

نمایش نمودار رطوبت ۳ روز آینده با استفاده از matplotlib


کتابخانه‌های جدید:

pip install matplotlib


---

لیست کامل کتابخانه‌های مورد نیاز:

pip install requests
pip install pillow
pip install arabic-reshaper
pip install python-bidi
pip install jdatetime
pip install matplotlib




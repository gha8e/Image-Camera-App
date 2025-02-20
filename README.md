# تطبيق الصورة والكاميرا

هذا المشروع هو تطبيق بسيط لمعالجة الصور والتقاطها باستخدام الكاميرا. يعتمد التطبيق على مكتبات Python مثل OpenCV وTkinter وPillow، ويوفر واجهة رسومية سهلة الاستخدام للقيام بالعمليات التالية:

- *فتح الصور:* اختيار صورة من الجهاز وعرضها داخل التطبيق.
- *التقاط الصور:* استخدام الكاميرا المدمجة لالتقاط صورة.
- *حفظ الصور:* إمكانية حفظ الصورة بعد إجراء التعديلات.
- *تطبيق تأثير Grayscale:* تحويل الصورة إلى تدرج رمادي.
- *تغيير حجم الصورة:* تقليل أبعاد الصورة بنسبة 50%.
- *عرض معلومات الصورة:* مثل الأبعاد وعدد القنوات.

## المميزات

- *واجهة مستخدم بسيطة:* بفضل استخدام Tkinter.
- *معالجة الصور:* باستخدام OpenCV وPillow.
- *سهولة الاستخدام:* كل ميزة يمكن الوصول إليها عبر أزرار واضحة في الواجهة.

## المتطلبات

- Python 3.x
- المكتبات التالية:
  - OpenCV (opencv-python)
  - Pillow (Pillow)
  - NumPy (numpy)
  - Tkinter (غالبًا ما تكون مثبتة مع Python)

## التثبيت

1. تأكدي من تثبيت Python 3 على جهازك.
2. ثبتي المكتبات المطلوبة باستخدام الأمر التالي في Terminal أو Command Prompt:
   ```bash
   pip install opencv-python Pillow numpy


# شرح تفصيلي للكود

### 1. استيراد المكتبات
python
import cv2          # معالجة الصور والكاميرا
import tkinter as tk # لواجهة المستخدم
from tkinter import filedialog, messagebox # للتفاعل مع الملفات
from PIL import Image, ImageTk # لعرض الصور في Tkinter
import numpy as np   # للمعالجة الرقمية


---

### 2. المتغيرات العامة
python
current_image = None # تخزين الصورة الحالية


---

### 3. فتح الصورة (open_image())
- *الوظيفة*: يفتح نافذة لاختيار صورة (JPG, PNG, etc).
- *التفاصيل*:
  - filedialog.askopenfilename(): يحدد المستخدم الملف.
  - cv2.imread(): تحميل الصورة باستخدام OpenCV.
  - show_image(): عرض الصورة في الواجهة.

---

### 4. التقاط صورة من الكاميرا (capture_image())
- *الوظيفة*: يلتقط صورة من الكاميرا المدمجة.
- *التفاصيل*:
  - cv2.VideoCapture(0): الاتصال بالكاميرا (0 = كاميرا الجهاز).
  - cap.read(): التقاط الإطار.
  - cap.release(): تحرير الكاميرا بعد الاستخدام.

---

### 5. حفظ الصورة (save_image())
- *الوظيفة*: حفظ الصورة المعدلة.
- *التفاصيل*:
  - asksaveasfilename(): تحديد مسار الحفظ.
  - cv2.imwrite(): حفظ الصورة بالتنسيق المحدد.
  - messagebox: إظهار رسالة نجاح/خطأ.

---

### 6. عرض الصورة (show_image())
- *الوظيفة*: تحويل الصورة إلى تنسيق مناسب لعرضها في Tkinter.
- *التفاصيل*:
  - cv2.cvtColor(): تحويل من BGR (OpenCV) إلى RGB (Pillow).
  - Image.fromarray(): تحويل numpy array إلى صورة Pillow.
  - ImageTk.PhotoImage(): تحويل الصورة لتكون متوافقة مع Tkinter.

---

### 7. تحديث معلومات الصورة (update_image_info())
- *الوظيفة*: عرض أبعاد الصورة وعدد القنوات (مثل 3 للألوان، 1 للرمادي).
- *التفاصيل*:
  - img.shape: إرجاع (الارتفاع، العرض، القنوات).

---

### 8. تأثير Grayscale (apply_grayscale())
- *الوظيفة*: تحويل الصورة إلى تدرج رمادي.
- *التفاصيل*:
  - cv2.COLOR_BGR2GRAY: تحويل مساحة الألوان.

---

### 9. تغيير حجم الصورة (resize_image())
- *الوظيفة*: تصغير الصورة إلى 50% من حجمها الأصلي.
- *التفاصيل*:
  - cv2.resize(): تغيير الأبعاد مع الحفاظ على النسبة.

---

### 10. واجهة المستخدم (Tkinter)
python
root = tk.Tk() # نافذة التطبيق الرئيسية
# الأزرار:
open_button = tk.Button(root, text="Open Image", command=open_image)
capture_button = tk.Button(root, text="Capture Image", command=capture_image)
# ... (بقية الأزرار بنفس الطريقة)
label = tk.Label(root) # لعرض الصورة
info_label = tk.Label(root, text="Dimensions: \nChannels: ") # للمعلومات


---

### 1. *التقاط صور للتطبيق:*
- *شكل الواجهة الرئيسية:*  
  

- *مثال على فتح صورة:*  
  ![Open Image](screenshots/open_image.png)  
  (صورة بعد فتح صورة من الجهاز)

- *تأثير Grayscale:*  
  ![Grayscale](screenshots/grayscale.png)  
  (صورة قبل وبعد تطبيق ال

   

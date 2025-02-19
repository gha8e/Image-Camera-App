import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

current_image = None


def open_image():
    global current_image
    filepath = filedialog.askopenfilename(
     title="Select an image",
     filetypes=[("Image Files", ".jpg;.png;.jpeg;.bmp;*.gif")])
    if filepath:
        current_image = cv2.imread(filepath)
        show_image(current_image)

# Function to capture an image from the camera
def capture_image():
    global current_image
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        current_image = frame
        show_image(frame)
    cap.release()

# Function to save the modified image
def save_image():
    if current_image is not None:
        filepath = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", ".jpg"), ("PNG files", ".png")])
        if filepath:
            cv2.imwrite(filepath, current_image)
            messagebox.showinfo("Saved", "Image saved successfully!")
    else:
        messagebox.showerror("Error", "No image to save.")

# Function to show the image in the Tkinter window
def show_image(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(img_pil)
    
    label.config(image=img_tk)
    label.image = img_tk
    update_image_info(img)

# Function to update the image information (dimensions, channels)
def update_image_info(img):
    height, width, channels = img.shape
    info_label.config(text=f"Dimensions: {width}x{height}\nChannels: {channels}")

# Function to draw a rectangle on the image
def draw_rectangle(event, x, y, flags, param):
    global current_image
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(current_image, (x, y), (x+100, y+100), (0, 255, 0), 2)
        show_image(current_image)

# Function to apply grayscale filter
def apply_grayscale():
    global current_image
    if current_image is not None:
        current_image = cv2.cvtColor(current_image, cv2.COLOR_BGR2GRAY)
        show_image(current_image)
    else:
        messagebox.showerror("Error", "No image to apply filter.")

# Function to resize the image
def resize_image():
    global current_image
    if current_image is not None:
        width = int(current_image.shape[1] * 0.5)
        height = int(current_image.shape[0] * 0.5)
        current_image = cv2.resize(current_image, (width, height))
        show_image(current_image)
    else:
        messagebox.showerror("Error", "No image to resize.")

# Main Tkinter window
root = tk.Tk()
root.title("Image and Camera App")

# Label to display the image
label = tk.Label(root)
label.pack()

# Information label for image details (Dimensions, Channels)
info_label = tk.Label(root, text="Dimensions: \nChannels: ", font=("Arial", 12))
info_label.pack()

# Buttons for the actions
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

capture_button = tk.Button(root, text="Capture Image", command=capture_image)
capture_button.pack()

save_button = tk.Button(root, text="Save Image", command=save_image)
save_button.pack()

grayscale_button = tk.Button(root, text="Apply Grayscale", command=apply_grayscale)
grayscale_button.pack()

resize_button = tk.Button(root, text="Resize Image", command=resize_image)
resize_button.pack()

# Start the Tkinter main loop
root.mainloop()
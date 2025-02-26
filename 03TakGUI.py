import tkinter as tk
from tkinter import messagebox

def calculate_vibration_distance():
    try:
        # Get input values
        v = float(speed_entry.get())  # Get speed (v) from the entry
        f = float(frequency_entry.get())  # Get frequency (f) from the entry
        
        # Calculate the vibration distance
        D = 27010 * v / f
        
        # Display the result
        result_label.config(text=f"ระยะการสั่นสะเทือน: {D:.2f} mm")

        # Provide machine size recommendation
        if D < 1.80:
            recommendation_label.config(text="เหมาะสำหรับเครื่องจักรขนาดกลางลงมา")
        else:
            recommendation_label.config(text="เหมาะสำหรับเครื่องจักรขนาดใหญ่ขึ้นไป")
    except ValueError:
        messagebox.showerror("Input Error", "กรุณากรอกข้อมูลให้ถูกต้อง")

def clear_fields():
    speed_entry.delete(0, tk.END)
    frequency_entry.delete(0, tk.END)
    result_label.config(text="ระยะการสั่นสะเทือน: ")
    recommendation_label.config(text="")

def exit_program():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Vibration Distance Calculator")
root.geometry("400x300")
root.config(bg="#f4f4f9")

# Create a title label
title_label = tk.Label(root, text="คำนวณระยะการสั่นสะเทือน", font=("Arial", 16, "bold"), bg="#f4f4f9")
title_label.pack(pady=10)

# Create a frame for the input fields
input_frame = tk.Frame(root, bg="#f4f4f9")
input_frame.pack(pady=20)

# Speed input
speed_label = tk.Label(input_frame, text="กรุณากรอกความเร็ว:", font=("Arial", 12), bg="#f4f4f9")
speed_label.grid(row=0, column=0, padx=10, pady=5)
speed_entry = tk.Entry(input_frame, font=("Arial", 12))
speed_entry.grid(row=0, column=1, padx=10, pady=5)

# Frequency input
frequency_label = tk.Label(input_frame, text="กรุณากรอกความเร็วรอบ:", font=("Arial", 12), bg="#f4f4f9")
frequency_label.grid(row=1, column=0, padx=10, pady=5)
frequency_entry = tk.Entry(input_frame, font=("Arial", 12))
frequency_entry.grid(row=1, column=1, padx=10, pady=5)

# Create a button frame
button_frame = tk.Frame(root, bg="#f4f4f9")
button_frame.pack(pady=10)

# Calculate button
calculate_button = tk.Button(button_frame, text="คำนวณ", font=("Arial", 12), bg="#4CAF50", fg="white", command=calculate_vibration_distance)
calculate_button.grid(row=0, column=0, padx=10)

# Clear button
clear_button = tk.Button(button_frame, text="ล้าง", font=("Arial", 12), bg="#f44336", fg="white", command=clear_fields)
clear_button.grid(row=0, column=1, padx=10)

# Exit button
exit_button = tk.Button(button_frame, text="ออก", font=("Arial", 12), bg="#f44336", fg="white", command=exit_program)
exit_button.grid(row=0, column=2, padx=10)

# Result label
result_label = tk.Label(root, text="ระยะการสั่นสะเทือน: ", font=("Arial", 14), bg="#f4f4f9")
result_label.pack(pady=10)

# Recommendation label
recommendation_label = tk.Label(root, text="", font=("Arial", 12), bg="#f4f4f9", fg="#888")
recommendation_label.pack()

# Run the application
root.mainloop()

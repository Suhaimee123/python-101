import tkinter as tk

def calculate_grade():
    score = float(score_entry.get())
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
    result_label.config(text="Your grade is " + grade)

# สร้างหน้าต่าง GUI
window = tk.Tk()

# กำหนดชื่อหน้าต่าง
window.title("Grade Calculator")

# กำหนดขนาดหน้าต่าง
window.geometry("300x200")

# สร้างป้ายแสดงคะแนน
score_label = tk.Label(text="Enter your score:")
score_label.pack(pady=10)

# สร้างช่องกรอกคะแนน
score_entry = tk.Entry()
score_entry.pack()

# สร้างปุ่มคำนวณเกรด
calculate_button = tk.Button(text="Calculate Grade", command=calculate_grade)
calculate_button.pack(pady=10)

# สร้างป้ายแสดงผล
result_label = tk.Label(text="")
result_label.pack()

# เริ่มการทำงานของหน้าต่าง GUI
window.mainloop()

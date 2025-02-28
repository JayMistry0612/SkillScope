import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3
import userdashboard


def postResume(userId):
    conn = sqlite3.connect('SkillScope.db')
    cursor = conn.cursor()

    # logged_in_user_id = 1

    def upload_resume():
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                resume_content = file.read()

            cursor.execute("UPDATE user_details SET resume_content = ? WHERE user_id = ?", 
                        (resume_content, userId))
            conn.commit()
            messagebox.showinfo("Success", "Resume uploaded successfully!")

    def go_back():
        resume_window.destroy()
        userdashboard.user_dashboard(userId)

    resume_window = tk.Tk()
    resume_window.title("Post Resume")
    resume_window.geometry("400x300")

    tk.Label(resume_window, text="Upload your Resume (TXT File):").pack(pady=20)
    btn_upload = tk.Button(resume_window, text="Upload Resume", command=upload_resume)
    btn_upload.pack(pady=10)

    btn_back = tk.Button(resume_window, text="Back", command=go_back)
    btn_back.pack(pady=10)

    resume_window.mainloop()
    conn.close()

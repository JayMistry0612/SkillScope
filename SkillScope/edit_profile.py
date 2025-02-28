import tkinter as tk
import sqlite3
import userdashboard



def edit_Profile(userID):
    conn = sqlite3.connect('SkillScope.db')
    cursor = conn.cursor()

    # logged_in_user_id = 1

    def update_profile():
        cursor.execute("UPDATE users SET username=?, email=?, phone_no=? WHERE user_id=?",
                    (username_entry.get(), email_entry.get(), phone_entry.get(), userID))
        cursor.execute("UPDATE user_details SET top_skill=? WHERE user_id=?",skills_entry.get(),userID)
        conn.commit()

    def go_back():
        edit_window.destroy()
        userdashboard.user_dashboard(userID)
        

    edit_window = tk.Tk()
    edit_window.title("Edit Profile")
    edit_window.geometry("400x300")

    tk.Label(edit_window, text="Username:").pack()
    username_entry = tk.Entry(edit_window)
    username_entry.pack()

    tk.Label(edit_window, text="Email:").pack()
    email_entry = tk.Entry(edit_window)
    email_entry.pack()

    tk.Label(edit_window, text="Phone Number:").pack()
    phone_entry = tk.Entry(edit_window)
    phone_entry.pack()

    tk.Label(edit_window, text="Top Skills (comma-separated):").pack()
    skills_entry = tk.Entry(edit_window)
    skills_entry.pack()

    btn_update = tk.Button(edit_window, text="Update Profile", command=update_profile)
    btn_update.pack()

    btn_back = tk.Button(edit_window, text="Back", command=go_back)
    btn_back.pack(pady=10)

    edit_window.mainloop()
    conn.close()

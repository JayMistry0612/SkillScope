# import sqlite3
# import tkinter as tk
# from tkinter import filedialog, messagebox, ttk

# def open_dashboard(user_id, username):
#     # Initialize Window
#     root = tk.Tk()
#     root.title("Job Market Dashboard")
#     root.geometry("600x600")
#     root.configure(bg="#f5f5f5")

#     # Database Connection
#     conn = sqlite3.connect("mydatabase.db")
#     cursor = conn.cursor()

#     # Fetch Recommended Jobs based on User Skills
#     cursor.execute("SELECT skills FROM user_details WHERE user_id = ?", (user_id,))
#     user_skills = cursor.fetchone()
#     skills_query = "%" + user_skills[0] + "%" if user_skills else "%"

#     cursor.execute("SELECT * FROM jobs WHERE skills_required LIKE ?", (skills_query,))
#     jobs = cursor.fetchall()
#     conn.close()

#     # UI Styling
#     heading = tk.Label(root, text=f"Welcome, {username}!", font=("Arial", 16, "bold"), bg="#3498db", fg="white", pady=10)
#     heading.pack(fill="x")

#     job_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
#     job_frame.pack(pady=10, padx=10, fill="both", expand=True)

#     tk.Label(job_frame, text="Recommended Jobs", font=("Arial", 12, "bold"), bg="white").pack(pady=5)

#     job_listbox = tk.Listbox(job_frame, height=10, font=("Arial", 10))
#     job_listbox.pack(pady=5, padx=10, fill="both", expand=True)
    
#     for job in jobs:
#         job_listbox.insert(tk.END, f"{job[1]} at {job[2]} ({job[3]})")

#     # Search Feature
#     search_frame = tk.Frame(root, bg="#f5f5f5")
#     search_frame.pack(pady=10, fill="x")

#     tk.Label(search_frame, text="Search Jobs:", font=("Arial", 10, "bold"), bg="#f5f5f5").pack(side="left", padx=10)
#     search_entry = tk.Entry(search_frame, width=30)
#     search_entry.pack(side="left", padx=5)

#     def search_jobs():
#         query = "%" + search_entry.get().strip() + "%"
#         conn = sqlite3.connect("mydatabase.db")
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM jobs WHERE title LIKE ? OR company LIKE ? OR skills_required LIKE ?", (query, query, query))
#         search_results = cursor.fetchall()
#         conn.close()
#         job_listbox.delete(0, tk.END)
#         for job in search_results:
#             job_listbox.insert(tk.END, f"{job[1]} at {job[2]} ({job[3]})")

#     tk.Button(search_frame, text="Search", command=search_jobs, bg="#2ecc71", fg="white").pack(side="left", padx=5)

#     # Upload Resume
#     def upload_resume():
#         file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
#         if file_path:
#             with open(file_path, "r") as file:
#                 resume_content = file.read()
#             conn = sqlite3.connect("mydatabase.db")
#             cursor = conn.cursor()
#             cursor.execute("INSERT INTO resumes (user_id, resume_text) VALUES (?, ?)", (user_id, resume_content))
#             conn.commit()
#             conn.close()
#             messagebox.showinfo("Success", "Resume uploaded successfully!")

#     # Create Resume
#     def create_resume():
#         messagebox.showinfo("Feature", "Resume creation feature coming soon!")

#     # Edit Profile
#     def edit_profile():
#         messagebox.showinfo("Feature", "Edit Profile feature coming soon!")

#     # Buttons Frame
#     btn_frame = tk.Frame(root, bg="#f5f5f5")
#     btn_frame.pack(pady=20, fill="x")

#     tk.Button(btn_frame, text="Upload Resume", command=upload_resume, bg="#e74c3c", fg="white", width=20).pack(side="left", padx=10)
#     tk.Button(btn_frame, text="Edit Profile", command=edit_profile, bg="#f39c12", fg="white", width=20).pack(side="left", padx=10)
#     tk.Button(btn_frame, text="Create Resume", command=create_resume, bg="#8e44ad", fg="white", width=20).pack(side="left", padx=10)

#     root.mainloop()

# open_dashboard(1,'a')


# pas='Nikhil124'

# for i in pas:
#     if i in '@#$%' or i.isalnum() or i.isupper() or i.islower():
#         check=True
#     else:
#         break

# else:
#     print("correct")

# import sqlite3
# import tkinter as tk
# from tkinter import messagebox, ttk

# def setup_database():
#     conn = sqlite3.connect("mydatabase.db")
#     cursor = conn.cursor()
    
#     # Create recruiters_details table if not exists
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS recruiters_details (
#             recruiter_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_id INTEGER,
#             company_name TEXT NOT NULL,
#             position TEXT NOT NULL,
#             location TEXT NOT NULL,
#             company_email TEXT NOT NULL UNIQUE,
#             FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
#         )
#     ''')
    
#     # Create jobs table if not exists
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS jobs (
#             job_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             recruiter_id INTEGER,
#             job_position TEXT NOT NULL,
#             location TEXT NOT NULL,
#             job_type TEXT NOT NULL,  -- Remote/Hybrid/On-site
#             salary INTEGER NOT NULL,
#             skills_required TEXT NOT NULL,
#             total_positions INTEGER NOT NULL,
#             FOREIGN KEY (recruiter_id) REFERENCES recruiters_details(recruiter_id) ON DELETE CASCADE
#         )
#     ''')
    
#     # Create applicants table if not exists
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS applicants (
#             applicant_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             job_id INTEGER,
#             user_id INTEGER,
#             resume TEXT NOT NULL,
#             status TEXT DEFAULT 'Pending',
#             FOREIGN KEY (job_id) REFERENCES jobs(job_id) ON DELETE CASCADE,
#             FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
#         )
#     ''')
    
#     conn.commit()
#     conn.close()

# def recruiter_dashboard(recruiter_id, company_name):
#     root = tk.Tk()
#     root.title("Recruiter Dashboard")
#     root.geometry("700x500")
    
#     # Sidebar Menu
#     menu_frame = tk.Frame(root, bg="blue", width=200, height=500)
#     menu_frame.pack(side=tk.LEFT, fill=tk.Y)
    
#     tk.Label(menu_frame, text=f"{company_name}\nRecruiter Dashboard", fg="white", bg="blue", font=("Arial", 14, "bold")).pack(pady=20)
    
#     def load_jobs_page():
#         messagebox.showinfo("Feature", "Load Jobs Page")
    
#     def post_job():
#         messagebox.showinfo("Feature", "Post Job Page")
    
#     def search_applicants():
#         messagebox.showinfo("Feature", "Search Applicants Page")
    
#     def view_company_profile():
#         messagebox.showinfo("Feature", "Company Profile Page")
    
#     def logout():
#         root.destroy()
    
#     buttons = [
#         ("📌 Post a Job", post_job),
#         ("📋 Manage Jobs", load_jobs_page),
#         ("🔎 Search Applicants", search_applicants),
#         ("🏢 Company Profile", view_company_profile),
#         ("🚪 Logout", logout)
#     ]
    
#     for text, command in buttons:
#         tk.Button(menu_frame, text=text, bg="white", fg="black", font=("Arial", 12), command=command).pack(pady=10, fill=tk.X)
    
#     root.mainloop()

# # Setup database on first run
# setup_database()
# # Example call to open dashboard (Replace with actual recruiter_id and company_name)
# recruiter_dashboard(1, "Tech Corp")
# import sqlite3
# conn = sqlite3.connect("mydatabase.db")
# cursor = conn.cursor()
# cursor.execute("select recruiter_id , company_name from recruiters_details where user_id =3",())
# # cursor.execute("select * from users",())
# data=cursor.fetchone()
# print(data[1])'



# tree view tuturial


import tkinter as tk
from tkinter import ttk
import sqlite3

conn=sqlite3.connect("mydatabase.db")
cursor=conn.cursor()



root=tk.Tk()
root.title("Tree view")
root.geometry("1000x500")

style=ttk.Style()
style.theme_use("default")

style.configure("Treeview",background='#D3D3D3',foreground='black',rowheight=25,fieldbackground='#D3D3D3')

tree_frame=tk.Frame(root)
tree_frame.pack(pady=10)

coloumn=('Job_name','username','User_skills','email','phone_no')
mytree=ttk.Treeview(tree_frame,columns=coloumn,show="headings")
for col in coloumn:
    mytree.heading(col,text=col)
    mytree.column(col,width=150)
mytree.pack(fill=tk.BOTH,expand=True,padx=10,pady=10)

cursor.execute("select job_id , user_id from applied_jobs where recruiter_id=1")

data=cursor.fetchall()
job_ids=[row[0] for row in data ]
user_ids=[row[1] for row in data]
print(job_ids)
print(user_ids)
# print(data)
# job_id=data[0][0]
# user_id=data[0][1]
# print(job_id,user_id)
# cursor.execute('select job_position from jobs where job_id=?',(job_id,))
# job_postion=cursor.fetchall()
# # print(cursor.fetchone())
# cursor.execute('select username,email,phone_no from users where user_id=?',(user_id,))
# # print(cursor.fetchone())
# user_details=cursor.fetchall()
# applied_jobs=job_postion+user_details
# print(applied_jobs)
 

# def selected():
#         selected_item=mytree.selection()
#         print(mytree.item(selected_item)["values"])
# tk.Button(root,text="clikc here",command=selected).pack(pady=10)
      

# for job in applied_jobs:
#             mytree.insert("", tk.END, values=job)

root.mainloop()
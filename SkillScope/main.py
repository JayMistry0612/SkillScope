import tkinter as tk
from tkinter import ttk
from signup_gui import Signup  # Ensure this module correctly handles "Employee" and "Recruiter"

def main():
    root = tk.Tk()
    root.title("SkillScope - Registration")
    root.geometry("500x500")
    root.configure(bg="#f8f9fa")  # Soft gray background
    root.resizable(False, False)

    # Gradient Header
    header_frame = tk.Frame(root, bg="#007BFF", height=80)
    header_frame.pack(fill="x")

    title_label = tk.Label(header_frame, text="Welcome to SkillScope", font=("Arial", 18, "bold"),
                           fg="white", bg="#007BFF")
    title_label.place(relx=0.5, rely=0.5, anchor="center")

    # Card Frame
    card = tk.Frame(root, bg="white", padx=20, pady=20, highlightbackground="#ddd", highlightthickness=2)
    card.place(relx=0.5, rely=0.5, anchor="center", width=400, height=250)

    # Instruction Label
    instruction_label = tk.Label(card, text="Select your role to proceed:", font=("Arial", 12), fg="#333", bg="white")
    instruction_label.pack(pady=10)

    # List of user types
    user_types = ["As a User", "As a Recruiter"]
    selected_type = tk.StringVar(value=user_types[0])  # Default value

    # Styled Dropdown
    dropdown = ttk.Combobox(card, textvariable=selected_type, values=user_types, state="readonly", 
                            font=("Arial", 12), width=25)
    dropdown.pack(pady=10)

    # Proceed Button with Style
    proceed_button = tk.Button(card, text="Proceed", font=("Arial", 12, "bold"), 
                               bg="#28a745", fg="white", padx=20, pady=10, bd=0, relief="flat", cursor="hand2",
                               width=15, height=1, activebackground="#218838")
    proceed_button.pack(pady=20)

    # Function to proceed
    def proceed():
        role = "user" if selected_type.get() == user_types[0] else "recruiter"
        root.destroy()  # Close current window
        Signup(role)  # Open signup page with selected role

    proceed_button.config(command=proceed)

    # Hover effect for button
    def on_enter(e):
        proceed_button.config(bg="#218838")

    def on_leave(e):
        proceed_button.config(bg="#28a745")

    proceed_button.bind("<Enter>", on_enter)
    proceed_button.bind("<Leave>", on_leave)

    root.mainloop()

main()

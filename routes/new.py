import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to submit the teacher form and save data to the database
def submit_teacher_form():
    name = entry_name.get()
    subject = entry_subject.get()

    # Save data to the database
    conn = sqlite3.connect('teacher_data.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS teachers (name TEXT, subject TEXT)')
    cursor.execute('INSERT INTO teachers VALUES (?, ?)', (name, subject))
    conn.commit()
    conn.close()

    # Display a success message
    messagebox.showinfo("Form Submission", "Teacher information saved successfully!")

# Create the main application window
root = tk.Tk()
root.title("Teacher Form")

# Create labels and entry fields for the form
tk.Label(root, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Subject:").grid(row=1, column=0)
entry_subject = tk.Entry(root)
entry_subject.grid(row=1, column=1)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_teacher_form)
submit_button.grid(row=2, column=0, columnspan=2)

# Run the main event loop
root.mainloop()

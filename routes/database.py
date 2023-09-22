import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to submit the form and save data to the database
def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    grade = entry_grade.get()

    # Save data to the database
    conn = sqlite3.connect('student_data.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, age INTEGER, grade TEXT)')
    cursor.execute('INSERT INTO students VALUES (?, ?, ?)', (name, age, grade))
    conn.commit()
    conn.close()

    # Display a success message
    messagebox.showinfo("Form Submission", "Student information saved successfully!")

# Create the main application window
root = tk.Tk()
root.title("Student Form")

# Create labels and entry fields for the form
tk.Label(root, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Age:").grid(row=1, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1)

tk.Label(root, text="Grade:").grid(row=2, column=0)
entry_grade = tk.Entry(root)
entry_grade.grid(row=2, column=1)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, column=0, columnspan=2)

# Run the main event loop
root.mainloop()

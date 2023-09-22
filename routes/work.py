import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to submit the admin form and save data to the database
def submit_admin_form():
    username = entry_username.get()
    password = entry_password.get()

    # Save data to the database
    conn = sqlite3.connect('admin_data.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS admins (username TEXT, password TEXT)')
    cursor.execute('INSERT INTO admins VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

    # Display a success message
    messagebox.showinfo("Form Submission", "Admin information saved successfully!")

# Create the main application window
root = tk.Tk()
root.title("Admin Form")

# Create labels and entry fields for the form
tk.Label(root, text="Username:").grid(row=0, column=0)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)

tk.Label(root, text="Password:").grid(row=1, column=0)
entry_password = tk.Entry(root, show="*")  # Show * for password
entry_password.grid(row=1, column=1)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_admin_form)
submit_button.grid(row=2, column=0, columnspan=2)

# Run the main event loop
root.mainloop()

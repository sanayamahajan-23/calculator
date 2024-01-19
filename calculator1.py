from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

def show_calculator_tab():
    global signup_frame, progress_bar
    if username_entry.get() and password_entry.get() and gender_var.get() and age_combobox.get() and about_textbox.get(1.0, END) and terms_check.instate(['selected']):
        progress_bar.start(10)  # Start the progress bar
        root.after(1000, show_calculator)  # Transition to calculator tab after 1 second
    else:
        messagebox.showerror("Error", "Please fill in all the fields and accept the terms and conditions.")

def show_calculator():
    progress_bar.stop()  # Stop the progress bar
    notebook.add(calculator_frame, text="Calculator")
    
    notebook.select(calculator_frame)

def save_data():
    # Perform save operation here
    messagebox.showinfo("Save", "Data saved successfully.")

def edit_data():
    # Perform edit operation here
    messagebox.showinfo("Edit", "Editing data.")

def submit_rating():
    experience_rating = experience_scale.get()
    quality_rating = quality_spinbox.get()
    messagebox.showinfo("Rating", f"Experience Rating: {experience_rating}\nQuality Rating: {quality_rating}")

root = Tk()
root.geometry("644x700")
root.title("Calculator")

notebook = ttk.Notebook(root)
notebook.pack(fill=BOTH, expand=True)

# Signup Form tab
signup_frame = ttk.Frame(notebook)
notebook.add(signup_frame, text="Signup Form")

# Username
username_label = ttk.Label(signup_frame, text="Username:")
username_label.pack()
username_entry = ttk.Entry(signup_frame)
username_entry.pack()
username_entry.focus()

# Password
password_label = ttk.Label(signup_frame, text="Password:")
password_label.pack()
password_entry = ttk.Entry(signup_frame, show="*")
password_entry.pack()

# Gender
gender_label = ttk.Label(signup_frame, text="Gender:")
gender_label.pack()
gender_var = StringVar()
gender_var.set("Male")
gender_male_radio = ttk.Radiobutton(signup_frame, text="Male", variable=gender_var, value="Male")
gender_male_radio.pack()
gender_female_radio = ttk.Radiobutton(signup_frame, text="Female", variable=gender_var, value="Female")
gender_female_radio.pack()

# Age
age_label = ttk.Label(signup_frame, text="Age:")
age_label.pack()
age_combobox = ttk.Combobox(signup_frame, values=["18-25", "26-35", "36-45", "46+"])
age_combobox.pack()

# About
about_label = ttk.Label(signup_frame, text="About:")
about_label.pack()
about_textbox = Text(signup_frame, height=5)
about_textbox.pack()
about_scrollbar = ttk.Scrollbar(signup_frame, command=about_textbox.yview)
about_scrollbar.pack(side=RIGHT, fill=Y)
about_textbox.config(yscrollcommand=about_scrollbar.set)

# Terms and Conditions
terms_check = ttk.Checkbutton(signup_frame, text="I accept the terms and conditions")
terms_check.pack()

# Submit button
submit_button = ttk.Button(signup_frame, text="Submit", command=show_calculator_tab)
submit_button.pack()

# Progress bar
progress_bar = ttk.Progressbar(signup_frame, mode='indeterminate')
progress_bar.pack(fill=X, padx=10, pady=10)

# Calculator tab
calculator_frame = ttk.Frame(notebook)

# Rest of the calculator code...
scvalue = StringVar()
scvalue.set("")
screen = Entry(calculator_frame, textvar=scvalue, font="lucida 40 bold", borderwidth=3)
screen.pack(fill=X, ipadx=8, padx=10, pady=10)

buttons_frame = Frame(calculator_frame, bg="grey")
buttons_frame.pack()

button_list = [
    '9', '8', '7', '6', '5', '4', '3', '2', '1', 'C', '0', '=', '+', '-', '*', '/', '%'
]

row_index = 0
col_index = 0
for i, button in enumerate(button_list):
    b = Button(buttons_frame, text=button, pady=13, padx=18, font="lucid 35 bold")
    b.grid(row=row_index, column=col_index, padx=5, pady=5)
    b.bind("<Button-1>", click)
    col_index += 1
    if col_index > 3:
        col_index = 0
        row_index += 1

notebook.add(calculator_frame, text="Calculator")

# Rate Us tab
rate_us_frame = ttk.Frame(notebook)
notebook.add(rate_us_frame, text="Rate Us")

# Experience Rating
experience_label = ttk.Label(rate_us_frame, text="Experience Rating:")
experience_label.pack()
experience_scale = ttk.Scale(rate_us_frame, from_=0, to=10, orient=HORIZONTAL)
experience_scale.pack()

# Quality Rating
quality_label = ttk.Label(rate_us_frame, text="Quality Rating:")
quality_label.pack()
quality_value = StringVar()
quality_spinbox = Spinbox(rate_us_frame, from_=0, to=100, textvariable=quality_value)
quality_spinbox.pack()

# Submit button
submit_rating_button = ttk.Button(rate_us_frame, text="Submit", command=submit_rating)
submit_rating_button.pack()

# Menu Bar
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Save", command=save_data)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Edit", command=edit_data)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

root.config(menu=menu_bar)
root.configure(background="red")
root.mainloop()


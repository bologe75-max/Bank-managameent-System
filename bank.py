from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# -------------------------------
# Main Window
# -------------------------------
root = Tk()
root.title("School Management System")
root.geometry("800x500")
root.config(bg="lightblue")

students = []

# -------------------------------
# Functions
# -------------------------------

def add_student():
    sid = entry_id.get()
    name = entry_name.get()
    age = entry_age.get()
    grade = entry_grade.get()

    if sid == "" or name == "" or age == "" or grade == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    students.append([sid, name, age, grade])
    show_students()
    clear_fields()
    messagebox.showinfo("Success", "Student Added Successfully")


def show_students():
    table.delete(*table.get_children())

    for student in students:
        table.insert("", END, values=student)


def search_student():
    sid = entry_id.get()

    for student in students:
        if student[0] == sid:
            entry_name.delete(0, END)
            entry_age.delete(0, END)
            entry_grade.delete(0, END)

            entry_name.insert(0, student[1])
            entry_age.insert(0, student[2])
            entry_grade.insert(0, student[3])
            return

    messagebox.showerror("Error", "Student Not Found")


def update_student():
    sid = entry_id.get()

    for student in students:
        if student[0] == sid:
            student[1] = entry_name.get()
            student[2] = entry_age.get()
            student[3] = entry_grade.get()

            show_students()
            clear_fields()
            messagebox.showinfo("Success", "Student Updated")
            return

    messagebox.showerror("Error", "Student Not Found")


def delete_student():
    sid = entry_id.get()

    for student in students:
        if student[0] == sid:
            students.remove(student)
            show_students()
            clear_fields()
            messagebox.showinfo("Success", "Student Deleted")
            return

    messagebox.showerror("Error", "Student Not Found")


def clear_fields():
    entry_id.delete(0, END)
    entry_name.delete(0, END)
    entry_age.delete(0, END)
    entry_grade.delete(0, END)


# -------------------------------
# Labels
# -------------------------------

Label(root, text="School Management System",
      font=("Arial", 20, "bold"),
      bg="navy",
      fg="white").pack(fill=X)

Label(root, text="Student ID", bg="lightblue",
      font=("Arial", 12)).place(x=20, y=70)

Label(root, text="Name", bg="lightblue",
      font=("Arial", 12)).place(x=20, y=110)

Label(root, text="Age", bg="lightblue",
      font=("Arial", 12)).place(x=20, y=150)

Label(root, text="Grade", bg="lightblue",
      font=("Arial", 12)).place(x=20, y=190)

# -------------------------------
# Entry Boxes
# -------------------------------

entry_id = Entry(root, width=25)
entry_id.place(x=120, y=70)

entry_name = Entry(root, width=25)
entry_name.place(x=120, y=110)

entry_age = Entry(root, width=25)
entry_age.place(x=120, y=150)

entry_grade = Entry(root, width=25)
entry_grade.place(x=120, y=190)

# -------------------------------
# Buttons
# -------------------------------

Button(root, text="Add", width=12,
       bg="green", fg="white",
       command=add_student).place(x=20, y=250)

Button(root, text="Search", width=12,
       bg="blue", fg="white",
       command=search_student).place(x=140, y=250)

Button(root, text="Update", width=12,
       bg="orange", fg="white",
       command=update_student).place(x=260, y=250)

Button(root, text="Delete", width=12,
       bg="red", fg="white",
       command=delete_student).place(x=380, y=250)

Button(root, text="Clear", width=12,
       bg="gray", fg="white",
       command=clear_fields).place(x=500, y=250)

# -------------------------------
# Table
# -------------------------------

columns = ("ID", "Name", "Age", "Grade")

table = ttk.Treeview(root, columns=columns, show="headings", height=8)

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=130)

table.place(x=20, y=320)

root.mainloop()
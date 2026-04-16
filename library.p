python Got it — you want each program to be ~30–40 lines, more detailed (exam-ready), not too short.

I’ll give you 5 full programs now (each ~30–40 lines). If you want, I’ll continue the remaining 10 in the next message.

PYTHON PROGRAM INDEX (15 Topics)
📌 Real World Mini Projects List

Library Management System
Student Grading System
ATM Banking System
Contact Book Management
To-Do List Manager
Online Shopping Cart System
Login & Registration System
Bus Ticket Booking System
Quiz (MCQ) System
Notes Saving App (File Handling)
Employee Salary Management System
Password Strength Checker
Electricity Bill Calculator
Attendance Management System
Restaurant Order Billing System
---

✅ 1. Library Management System (≈35 lines)

def library_management():
    books = ["Python", "Java", "C++", "Data Science"]
    issued_books = []

    while True:
        print("\n--- Library Menu ---")
        print("1. View Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print("Available Books:", books)

        elif choice == 2:
            book = input("Enter book name to issue: ")
            if book in books:
                books.remove(book)
                issued_books.append(book)
                print("Book issued successfully")
            else:
                print("Book not available")

        elif choice == 3:
            book = input("Enter book name to return: ")
            if book in issued_books:
                issued_books.remove(book)
                books.append(book)
                print("Book returned")
            else:
                print("Invalid book")

        elif choice == 4:
            break
        else:
            print("Invalid choice")


---

✅ 2. Student Grading System (≈30 lines)

def student_grading():
    students = {}

    while True:
        print("\n--- Student Menu ---")
        print("1. Add Student")
        print("2. View Grades")
        print("3. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            name = input("Enter name: ")
            marks = int(input("Enter marks: "))

            if marks >= 90:
                grade = 'A'
            elif marks >= 75:
                grade = 'B'
            elif marks >= 50:
                grade = 'C'
            else:
                grade = 'F'

            students[name] = grade
            print("Student added")

        elif choice == 2:
            for s, g in students.items():
                print(s, ":", g)

        elif choice == 3:
            break
        else:
            print("Invalid choice")


---

✅ 3. ATM System (≈35 lines)

def atm_system():
    balance = 1000

    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print("Balance:", balance)

        elif choice == 2:
            amount = int(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print("Deposited successfully")
            else:
                print("Invalid amount")

        elif choice == 3:
            amount = int(input("Enter withdraw amount: "))
            if amount <= balance:
                balance -= amount
                print("Withdraw successful")
            else:
                print("Insufficient balance")

        elif choice == 4:
            break
        else:
            print("Invalid choice")


---

✅ 4. Contact Book System (≈35 lines)

def contact_book():
    contacts = {}

    while True:
        print("\n--- Contact Menu ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            contacts[name] = phone
            print("Contact saved")

        elif choice == 2:
            name = input("Enter name to search: ")
            if name in contacts:
                print("Phone:", contacts[name])
            else:
                print("Not found")

        elif choice == 3:
            for name, phone in contacts.items():
                print(name, ":", phone)

        elif choice == 4:
            break
        else:
            print("Invalid choice")


---

✅ 5. To-Do List Manager (≈30 lines)

def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            task = input("Enter task: ")
            tasks.append(task)
            print("Task added")

        elif choice == 2:
            if len(tasks) == 0:
                print("No tasks")
            else:
                for i in range(len(tasks)):
                    print(i+1, tasks[i])

        elif choice == 3:
            num = int(input("Enter task number: "))
            if 0 < num <= len(tasks):
                tasks.pop(num-1)
                print("Task deleted")
            else:
                print("Invalid number")

        elif choice == 4:
            break
        else:
            print("Invalid choice")


Nice — now you’re thinking like examiner level 👍
You want real-world scenario programs (30–40 lines each). I’ll give 10 practical mini-projects you can directly write in lab.


---

✅ 6. Online Shopping Cart System

def shopping_cart():
    cart = {}
    
    while True:
        print("\n--- Shopping Cart ---")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Cart")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            item = input("Item name: ")
            qty = int(input("Quantity: "))
            cart[item] = cart.get(item, 0) + qty
            print("Item added")

        elif choice == 2:
            item = input("Item to remove: ")
            if item in cart:
                del cart[item]
                print("Removed")
            else:
                print("Item not found")

        elif choice == 3:
            for i, q in cart.items():
                print(i, ":", q)

        elif choice == 4:
            break


---

✅ 7. Simple Login & Registration System

def login_system():
    users = {}

    while True:
        print("\n--- Login System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        ch = int(input("Choice: "))

        if ch == 1:
            u = input("Username: ")
            p = input("Password: ")
            users[u] = p
            print("Registered")

        elif ch == 2:
            u = input("Username: ")
            p = input("Password: ")

            if u in users and users[u] == p:
                print("Login success")
            else:
                print("Invalid credentials")

        elif ch == 3:
            break


---

✅ 8. Bus Ticket Booking System

def bus_booking():
    seats = [0]*10   # 0 = free, 1 = booked

    while True:
        print("\n--- Bus Booking ---")
        print("1. View Seats")
        print("2. Book Seat")
        print("3. Cancel Seat")
        print("4. Exit")

        ch = int(input("Choice: "))

        if ch == 1:
            print("Seats:", seats)

        elif ch == 2:
            s = int(input("Seat number (0-9): "))
            if seats[s] == 0:
                seats[s] = 1
                print("Booked")
            else:
                print("Already booked")

        elif ch == 3:
            s = int(input("Seat to cancel: "))
            if seats[s] == 1:
                seats[s] = 0
                print("Cancelled")
            else:
                print("Not booked")

        elif ch == 4:
            break


---

✅ 9. Quiz System (MCQ)

def quiz_system():
    questions = {
        "Capital of India?": "Delhi",
        "2+2?": "4",
        "Python is language?": "Yes"
    }

    score = 0

    for q, ans in questions.items():
        user = input(q + ": ")
        if user.lower() == ans.lower():
            score += 1

    print("Score:", score, "/", len(questions))


---

✅ 10. File-Based Notes Saver

def notes_app():
    while True:
        print("\n--- Notes App ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        ch = int(input("Choice: "))

        if ch == 1:
            note = input("Enter note: ")
            with open("notes.txt", "a") as f:
                f.write(note + "\n")
            print("Saved")

        elif ch == 2:
            try:
                with open("notes.txt", "r") as f:
                    print(f.read())
            except:
                print("No notes found")

        elif ch == 3:
            break


---

✅ 11. Employee Salary Management

def employee_salary():
    employees = {}

    while True:
        print("\n--- Employee System ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Exit")

        ch = int(input("Choice: "))

        if ch == 1:
            name = input("Name: ")
            salary = int(input("Salary: "))
            employees[name] = salary

        elif ch == 2:
            for n, s in employees.items():
                print(n, ":", s)

        elif ch == 3:
            break


---

✅ 12. Password Strength Checker

def password_checker():
    pwd = input("Enter password: ")

    if len(pwd) < 6:
        print("Weak password")
    elif any(c.isdigit() for c in pwd) and any(c.isalpha() for c in pwd):
        print("Strong password")
    else:
        print("Medium password")


---

✅ 13. Electricity Bill Calculator

def electricity_bill():
    units = int(input("Enter units: "))

    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = units * 3
    else:
        bill = units * 5

    print("Total bill:", bill)


---

✅ 14. Attendance Management System

def attendance():
    students = {}

    while True:
        print("\n--- Attendance ---")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")

        ch = int(input("Choice: "))

        if ch == 1:
            name = input("Student name: ")
            status = input("Present/Absent: ")
            students[name] = status

        elif ch == 2:
            for n, s in students.items():
                print(n, ":", s)

        elif ch == 3:
            break


---

✅ 15. Restaurant Order System

def restaurant_order():
    menu = {"Burger": 100, "Pizza": 200, "Juice": 50}
    total = 0

    while True:
        print("\nMenu:", menu)
        item = input("Enter item (or exit): ")

        if item == "exit":
            break

        if item in menu:
            qty = int(input("Quantity: "))
            total += menu[item] * qty
        else:
            print("Invalid item")

    print("Total bill:", total)

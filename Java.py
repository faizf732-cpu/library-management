Java  having both Python + Java versions gives you a big advantage in lab exams 👍

I’ll give you 5 real-world Java programs (each ~30–40 lines, menu-based, exam-ready). If you want, I’ll continue 


JAVA PROGRAM INDEX (15 Topics)
📌 Real World Mini Projects List

Library Management System
Student Grading System
ATM Banking System
Bus Ticket Booking System
Shopping Cart System
Contact Book System
To-Do List Manager
Quiz System (MCQ)
Employee Salary Management System
Notes App (File Handling)
Electricity Bill Calculator
Attendance Management System
Restaurant Order System
Password Strength Checker
Prime Number Checker

✅ 1. Library Management System (Java)

import java.util.*;

public class LibraryManagement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> books = new ArrayList<>(Arrays.asList("Java", "Python", "C++"));
        ArrayList<String> issued = new ArrayList<>();

        while (true) {
            System.out.println("\n--- Library Menu ---");
            System.out.println("1. View Books\n2. Issue Book\n3. Return Book\n4. Exit");
            int ch = sc.nextInt();
            sc.nextLine();

            if (ch == 1) {
                System.out.println("Available: " + books);
            } 
            else if (ch == 2) {
                System.out.print("Enter book: ");
                String b = sc.nextLine();
                if (books.contains(b)) {
                    books.remove(b);
                    issued.add(b);
                    System.out.println("Issued");
                } else {
                    System.out.println("Not available");
                }
            } 
            else if (ch == 3) {
                System.out.print("Return book: ");
                String b = sc.nextLine();
                if (issued.contains(b)) {
                    issued.remove(b);
                    books.add(b);
                    System.out.println("Returned");
                } else {
                    System.out.println("Invalid");
                }
            } 
            else break;
        }
    }
}


---

✅ 2. Student Grading System (Java)

import java.util.*;

public class StudentGrading {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashMap<String, String> students = new HashMap<>();

        while (true) {
            System.out.println("\n1.Add 2.View 3.Exit");
            int ch = sc.nextInt();
            sc.nextLine();

            if (ch == 1) {
                System.out.print("Name: ");
                String name = sc.nextLine();
                System.out.print("Marks: ");
                int marks = sc.nextInt();

                String grade;
                if (marks >= 90) grade = "A";
                else if (marks >= 75) grade = "B";
                else if (marks >= 50) grade = "C";
                else grade = "F";

                students.put(name, grade);
            } 
            else if (ch == 2) {
                for (String s : students.keySet()) {
                    System.out.println(s + " : " + students.get(s));
                }
            } 
            else break;
        }
    }
}


---

✅ 3. ATM System (Java)

import java.util.*;

public class ATMSystem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int balance = 1000;

        while (true) {
            System.out.println("\n1.Balance 2.Deposit 3.Withdraw 4.Exit");
            int ch = sc.nextInt();

            if (ch == 1) {
                System.out.println("Balance: " + balance);
            } 
            else if (ch == 2) {
                System.out.print("Amount: ");
                int amt = sc.nextInt();
                if (amt > 0) balance += amt;
            } 
            else if (ch == 3) {
                System.out.print("Amount: ");
                int amt = sc.nextInt();
                if (amt <= balance) balance -= amt;
                else System.out.println("Insufficient");
            } 
            else break;
        }
    }
}


---

✅ 4. Bus Ticket Booking System (Java)

import java.util.*;

public class BusBooking {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int seats[] = new int[10];

        while (true) {
            System.out.println("\n1.View 2.Book 3.Cancel 4.Exit");
            int ch = sc.nextInt();

            if (ch == 1) {
                System.out.println(Arrays.toString(seats));
            } 
            else if (ch == 2) {
                System.out.print("Seat no: ");
                int s = sc.nextInt();
                if (seats[s] == 0) {
                    seats[s] = 1;
                    System.out.println("Booked");
                } else {
                    System.out.println("Already booked");
                }
            } 
            else if (ch == 3) {
                System.out.print("Seat no: ");
                int s = sc.nextInt();
                if (seats[s] == 1) {
                    seats[s] = 0;
                    System.out.println("Cancelled");
                }
            } 
            else break;
        }
    }
}


---

✅ 5. Shopping Cart System (Java)

import java.util.*;

public class ShoppingCart {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashMap<String, Integer> cart = new HashMap<>();

        while (true) {
            System.out.println("\n1.Add 2.Remove 3.View 4.Exit");
            int ch = sc.nextInt();
            sc.nextLine();

            if (ch == 1) {
                System.out.print("Item: ");
                String item = sc.nextLine();
                System.out.print("Qty: ");
                int qty = sc.nextInt();
                cart.put(item, cart.getOrDefault(item, 0) + qty);
            } 
            else if (ch == 2) {
                System.out.print("Item: ");
                String item = sc.nextLine();
                cart.remove(item);
            } 
            else if (ch == 3) {
                System.out.println(cart);
            } 
            else break;
        }
    }
}


Perfect — here are the remaining 10 Java programs, all real-world, ~30–40 lines, menu/logic based, exam-ready 👍


---

✅ 6. Contact Book System (Java)

import java.util.*;

public class ContactBook {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashMap<String, String> contacts = new HashMap<>();

        while (true) {
            System.out.println("\n1.Add 2.Search 3.Display 4.Exit");
            int ch = sc.nextInt();
            sc.nextLine();

            if (ch == 1) {
                System.out.print("Name: ");
                String name = sc.nextLine();
                System.out.print("Phone: ");
                String phone = sc.nextLine();
                contacts.put(name, phone);
            } 
            else if (ch == 2) {
                System.out.print("Search name: ");
                String name = sc.nextLine();
                if (contacts.containsKey(name))
                    System.out.println("Phone: " + contacts.get(name));
                else
                    System.out.println("Not found");
            } 
            else if (ch == 3) {
                for (String n : contacts.keySet())
                    System.out.println(n + " : " + contacts.get(n));
            } 
            else break;
        }
    }
}


---

✅ 7. To-Do List Manager (Java)

import java.util.*;

public class TodoList {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> tasks = new ArrayList<>();

        while (true) {
            System.out.println("\n1.Add 2.View 3.Delete 4.Exit");
            int ch = sc.nextInt();
            sc.nextLine();

            if (ch == 1) {
                System.out.print("Task: ");
                tasks.add(sc.nextLine());
            } 
            else if (ch == 2) {
                for (int i = 0; i < tasks.size(); i++)
                    System.out.println((i+1) + ". " + tasks.get(i));
            } 
            else if (ch == 3) {
                System.out.print("Task number: ");
                int n = sc.nextInt();
                if (n > 0 && n <= tasks.size())
                    tasks.remove(n-1);
            } 
            else break;
        }
    }
}


---

✅ 8. Quiz System (Java)

import java.util.*;

public class QuizSystem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[][] q = {
            {"Capital of India?", "Delhi"},
            {"2+2?", "4"},
            {"Java is language?", "Yes"}
        };

        int score = 0;

        for (int i = 0; i < q.length; i++) {
            System.out.print(q[i][0] + " ");
            String ans = sc.nextLine();

            if (ans.equalsIgnoreCase(q[i][1])) {
                score++;
            }
        }

        System.out.println("Score: " + score + "/" + q.length);
    }
}


---

✅ 9. Employee Salary System (Java)

import java.util.*;

public class EmployeeSystem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashMap<String, Integer> emp = new HashMap<>();

        while (true) {
            System.out.println("\n1.Add 2.View 3.Exit");
            int ch = sc.nextInt();
            sc.nextLine();

            if (ch == 1) {
                System.out.print("Name: ");
                String name = sc.nextLine();
                System.out.print("Salary: ");
                int sal = sc.nextInt();
                emp.put(name, sal);
            } 
            else if (ch == 2) {
                for (String e : emp.keySet())
                    System.out.println(e + " : " + emp.get(e));
            } 
            else break;
        }
    }
}


---

✅ 10. Notes File System (Java - File Handling)

import java.util.*;
import java.io.*;

public class NotesApp {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("\n1.Add Note 2.View Notes 3.Exit");
            int ch = sc.nextInt();
            sc.nextLine();

            if (ch == 1) {
                System.out.print("Enter note: ");
                String note = sc.nextLine();
                FileWriter fw = new FileWriter("notes.txt", true);
                fw.write(note + "\n");
                fw.close();
            } 
            else if (ch == 2) {
                File file = new File("notes.txt");
                Scanner fr = new Scanner(file);
                while (fr.hasNextLine())
                    System.out.println(fr.nextLine());
                fr.close();
            } 
            else break;
        }
    }
}


---

✅ 11. Electricity Bill Calculator (Java)

import java.util.*;

public class ElectricityBill {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter units: ");
        int units = sc.nextInt();
        int bill;

        if (units <= 100)
            bill = units * 2;
        else if (units <= 200)
            bill = units * 3;
        else
            bill = units * 5;

        System.out.println("Total Bill: " + bill);
    }
}


---

✅ 12. Attendance System (Java)

import java.util.*;

public class AttendanceSystem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashMap<String, String> att = new HashMap<>();

        while (true) {
            System.out.println("\n1.Mark 2.View 3.Exit");
            int ch = sc.nextInt();
            sc.nextLine();

            if (ch == 1) {
                System.out.print("Name: ");
                String name = sc.nextLine();
                System.out.print("Status: ");
                String status = sc.nextLine();
                att.put(name, status);
            } 
            else if (ch == 2) {
                for (String s : att.keySet())
                    System.out.println(s + " : " + att.get(s));
            } 
            else break;
        }
    }
}


---

✅ 13. Restaurant Order System (Java)

import java.util.*;

public class Restaurant {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        HashMap<String, Integer> menu = new HashMap<>();
        menu.put("Burger", 100);
        menu.put("Pizza", 200);
        menu.put("Juice", 50);

        int total = 0;

        while (true) {
            System.out.println(menu);
            System.out.print("Enter item (exit to stop): ");
            String item = sc.nextLine();

            if (item.equals("exit"))
                break;

            if (menu.containsKey(item)) {
                System.out.print("Qty: ");
                int q = sc.nextInt();
                sc.nextLine();
                total += menu.get(item) * q;
            } 
            else {
                System.out.println("Invalid item");
            }
        }

        System.out.println("Total Bill: " + total);
    }
}


---

✅ 14. Password Strength Checker (Java)

import java.util.*;

public class PasswordChecker {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter password: ");
        String pwd = sc.nextLine();

        boolean hasDigit = false, hasAlpha = false;

        for (char c : pwd.toCharArray()) {
            if (Character.isDigit(c)) hasDigit = true;
            if (Character.isLetter(c)) hasAlpha = true;
        }

        if (pwd.length() < 6)
            System.out.println("Weak");
        else if (hasDigit && hasAlpha)
            System.out.println("Strong");
        else
            System.out.println("Medium");
    }
}


---

✅ 15. Prime Number Checker (Java)

import java.util.*;

public class PrimeCheck {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number: ");
        int n = sc.nextInt();
        boolean prime = true;

        if (n <= 1) prime = false;

        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                prime = false;
                break;
            }
        }

        if (prime)
            System.out.println("Prime");
        else
            System.out.println("Not Prime");
    }
}


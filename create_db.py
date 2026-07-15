import sqlite3

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect("database.db")

# Create a cursor
cursor = conn.cursor()

# Create Employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER NOT NULL,
    city TEXT NOT NULL
)
""")

# Insert sample data
employees = [
    ("Rahul", "IT", 60000, "Mumbai"),
    ("Priya", "HR", 45000, "Pune"),
    ("Amit", "Finance", 70000, "Delhi"),
    ("Sneha", "IT", 55000, "Mumbai"),
    ("Rohan", "Sales", 50000, "Bangalore"),
    ("Neha", "Marketing", 48000, "Pune"),
    ("Arjun", "IT", 80000, "Hyderabad"),
    ("Kiran", "HR", 52000, "Mumbai"),

    ("Anjali", "Finance", 68000, "Mumbai"),
    ("Vikram", "IT", 75000, "Pune"),
    ("Meera", "Marketing", 54000, "Delhi"),
    ("Karan", "Sales", 47000, "Mumbai"),
    ("Pooja", "HR", 51000, "Hyderabad"),
    ("Aditya", "IT", 90000, "Bangalore"),
    ("Ritika", "Finance", 62000, "Pune"),
    ("Saurabh", "IT", 58000, "Delhi"),
    ("Divya", "Marketing", 61000, "Mumbai"),
    ("Manish", "Sales", 46000, "Hyderabad"),
    ("Komal", "HR", 49000, "Bangalore"),
    ("Nikhil", "IT", 85000, "Mumbai"),
    ("Shreya", "Finance", 73000, "Delhi"),
    ("Yash", "IT", 67000, "Pune"),
    ("Tanvi", "Marketing", 53000, "Mumbai"),
    ("Harsh", "Sales", 52000, "Delhi"),
    ("Isha", "HR", 56000, "Pune"),
    ("Akash", "IT", 78000, "Hyderabad"),
    ("Simran", "Finance", 69000, "Bangalore"),
    ("Ritesh", "Sales", 44000, "Mumbai"),
    ("Ayesha", "Marketing", 59000, "Pune"),
    ("Deepak", "IT", 81000, "Delhi")
]

cursor.executemany("""
INSERT INTO employees (name, department, salary, city)
VALUES (?, ?, ?, ?)
""", employees)

# Save changes
conn.commit()

# Close connection
conn.close()

print("Database created successfully!")
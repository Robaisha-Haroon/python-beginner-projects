class StudentSystem:

  def __init__(self):
    self.students = []

  def add_student(self):
    sid = input("Enter Student ID: ")

    # Check if ID already exists
    for s in self.students:
      if s["id"] == sid:
        print("Error: This ID already exists!")
        return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student_dict = {"id": sid, "name": name, "age": age, "course": course}
    self.students.append(student_dict)
    print("Student added successfully!")

  def view_students(self):
    if len(self.students) == 0:
      print("No records found.")
      return

    print("\n--- All Student Records ---")
    for s in self.students:
      print(
          f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Course:"
          f" {s['course']}"
      )
    print("---------------------------")

  def update_student(self):
    sid = input("Enter Student ID to update: ")

    for s in self.students:
      if s["id"] == sid:
        s["name"] = input("Enter new Name: ")
        s["age"] = input("Enter new Age: ")
        s["course"] = input("Enter new Course: ")
        print("Student updated successfully!")
        return

    print("Error: Student ID does not exist!")


# Main Program Loop
system = StudentSystem()

while True:
  print("\n=== Student Management System ===")
  print("1. Add Student")
  print("2. View All Students")
  print("3. Update Student")
  print("4. Exit")

  choice = input("Choose an option (1-4): ")

  if choice == "1":
    system.add_student()
  elif choice == "2":
    system.view_students()
  elif choice == "3":
    system.update_student()
  elif choice == "4":
    print("Closing program. Goodbye!")
    break
  else:
    print("Invalid choice! Please enter a number from 1 to 4.")

# الدالة الاولى
def show_menu():
    print("-"*5,"STUDENT MANAGEMENT SYSTEM","-"*5)
    print("1. Add new students (ID and Name)")
    print("2. View all students")
    print("3. Search student by ID")
    print("4. Search student by Name")
    print("5. Delete a student")
    print("6. Save all data to a file")
    print("7. Load data from a file")
    print("8. Exit")
    print("-"*40)
#show_menu()
# الدالة الثانية
def add_student(ids_list, names_list): # مررنا بارامترز
    try:  # عشان ما يعمل crash
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Error: ID must be numeric")
        return
    if student_id in ids_list:
       print(f"Error: ID {student_id} already exists")
       return
    student_name = input("Enter student name: ").strip()
    if student_name == "" :
        print("Error: student name cannot be empty")
        return
#اضافة الطالب الى القوائم
    ids_list.append(student_id)
    names_list.append(student_name)
    print("Student added successfully")

# الدالة الثالثة
def view_all_students(ids_list, names_list):
    if len(ids_list) == 0 :
        print("No students found")
        return
    print("ID\t\tName")
    print("-" * 40)
    for i in range(len(ids_list)):
        print(f"{ids_list[i]}\t\t{names_list[i]}")
    print("-" * 40)
    print("Total Students:", len(ids_list))

# الدالة الرابعة
def search_by_id(ids_list, names_list):
    if len(ids_list) == 0: # التحقق من وجود الطلاب
        print("No students found!")
        return
    try:
        search_id = int(input("Enter Student ID to search for: "))
    except ValueError:
        print("Invalid input! ID must be numeric.")
        return
    found = False
    for i in range(len(ids_list)):
        if ids_list[i] == search_id:
            print("Student Found:")
            print("ID:", ids_list[i])
            print("Name:", names_list[i])
            found = True
            break
    if not found:
        print("Student not found!")

# الدالة الخامسة
def search_by_name(ids_list, names_list):
    if len(ids_list) == 0:
        print("No students found")
        return
    search_name = input("Enter student name: ").strip()
    found = False
    for i in range(len(names_list)):
        if search_name.lower() in names_list[i].lower():
            print("Student Found:")
            print("ID:", ids_list[i])
            print("Name:", names_list[i])
            found = True
            break
    if not found:
        print("Student not found!")
# الدالة السادسة
def delete_by_id(ids_list, names_list):
    if len(ids_list) == 0:
        print("No students found")
        return
    try:
        delete_id = int(input("Enter Student ID to delete: "))
    except ValueError:
        print("Invalid input! ID must be numeric.")
        return
    if delete_id in ids_list:
        index = ids_list.index(delete_id)
        print("\nStudent found:")
        print("ID:", delete_id)
        print("Name:", names_list[index])
        confirm = input("Are you sure you want to delete this student? (y/n): ").strip().lower()
        if confirm == "yes":
            ids_list.pop(index)
            names_list.pop(index)
            print("Student deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print("Student not found!")

# الدالة السابعة
def save_to_file(ids_list, names_list):
    if len(ids_list) == 0:
        print("No students to save!")
        return
    file = open("students.txt", "w")
    for i in range(len(ids_list)):
        file.write(f"{ids_list[i]}, {names_list[i]}\n")
    file.close()
    print("Students saved successfully!")

#الدالة الثامنة
def load_from_file(ids_list, names_list):
    try:
        file = open("students.txt", "r")
        ids_list.clear()
        names_list.clear()
        for line in file:
            line = line.strip().split(",")
            if len(line) == 2:
                student_id = int(line[0])
                student_name = line[1]
                ids_list.append(student_id)
                names_list.append(student_name)
        file.close()
        print("Data loaded successfully from students.txt!")
    except FileNotFoundError:
        print("No saved file found!")


def main():
    student_ids = []
    student_names = []
    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ")
        if choice == "1":
            add_student(student_ids, student_names)
        elif choice == "2":
            view_all_students(student_ids, student_names)
        elif choice == "3":
            search_by_id(student_ids, student_names)
        elif choice == "4":
            search_by_name(student_ids, student_names)
        elif choice == "5":
            delete_by_id(student_ids, student_names)
        elif choice == "6":
            save_to_file(student_ids, student_names)
        elif choice == "7":
            load_from_file(student_ids, student_names)
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-8")
main()